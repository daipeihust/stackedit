<html lang="en">

<head>
  <meta charset="utf-8">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.0.0/mermaid.min.js"></script>
  <script>mermaid.initialize({ startOnLoad: true });</script>
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
<script>
  var config = {
    startOnLoad: true,
    theme: 'forest',
    flowchart: {
      useMaxWidth: false,
      htmlLabels: true
    }
  };
  mermaid.initialize(config);
  window.mermaid.init(undefined, document.querySelectorAll('.language-mermaid'));
</script>

</html>
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDg2MDkyNTEzLDE0MjUwNTI4ODUsNzM4OT
cyODcsMTg5OTI4NzMwNiwtODc3MDE2NTI0LDUxMDI5MTMwMiwt
ODU1NjcxNTQ3LDMyMjE5MjQ4NywtMjA4ODc0NjYxMiwtMTYwMj
Q0MTAzLDkzNzI4OTcsLTEzNjc4MzIzMTUsNzc3MzI1NjMxLDYz
NzAyNjk2NywxODM1NDE2MjMzLC04NzE2MTkwMzZdfQ==
-->