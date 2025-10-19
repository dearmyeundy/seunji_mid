import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(layout="wide")
st.title("🚀 인터랙티브 포물선 발사 실험실")
st.markdown("---")

# 사이드바: 실험 조건
st.sidebar.header("실험 조건 설정")
v0 = st.sidebar.slider("1) 초기 속도 v₀ (m/s)", 1.0, 50.0, 20.0, 0.5)
angle_deg = st.sidebar.slider("2) 발사 각도 θ (°)", 0, 90, 45, 1)
g = st.sidebar.slider("3) 중력 가속도 g (m/s²)", 0.5, 20.0, 9.8, 0.01)
points = st.sidebar.slider("해상도 (그래프 점 개수)", 100, 2000, 500, 100)
control_mode = st.sidebar.radio("시간 제어 방식", ["슬라이더로 직접 조작", "재생(애니메이션)"])

angle_rad = np.radians(angle_deg)

# 물리량 계산 (안전 처리)
if g <= 0:
    g = 9.8
T = 0.0
if v0 > 0 and (angle_deg % 180) != 0:
    T = max(0.0, (2 * v0 * np.sin(angle_rad)) / g)
else:
    T = 0.0

# 주요 물리량 출력
R = (v0**2 * np.sin(2 * angle_rad)) / g if T > 0 else 0.0
H = (v0**2 * np.sin(angle_rad)**2) / (2 * g) if T > 0 else 0.0

col1, col2, col3 = st.columns(3)
col1.metric("비행 시간 T (s)", f"{T:.2f}")
col2.metric("최대 도달 거리 R (m)", f"{R:.2f}")
col3.metric("최대 높이 H (m)", f"{H:.2f}")

st.markdown("---")

# 시간 배열 및 궤적 계산
if T <= 0:
    t = np.linspace(0, 1.0, points)
else:
    t = np.linspace(0, T, points)
x = v0 * np.cos(angle_rad) * t
y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2
vx = np.full_like(t, v0 * np.cos(angle_rad))
vy = v0 * np.sin(angle_rad) - g * t
speed = np.sqrt(vx**2 + vy**2)

# 그리기 함수 (재사용 목적)
def _draw_figs(t_arr, x_arr, y_arr, vy_arr, t_now, vx_arr, speed_arr):
    i_now = int(np.clip((t_now / (t_arr[-1] if t_arr[-1] > 0 else 1.0)) * (len(t_arr) - 1), 0, len(t_arr) - 1))

    # 1) 궤적 (x-y)
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.plot(x_arr, y_arr, color="tab:blue", lw=2)
    ax1.scatter([x_arr[i_now]], [y_arr[i_now]], color="red", zorder=5)
    ax1.set_xlabel("수평 거리 x (m)")
    ax1.set_ylabel("수직 높이 y (m)")
    ax1.set_title("포물선 궤적")
    ax1.grid(True)
    ax1.set_xlim(0, max(1.0, x_arr.max()*1.05))
    ax1.set_ylim(0, max(0.1, y_arr.max()*1.1))

    # 2) y(t) 그래프
    fig2, ax2 = plt.subplots(figsize=(6, 2.5))
    ax2.plot(t_arr, y_arr, color="tab:green")
    ax2.axvline(t_now, color="red", linestyle="--", alpha=0.7)
    ax2.scatter([t_arr[i_now]], [y_arr[i_now]], color="red")
    ax2.set_xlabel("시간 t (s)")
    ax2.set_ylabel("높이 y (m)")
    ax2.set_title("시간-높이 그래프 (y-t)")
    ax2.grid(True)

    # 3) vy(t) 그래프
    fig3, ax3 = plt.subplots(figsize=(6, 2.5))
    ax3.plot(t_arr, vy_arr, color="tab:orange", label="vy(t)")
    ax3.axvline(t_now, color="red", linestyle="--", alpha=0.7)
    ax3.scatter([t_arr[i_now]], [vy_arr[i_now]], color="red")
# (함수 _draw_figs는 위로 이동되었습니다)

# 그리기 함수 (재사용 목적)
def _draw_figs(t_arr, x_arr, y_arr, vy_arr, t_now, vx_arr, speed_arr):
    i_now = int(np.clip((t_now / (t_arr[-1] if t_arr[-1] > 0 else 1.0)) * (len(t_arr) - 1), 0, len(t_arr) - 1))

    # 1) 궤적 (x-y)
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.plot(x_arr, y_arr, color="tab:blue", lw=2)
    ax1.scatter([x_arr[i_now]], [y_arr[i_now]], color="red", zorder=5)
    ax1.set_xlabel("수평 거리 x (m)")
    ax1.set_ylabel("수직 높이 y (m)")
    ax1.set_title("포물선 궤적")
    ax1.grid(True)
    ax1.set_xlim(0, max(1.0, x_arr.max()*1.05))
    ax1.set_ylim(0, max(0.1, y_arr.max()*1.1))

    # 2) y(t) 그래프
    fig2, ax2 = plt.subplots(figsize=(6, 2.5))
    ax2.plot(t_arr, y_arr, color="tab:green")
    ax2.axvline(t_now, color="red", linestyle="--", alpha=0.7)
    ax2.scatter([t_arr[i_now]], [y_arr[i_now]], color="red")
    ax2.set_xlabel("시간 t (s)")
    ax2.set_ylabel("높이 y (m)")
    ax2.set_title("시간-높이 그래프 (y-t)")
    ax2.grid(True)

    # 3) vy(t) 그래프
    fig3, ax3 = plt.subplots(figsize=(6, 2.5))
    ax3.plot(t_arr, vy_arr, color="tab:orange", label="vy(t)")
    ax3.axvline(t_now, color="red", linestyle="--", alpha=0.7)
    ax3.scatter([t_arr[i_now]], [vy_arr[i_now]], color="red")
    ax3.set_xlabel("시간 t (s)")
    ax3.set_ylabel("수직 속도 vy (m/s)")
    ax3.set_title("시간-속도 그래프 (vy-t)")
    ax3.grid(True)
    ax3.legend()

    return fig1, fig2, fig3

# 메인 영역: 그림 출력
# 시간 제어: 슬라이더 또는 단순 재생 버튼으로 t_visible을 정의
if control_mode == "슬라이더로 직접 조작":
    t_visible = st.slider("관찰 시간 t (s)", 0.0, T if T > 0 else 1.0, 0.0, 0.01)
else:
    play = st.button("재생(단순)")
    if play:
        t_visible = T if T > 0 else 1.0
    else:
        t_visible = 0.0

fig_traj, fig_yt, fig_vyt = _draw_figs(t, x, y, vy, t_visible, vx, speed)
left, right = st.columns([2, 1])
with left:
    st.pyplot(fig_traj)
with right:
    st.pyplot(fig_yt)
    st.pyplot(fig_vyt)

st.markdown("---")
st.subheader("📝 사용된 주요 공식")
st.latex(r'''
x(t) = v_0 \cos(\theta)\, t \\
y(t) = v_0 \sin(\theta)\, t - \tfrac{1}{2} g t^2 \\
v_y(t) = v_0 \sin(\theta) - g t
''')
st.caption("시간 슬라이더로 특정 순간을 선택하면 해당 순간에 대한 궤적상의 위치와 y-t, vy-t 그래프의 점/보조선이 함께 표시됩니다. 재생 버튼은 간단한 애니메이션을 제공합니다.")
