# Stock Price Prediction Error Tool (Insight Coding Challenge)

## Tool used to calculate stock prediction error written in Python 3
* Compares stocks prices from actual data to predicted data and calculates average error.
* Calculates average error over a specific sliding time window.
* Inputs data from actual.txt, predicted.txt, and window.txt and outputs results to comparison.txt

# Usage

Place input files into corresponding folder.
```
Place actual stock prices (actual.txt), predicted stock prices (predicted.txt), and specified window number (window.txt) into input folder. Note: For window number, please DO NOT use decimals to indicate a whole-number (i.e. 4.0 instead of 4).
```
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

Execute run.sh in command window using ./run.sh
```
Tool will start running. If there are no errors, "Prediction Validation is Complete." will be outputted.  Output file (comparison.txt) will be written to output folder. 
```

#### comparison.txt sample:

```
1|4|0.00
2|5|0.00
3|6|0.00
4|7|0.00
5|8|0.00
6|9|0.00
7|10|0.00
8|11|0.00
9|12|0.00
10|13|0.00
```

# Additional Notes

Tool was tested using coding challenge's testing suites.  Results are within +- .01 error range presumably due to rounding issues.  Only minor dependancies were utilized to display fundamental coding logic.  Additional error-checks were implemented as well.  Code assumes user will also use same input/output file names and execute code using run.sh.  Thank you for your time and consideration.
