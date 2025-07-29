def rgb_to_hex(r,g,b):
    return f"#{((r<<16) + (g<<8) + b):06X}"

print(rgb_to_hex(0,51,255))