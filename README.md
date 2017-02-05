# misp-darwin

MISP darwin is a model to automatically translate in natural language technical or structured information from [MISP](https://github.com/MISP/MISP). This allows to convert information contained in MISP to make it readable by human and also actionable beyond standard automatisation aspects. misp-darwin main objectives are:

- Automatically translating MISP event into human readable reports
- Adding actions and information to support analysts, security engineers from the indicators shared by other organisations
- Supporting automatically the translation in various natural language or localized natural languages used in an organisation or in an specific community

This is a Work-in-Progress (WiP) and the format of the rules might still change significantly.

## The origin of the darwin name

After an intense chat session between MISP core team members, the model is basically supporting the selection of mapping from structured information to natural languages. So the project is a kind of natural selection and as [Charles Darwin](https://en.wikipedia.org/wiki/Charles_Darwin) popularised the term "natural selection", misp-darwin was a logical consequence.

# Requirements

- Python 3
- [PyMISP](https://github.com/MISP/PyMISP) installed
- and a [MISP](https://github.com/MISP/) instance

# License

This software and rules are licensed under [GNU Affero General Public License version 3](http://www.gnu.org/licenses/agpl-3.0.html).

Copyright (C) 2016-2017 Alexandre Dulaunoy
Copyright (C) 2016-2017 CIRCL - Computer Incident Response Center Luxembourg

