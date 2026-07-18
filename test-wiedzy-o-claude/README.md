# Profil uczestnika + Test wiedzy o Claude

Samodzielny (jednoplikowy) test w HTML, który łączy **profil uczestnika**
z **testem wiedzy o Claude i Anthropic** — 15 pytań jednokrotnego wyboru
z natychmiastowymi wyjaśnieniami.

## Uruchomienie

Otwórz `index.html` w dowolnej przeglądarce — nie wymaga instalacji ani serwera
(cały kod HTML/CSS/JS jest w jednym pliku). Wysyłka wyniku wymaga dostępu do
internetu.

## Profil uczestnika

Przed rozpoczęciem testu uczestnik uzupełnia profil:

- **Imię i nazwisko** — wymagane (bez niego nie można zakończyć testu)
- **Adres e-mail** — opcjonalny
- **Organizacja / firma** — opcjonalna
- **Rola** — lista wyboru (uczeń/student, programista, badacz, menedżer, inna)
- **Znajomość Claude** — lista wyboru (początkująca / średnia / zaawansowana)

Dane profilu trafiają do podsumowania oraz do wiadomości wysyłanej przez Web3Forms.

## Zakres testu

15 pytań w czterech kategoriach:

- **Podstawy** — Anthropic, założyciele, Constitutional AI, pochodzenie nazwy
- **Modele** — poziomy Haiku / Sonnet / Opus i ich charakterystyka
- **Funkcje** — MCP, Claude Code, Artifacts, tool use, prompt caching
- **Pojęcia AI** — okno kontekstu, token, halucynacja

## Konfiguracja wysyłki wyniku (Web3Forms)

Wynik (profil + punktacja + rozbicie na kategorie) można wysłać na e-mail przez
usługę [Web3Forms](https://web3forms.com), bez własnego backendu.

1. Wygeneruj **Access Key** na https://web3forms.com.
2. W `index.html`, na początku sekcji `<script>`, wstaw klucz w linii:

   ```js
   const WEB3FORMS_ACCESS_KEY = "TWOJ_KLUCZ_TUTAJ";
   ```

Klucz Web3Forms jest publiczny i z założenia umieszcza się go w kodzie front-endu.

## Uwaga o aktualności

Świat modeli AI zmienia się szybko. Test celowo skupia się na trwałych,
ogólnych faktach o Claude i Anthropic; szczegóły dotyczące konkretnych wersji
modeli i cen najlepiej sprawdzać w oficjalnej dokumentacji Anthropic.

Test ma charakter edukacyjny.
