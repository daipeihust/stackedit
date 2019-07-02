# turn-based

## post

### request
```json
Optional(["matchType": Optional("quick-match"), "token": Optional("GT"), "gameType": Optional("solo"), "myAddress": Optional("cb9b58defc54151b9993bd0f23104c34a3fef44c"), "opponentAddress": Optional("a25e6d748da3839236fef432e8770aef7c1f3f8a"), "lastUpdated": Optional(1562080013), "opponentPaymentId": Optional(""), "historyId": Optional("2A056D39-AD1C-4518-8C35-A74CEC3AF20B"), "myScore": Optional(0), "appId": Optional("000009"), "opponentScore": Optional(0), "entryFee": Optional(1.0), "matchId": Optional("9e1420cd-0fb7-4aaf-8d45-4a28d362e3eb."), "myPaymentId": Optional(""), "prizeWinner": Optional("winner"), "myNakamaId": Optional("2aa3b5fb-6cf2-4dc2-9c16-8e00745faf1a"), "prize": Optional(2.0), "opponentNakamaId": Optional("b6c5bb5e-688b-4a84-9448-a9a650ef92cf"), "status": Optional("pending"), "initiated": Optional(1562080013), "chain": Optional("ropsten")])
```

### response

```json
Optional("{"success":true,"data":{"historyId":"2A056D39-AD1C-4518-8C35-A74CEC3AF20B","historyType":"match","matchId":"9e1420cd-0fb7-4aaf-8d45-4a28d362e3eb.","matchType":"quick-match","appID":"000009","gameType":"solo","prizeWinner":"winner","token":"GT","entryFee":1,"prize":2,"myAddress":"cb9b58defc54151b9993bd0f23104c34a3fef44c","myNakamaId":"2aa3b5fb-6cf2-4dc2-9c16-8e00745faf1a","opponentAddress":"a25e6d748da3839236fef432e8770aef7c1f3f8a","opponentNakamaId":"b6c5bb5e-688b-4a84-9448-a9a650ef92cf","status":"pending","chain":"ropsten","initiated":1562080013,"lastUpdated":1562080013}}")
```

## update

### request

```json
Optional(["historyId": Optional("2A056D39-AD1C-4518-8C35-A74CEC3AF20B"), "opponentScore": Optional(1), "myScore": Optional(0), "status": Optional("completed"), "lastUpdated": Optional(1562080063)])
```

### response

```json
Optional("{"data":{"historyId":"2A056D39-AD1C-4518-8C35-A74CEC3AF20B","historyType":"match","matchId":"9e1420cd-0fb7-4aaf-8d45-4a28d362e3eb.","matchType":"quick-match","appID":"000009","gameType":"solo","prizeWinner":"winner","token":"GT","entryFee":1,"prize":2,"myAddress":"cb9b58defc54151b9993bd0f23104c34a3fef44c","myNakamaId":"2aa3b5fb-6cf2-4dc2-9c16-8e00745faf1a","opponentAddress":"a25e6d748da3839236fef432e8770aef7c1f3f8a","opponentNakamaId":"b6c5bb5e-688b-4a84-9448-a9a650ef92cf","opponentScore":1,"status":"completed","chain":"ropsten","initiated":1562080013,"lastUpdated":1562080063},"success":true}")
```

# solo

## post

### request

```json
Optional(["myPaymentId": Optional(""), "opponentAddress": Optional("a25e6d748da3839236fef432e8770aef7c1f3f8a"), "entryFee": Optional(1.0), "prize": Optional(2.0), "gameType": Optional("solo"), "opponentPaymentId": Optional(""), "historyId": Optional("7256A1E0-D3D6-4EEB-AEDC-32DE1ACBAE77"), "matchId": Optional("99fc9c18-9109-4f33-b0b7-157d13ae1932."), "myNakamaId": Optional("2aa3b5fb-6cf2-4dc2-9c16-8e00745faf1a"), "opponentNakamaId": Optional("b6c5bb5e-688b-4a84-9448-a9a650ef92cf"), "initiated": Optional(1562080531), "prizeWinner": Optional("high-score-achiever"), "myAddress": Optional("cb9b58defc54151b9993bd0f23104c34a3fef44c"), "matchType": Optional("quick-match"), "lastUpdated": Optional(1562080531), "chain": Optional("ropsten"), "opponentScore": Optional(0), "token": Optional("GT"), "myScore": Optional(0), "appId": Optional("000064"), "status": Optional("pending")])
```

### response

```json
Optional("{"success":true,"data":{"historyId":"7256A1E0-D3D6-4EEB-AEDC-32DE1ACBAE77","historyType":"match","matchId":"99fc9c18-9109-4f33-b0b7-157d13ae1932.","matchType":"quick-match","appID":"000064","gameType":"solo","prizeWinner":"high-score-achiever","token":"GT","entryFee":1,"prize":2,"myAddress":"cb9b58defc54151b9993bd0f23104c34a3fef44c","myNakamaId":"2aa3b5fb-6cf2-4dc2-9c16-8e00745faf1a","opponentAddress":"a25e6d748da3839236fef432e8770aef7c1f3f8a","opponentNakamaId":"b6c5bb5e-688b-4a84-9448-a9a650ef92cf","status":"pending","chain":"ropsten","initiated":1562080531,"lastUpdated":1562080531}}")
```


## update

### request

```json
Optional(["historyId": Optional("7256A1E0-D3D6-4EEB-AEDC-32DE1ACBAE77"), "status": Optional("pending"), "myScore": Optional(0), "opponentScore": Optional(0), "lastUpdated": Optional(1562080531)])
```

### response

```json

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjI5Mzg5Njk5LC0xNjAyNDQxMDMsOTM3Mj
g5NywtMTM2NzgzMjMxNSw3NzczMjU2MzEsNjM3MDI2OTY3LDE4
MzU0MTYyMzMsLTg3MTYxOTAzNl19
-->