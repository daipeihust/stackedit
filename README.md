<html lang="en">
<head>
  <meta charset="utf-8">
     <script src="https://unpkg.com/mermaid@8.1.0/dist/mermaid.js"></script>
  <script>mermaid.initialize({startOnLoad:true});</script>
</head>
<body>
  <div class="mermaid">
  graph TD
    A((start)) -->|matchData| B(find match)
    B -->|matchTicket| C(record ticket)
    B -->|failed| End
    C --> D(wait opponent)
    C --> |failed| End
    D --> E(submit payment)
    D --> |timeout| End
    E --> F{isCentralized?}
    F -->|yes| G(send payment)
    F -->|no| H(send condition payment)
    G --> I{success?}
    H --> I
    I -->|yes| J(waiting opponent pay)
    I -->|no| End((end))
    J --> K(opponent payed)
    K --> L(join match)
    L --> M(check game status)
    M --> N{status?}
    N -->|started| O("start game (open centralized game page)")
    N -->|invalid, cancelled, draw, winOrLose| P("end game (open result page)")
    P --> Q{get game result?}
    Q --> Q
    O -->|win, lose, draw, surrender| P
    Q --> R(display result)
    R --> End
  </div>
</body>
</html>

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQyNTA1Mjg4NSw3Mzg5NzI4NywxODk5Mj
g3MzA2LC04NzcwMTY1MjQsNTEwMjkxMzAyLC04NTU2NzE1NDcs
MzIyMTkyNDg3LC0yMDg4NzQ2NjEyLC0xNjAyNDQxMDMsOTM3Mj
g5NywtMTM2NzgzMjMxNSw3NzczMjU2MzEsNjM3MDI2OTY3LDE4
MzU0MTYyMzMsLTg3MTYxOTAzNl19
-->