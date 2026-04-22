# ⌨️ Typing Trainer

## INTRO

Typing Trainer è un'applicazione desktop sviluppata in Python che permette di allenare la memoria muscolare delle mani per migliorare l'utilizzo della tastiera.

È pensata per chiunque voglia migliorare la propria velocità e precisione nella scrittura, dagli studenti ai professionisti.

L'obiettivo è offrire un sistema di allenamento:

* leggero (senza frizioni inutili)
* interattivo
* efficace nel tempo

Il progetto nasce sia come strumento reale utilizzabile quotidianamente, sia come progetto portfolio per lo sviluppo di competenze software.

---

## COME È NATA L'IDEA

Il progetto nasce da un'esigenza personale: migliorare velocità e precisione nella scrittura, competenze fondamentali in ambito informatico.

Dopo aver testato diversi typing trainer già esistenti, è emersa una mancanza comune:

* poca libertà di personalizzazione
* esperienza poco soddisfacente
* struttura spesso rigida o limitata

Da qui la decisione di sviluppare una soluzione propria, con l'obiettivo di creare un sistema modulare, flessibile e progressivamente espandibile.

Attualmente il progetto è nelle fasi iniziali e si concentra su:

* sviluppo di diverse modalità di allenamento
* espansione e miglioramento dei dizionari

---

## COME È STRUTTURATA

L'applicazione è sviluppata in:

* **Python**
* **Tkinter** (interfaccia grafica)

La struttura del progetto segue un approccio modulare per mantenere il codice leggibile e scalabile.

### Architettura (semplificata)

```
run.py
app/
│
├── main.py                # entry point logico dell'app
├── views/                 # gestione interfacce (UI)
│   └── survival_view.py
│
├── services/              # logica applicativa
│
├── settings_manager.py    # gestione impostazioni (JSON)
├── translations.py        # gestione lingua UI
│
data/
├── *.txt                  # dizionari parole
├── user_settings.json     # configurazioni utente
```

### Principi adottati

* separazione tra logica e interfaccia
* modularità dei componenti
* dati esterni (configurazioni e dizionari)
* codice facilmente estendibile per nuove modalità

⚠️ Nota: la struttura è in fase di miglioramento e refactor per supportare meglio l’espansione futura.

---

## COME FUNZIONA

L'applicazione permette di allenarsi tramite diverse modalità di digitazione.

### Modalità attuali / pianificate

* Survival Mode
* Timed Mode
* Zen Mode
* Modalità a ondate
* Precision Mode
* TTS Mode (dettato)
* Altre modalità in sviluppo

### Funzionalità principali

* selezione modalità di allenamento
* selezione lingua dell’interfaccia
* selezione dizionario (file `.txt`)
* possibilità di usare:

  * testo personalizzato
  * importazione file `.txt`
* limite errori con sistema di game over
* generazione automatica del test
* feedback visivo:

  * testo corretto (verde)
  * errori (rosso)
* tastiera virtuale (supporto visivo)

### Sistema di configurazione

* impostazioni salvate in file `.json`
* persistenza tra sessioni

---

## STATO DEL PROGETTO

🚧 In sviluppo attivo

Attualmente:

* base funzionante
* struttura modulare presente
* alcune parti in refactor

---

## ROADMAP

Prossimi sviluppi previsti:

* miglioramento architettura interna
* implementazione completa modalità:

  * timed
  * precision
  * ondate
  * dettato (TTS)
* espansione dizionari
* miglioramento UX/UI
* statistiche utente
* ottimizzazione performance

---

## PUNTO FORTE

Il progetto punta su:

* modularità
* semplicità d’uso
* alta personalizzazione
* crescita progressiva delle funzionalità

---

## NOTE FINALI

Typing Trainer è un progetto in evoluzione continua, pensato per crescere nel tempo sia come prodotto utilizzabile, sia come base di apprendimento nello sviluppo software.
