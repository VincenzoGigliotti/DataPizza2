## Descrizione 

Ho creato un interfaccia comune che ogni modulo deve implementare, questa interfaccia espone il metodo `run(input_data: dict) -> dict` e grazie a qursto tutti i moduli possono essere concatenati in una pipelinw.

Il file Yaml descrive la pipeline e la classe `Pipeline` legge questa configurazione, istanzia i moduli nella giusta sequenza, e passa l'output di un modulo come input al modulo successivo.

Ho usato Pydantic per garantire la validazione degli input e degli output

## Esempio di configurazione YAML funzionante
pipeline:
  - name: cleaner
    type: TextCleaner
  - name: generator
    type: TextGenerator
    params:
      max_length: 100