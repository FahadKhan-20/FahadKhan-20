"""Builds assets/animated-pfp.svg from your GitHub avatar (rotating gradient rings + pulse glow)."""
import base64
import os
import urllib.request

USER = "FahadKhan-20"
URL = f"https://github.com/{USER}.png?size=300"

req = urllib.request.Request(URL, headers={"User-Agent": "pfp-generator"})
with urllib.request.urlopen(req) as r:
    data = r.read()
    ctype = r.headers.get("Content-Type", "image/png").split(";")[0]
b64 = base64.b64encode(data).decode()

svg = f"""<svg width="220" height="220" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#36BCF7">
        <animate attributeName="stop-color" values="#36BCF7;#A855F7;#F43F5E;#36BCF7" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#A855F7">
        <animate attributeName="stop-color" values="#A855F7;#F43F5E;#36BCF7;#A855F7" dur="6s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <clipPath id="c"><circle cx="110" cy="110" r="85"/></clipPath>
  </defs>

  <!-- pulsing glow -->
  <circle cx="110" cy="110" r="90" fill="none" stroke="url(#g1)" stroke-width="3" opacity="0.6">
    <animate attributeName="r" values="90;104;90" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0;0.6" dur="3s" repeatCount="indefinite"/>
  </circle>

  <!-- outer rotating ring -->
  <circle cx="110" cy="110" r="100" fill="none" stroke="url(#g1)" stroke-width="5" stroke-linecap="round" stroke-dasharray="60 30">
    <animateTransform attributeName="transform" type="rotate" from="0 110 110" to="360 110 110" dur="8s" repeatCount="indefinite"/>
  </circle>

  <!-- inner counter-rotating ring -->
  <circle cx="110" cy="110" r="92" fill="none" stroke="url(#g1)" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="15 12">
    <animateTransform attributeName="transform" type="rotate" from="360 110 110" to="0 110 110" dur="12s" repeatCount="indefinite"/>
  </circle>

  <!-- avatar -->
  <image x="25" y="25" width="170" height="170" clip-path="url(#c)" preserveAspectRatio="xMidYMid slice"
         xlink:href="data:{ctype};base64,{b64}"/>
</svg>
"""

os.makedirs("assets", exist_ok=True)
with open("assets/animated-pfp.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("Generated assets/animated-pfp.svg")
