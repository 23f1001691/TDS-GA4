# pip install tiktoken

import tiktoken
encoding = tiktoken.encoding_for_model("gpt-4o-mini")
msg = "List only the valid English words from these: zuganoj, 3, wu2Mf, 5j7l, 0SE, JPqgsuuZJO, 7kgX4Ti09, v8S, Q, o, zSLv, yM, 5Os9acNo, kVeCrNiMiS, ftZRr, 7, B1x, lA7, uG6R5, H, 8KPbNg1R, FOk2svFax, gcF, lv, Wr7, FVRg, 0OCVp6Yt, B8STshK, Epd6v, qIsLcr, s797s6iv, htiap7NH3, epn, TqaFLE82h, 8kdo77ht, MPq, WNa7, XRFg9oPnaO, A, AEif, Q, R, R6HLU, k, oz79K, TCUSqzC, yie, y2vPaW, YFu1DeZ2Rg, Fb3, 8R6O6, ltY1, mE7D0, sztMpf3xXq, JEGT, y3zZDFwjUo, c, 6, APUzszLJ, cRd4zzVD"
tokens = encoding.encode(msg)
print(len(tokens)+7)