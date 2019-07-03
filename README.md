```mermaid
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
```

![]()
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU1MzQ4MzE1NSw1MTAyOTEzMDIsLTg1NT
Y3MTU0NywzMjIxOTI0ODcsLTIwODg3NDY2MTIsLTE2MDI0NDEw
Myw5MzcyODk3LC0xMzY3ODMyMzE1LDc3NzMyNTYzMSw2MzcwMj
Y5NjcsMTgzNTQxNjIzMywtODcxNjE5MDM2XX0=
-->