## Please place input files into this folder.
* Actual stock prices should be labeled as actual.txt in a pipe-delimited format
* Predicted stock prices should be labeled as predicted.txt in a pipe-delimited format
* Window specification file should be labeled as window.txt.

  _Note: For window number, please DO NOT use decimals to indicate a whole-number (i.e. Use 4 instead of 4.0)._ 

#### actual.txt sample:

```
1|ROOKVN|283.43
1|NJFTAL|293.10
1|NYZXXA|315.55
1|FRYYPL|302.20
1|GDKJPI|294.78
1|RRVMLC|292.52
1|JEDAXP|306.81
2|EDMMCA|22.94
2|AMDDPW|22.48
2|YZSGPL|27.72
```

#### predicted.txt sample:

```
1|FRYYPL|302.20
1|GDKJPI|294.78
1|RRVMLC|292.52
2|EDMMCA|22.94
2|AMDDPW|22.48
2|CCKENL|24.75
2|LWZQMJ|17.26
2|QMQNMQ|26.22
2|ZMGTBK|23.63
2|ALAHMX|24.14
```

#### window.txt sample:

```
4
```
