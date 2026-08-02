import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# --- 1. PARAMETRIT ---
x_event = 2.0
ct_event = 3.0

betas_forward = np.linspace(-0.9, 0.9, 120)
betas_backward = np.linspace(0.9, -0.9, 120)
betas = np.concatenate([betas_forward, betas_backward])

# --- 2. KUVAJAN ALUSTUS ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5), facecolor='#0f111a')

lim = 6
x_vals = np.linspace(-lim, lim, 100)

for ax in (ax1, ax2):
  ax.set_facecolor('#0f111a')
  ax.set_xlim(-lim, lim)
  ax.set_ylim(-lim, lim)
  ax.grid(True, color='#2e3440', linestyle=':', alpha=0.7)
  ax.tick_params(colors='#d8dee9')
  for spine in ax.spines.values():
    spine.set_color('#4c566a')

  # Valokartio (ct = ±x), invariantti kaikissa koordinaatistoissa
  ax.plot(
      x_vals, x_vals, color='#d8dee9', linestyle='-.', alpha=0.35, label='Valokartio ($c$)'
  )
  ax.plot(x_vals, -x_vals, color='#d8dee9', linestyle='-.', alpha=0.35)

# Akselit ja elementit (S-järjestelmä)
ax1.axhline(0, color='#81a1c1', linewidth=1.5)
ax1.axvline(0, color='#81a1c1', linewidth=1.5)
(line_x_prime,) = ax1.plot([], [], color='#a3be8c', linestyle='--', linewidth=1.5, label=r"$x'$ -akseli")
(line_ct_prime,) = ax1.plot([], [], color='#bf616a', linestyle='--', linewidth=1.5, label=r"$ct'$ -akseli")
ax1.plot(x_event, ct_event, 'o', color='#ebcb8b', markersize=8, zorder=5, label=f'E ({x_event}, {ct_event})')

ax1.set_xlabel(r'Paikka $x$', color='#d8dee9')
ax1.set_ylabel(r'Aika $ct$', color='#d8dee9')
ax1.set_title(r'LEPOJÄRJESTELMÄ $S$' + '\n' + r'Kallistuvat $S^\prime$-akselit', color='#88c0d0')
ax1.legend(loc='upper left', facecolor='#1a1c23', edgecolor='#4c566a', fontsize=9)

# Akselit ja elementit (S'-järjestelmä)
ax2.axhline(0, color='#a3be8c', linewidth=1.5)
ax2.axvline(0, color='#bf616a', linewidth=1.5)
(path_S_prime,) = ax2.plot([], [], color='#ebcb8b', linestyle=':', alpha=0.6, linewidth=1.5, label='Hyperbelirata ($s^2 = -5$)')
(point_S_prime,) = ax2.plot([], [], 'o', color='#ebcb8b', markersize=8, zorder=5, label=r'Tapahtuma E ($x^\prime, ct^\prime$)')

ax2.set_xlabel(r"Paikka $x'$", color='#d8dee9')
ax2.set_ylabel(r"Aika $ct'$", color='#d8dee9')
ax2.set_title(r'LIIKKUVA JÄRJESTELMÄ $S^\prime$' + '\n' + r'Pisteen E liikerata $(x^\prime, ct^\prime)$', color='#88c0d0')
ax2.legend(loc='upper left', facecolor='#1a1c23', edgecolor='#4c566a', fontsize=9)

title_text = fig.suptitle('', color='#d8dee9', fontsize=12, y=0.98)
x_prime_hist, ct_prime_hist = [], []

# --- 3. PÄIVITYSFUNKTIO ---
def update(frame):
  v_rel = betas[frame]

  if abs(v_rel) < 1e-4:
    v_rel = 1e-4 if v_rel >= 0 else -1e-4

  gamma = 1.0 / np.sqrt(1.0 - v_rel**2)

  x_p = gamma * (x_event - v_rel * ct_event)
  ct_p = gamma * (ct_event - v_rel * x_event)

  x_prime_hist.append(x_p)
  ct_prime_hist.append(ct_p)

  if len(x_prime_hist) > 100:
    x_prime_hist.pop(0)
    ct_prime_hist.pop(0)

  y_x_prime = np.clip(v_rel * x_vals, -100, 100)
  y_ct_prime = np.clip(x_vals / v_rel, -100, 100)

  line_x_prime.set_data(x_vals, y_x_prime)
  line_ct_prime.set_data(x_vals, y_ct_prime)

  point_S_prime.set_data([x_p], [ct_p])
  path_S_prime.set_data(x_prime_hist, ct_prime_hist)

  title_text.set_text(
      rf'v = {v_rel:.2f}c  |  $\gamma$ = {gamma:.3f}  |  E = ({x_p:.2f}, {ct_p:.2f})'
  )

  return (
      line_x_prime,
      line_ct_prime,
      point_S_prime,
      path_S_prime,
      title_text,
  )

# --- 4. ANIMAATION SUORITUS ---
global ani
ani = animation.FuncAnimation(
    fig, update, frames=len(betas), interval=35, blit=False, repeat=True
)

plt.tight_layout()
plt.show()