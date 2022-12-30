def center_win(window, w, h):
  x_pos = int(window.winfo_screenwidth()/2 - w/2)
  y_pos = int(window.winfo_screenheigth()/2 - w/2)
  window.geomety(f"{w}x{h}+{x_pos}+{y_pos}")