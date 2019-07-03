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

![]([https://mermaidjs.github.io/mermaid-live-editor/#/view/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKChzdGFydCkpIC0tPnxtYXRjaERhdGF8IEIoZmluZCBtYXRjaClcbiAgICBCIC0tPnxtYXRjaFRpY2tldHwgQyhyZWNvcmQgdGlja2V0KVxuICAgIEIgLS0-fGZhaWxlZHwgRW5kXG4gICAgQyAtLT4gRCh3YWl0IG9wcG9uZW50KVxuICAgIEMgLS0-IHxmYWlsZWR8IEVuZFxuICAgIEQgLS0-IEUoc3VibWl0IHBheW1lbnQpXG4gICAgRCAtLT4gfHRpbWVvdXR8IEVuZFxuICAgIEUgLS0-IEZ7aXNDZW50cmFsaXplZD99XG4gICAgRiAtLT58eWVzfCBHKHNlbmQgcGF5bWVudClcbiAgICBGIC0tPnxub3wgSChzZW5kIGNvbmRpdGlvbiBwYXltZW50KVxuICAgIEcgLS0-IEl7c3VjY2Vzcz99XG4gICAgSCAtLT4gSVxuICAgIEkgLS0-fHllc3wgSih3YWl0aW5nIG9wcG9uZW50IHBheSlcbiAgICBJIC0tPnxub3wgRW5kKChlbmQpKVxuICAgIEogLS0-IEsob3Bwb25lbnQgcGF5ZWQpXG4gICAgSyAtLT4gTChqb2luIG1hdGNoKVxuICAgIEwgLS0-IE0oY2hlY2sgZ2FtZSBzdGF0dXMpXG4gICAgTSAtLT4gTntzdGF0dXM_fVxuICAgIE4gLS0-fHN0YXJ0ZWR8IE8oXCJzdGFydCBnYW1lIChvcGVuIGNlbnRyYWxpemVkIGdhbWUgcGFnZSlcIilcbiAgICBOIC0tPnxpbnZhbGlkLCBjYW5jZWxsZWQsIGRyYXcsIHdpbk9yTG9zZXwgUChcImVuZCBnYW1lIChvcGVuIHJlc3VsdCBwYWdlKVwiKVxuICAgIFAgLS0-IFF7Z2V0IGdhbWUgcmVzdWx0P31cbiAgICBRIC0tPiBRXG4gICAgTyAtLT58d2luLCBsb3NlLCBkcmF3LCBzdXJyZW5kZXJ8IFBcbiAgICBRIC0tPiBSKGRpc3BsYXkgcmVzdWx0KVxuICAgIFIgLS0-IEVuZCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In19](https://mermaidjs.github.io/mermaid-live-editor/#/view/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKChzdGFydCkpIC0tPnxtYXRjaERhdGF8IEIoZmluZCBtYXRjaClcbiAgICBCIC0tPnxtYXRjaFRpY2tldHwgQyhyZWNvcmQgdGlja2V0KVxuICAgIEIgLS0-fGZhaWxlZHwgRW5kXG4gICAgQyAtLT4gRCh3YWl0IG9wcG9uZW50KVxuICAgIEMgLS0-IHxmYWlsZWR8IEVuZFxuICAgIEQgLS0-IEUoc3VibWl0IHBheW1lbnQpXG4gICAgRCAtLT4gfHRpbWVvdXR8IEVuZFxuICAgIEUgLS0-IEZ7aXNDZW50cmFsaXplZD99XG4gICAgRiAtLT58eWVzfCBHKHNlbmQgcGF5bWVudClcbiAgICBGIC0tPnxub3wgSChzZW5kIGNvbmRpdGlvbiBwYXltZW50KVxuICAgIEcgLS0-IEl7c3VjY2Vzcz99XG4gICAgSCAtLT4gSVxuICAgIEkgLS0-fHllc3wgSih3YWl0aW5nIG9wcG9uZW50IHBheSlcbiAgICBJIC0tPnxub3wgRW5kKChlbmQpKVxuICAgIEogLS0-IEsob3Bwb25lbnQgcGF5ZWQpXG4gICAgSyAtLT4gTChqb2luIG1hdGNoKVxuICAgIEwgLS0-IE0oY2hlY2sgZ2FtZSBzdGF0dXMpXG4gICAgTSAtLT4gTntzdGF0dXM_fVxuICAgIE4gLS0-fHN0YXJ0ZWR8IE8oXCJzdGFydCBnYW1lIChvcGVuIGNlbnRyYWxpemVkIGdhbWUgcGFnZSlcIilcbiAgICBOIC0tPnxpbnZhbGlkLCBjYW5jZWxsZWQsIGRyYXcsIHdpbk9yTG9zZXwgUChcImVuZCBnYW1lIChvcGVuIHJlc3VsdCBwYWdlKVwiKVxuICAgIFAgLS0-IFF7Z2V0IGdhbWUgcmVzdWx0P31cbiAgICBRIC0tPiBRXG4gICAgTyAtLT58d2luLCBsb3NlLCBkcmF3LCBzdXJyZW5kZXJ8IFBcbiAgICBRIC0tPiBSKGRpc3BsYXkgcmVzdWx0KVxuICAgIFIgLS0-IEVuZCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In19)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg1NTY3MTU0NywzMjIxOTI0ODcsLTIwOD
g3NDY2MTIsLTE2MDI0NDEwMyw5MzcyODk3LC0xMzY3ODMyMzE1
LDc3NzMyNTYzMSw2MzcwMjY5NjcsMTgzNTQxNjIzMywtODcxNj
E5MDM2XX0=
-->