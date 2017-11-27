# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name_male}}-{{first_name_male}} {{last_name}}',
        '{{first_name_male}}-{{first_name_male}} {{last_name}}',
        '{{first_name_female}}-{{first_name_female}} {{last_name}}',
        '{{first_name_female}}-{{first_name_female}} {{last_name}}',
        '{{first_name}} {{last_name}}-{{last_name}}',
        '{{first_name}} {{last_name}}-{{last_name}}',
        '{{prefix}} {{first_name_male}} {{last_name}}',
    )

    # 100 most common male first names, alphabetically.
    # Source: http://www.ssb.no/a/navn/fornavn-menn-100.html
    first_names_male = (
        'Adrian',
        'Alexander',
        'Alf',
        'Anders',
        'Andreas',
        'Arild',
        'Arne',
        'Asbjørn',
        'Bjørn',
        'Christian',
        'Dag',
        'Daniel',
        'Egil',
        'Einar',
        'Eirik',
        'Eivind',
        'Emil',
        'Erik',
        'Erling',
        'Espen',
        'Finn',
        'Frank',
        'Fredrik',
        'Frode',
        'Geir',
        'Gunnar',
        'Hans',
        'Harald',
        'Helge',
        'Henrik',
        'Håkon',
        'Håvard',
        'Ivar',
        'Jan',
        'Jens',
        'Joakim',
        'Johannes',
        'Johan',
        'John',
        'Jonas',
        'Jon',
        'Jørgen',
        'Karl',
        'Kenneth',
        'Kim',
        'Kjell',
        'Kjetil',
        'Knut',
        'Kåre',
        'Kristian',
        'Kristoffer',
        'Lars',
        'Leif',
        'Magne',
        'Magnus',
        'Marius',
        'Markus',
        'Martin',
        'Mathias',
        'Morten',
        'Nils',
        'Odd',
        'Ola',
        'Olav',
        'Ole',
        'Per',
        'Petter',
        'Pål',
        'Roar',
        'Robert',
        'Roger',
        'Rolf',
        'Roy',
        'Rune',
        'Sander',
        'Sebastian',
        'Sigurd',
        'Simen',
        'Sindre',
        'Sondre',
        'Steinar',
        'Stein',
        'Stian',
        'Stig',
        'Svein',
        'Sverre',
        'Terje',
        'Thomas',
        'Thor',
        'Tobias',
        'Tommy',
        'Tom',
        'Torbjørn',
        'Tore',
        'Tor',
        'Trond',
        'Vegard',
        'Vidar',
        'Øystein',
        'Øyvind',
    )

    # 100 most common female first names, alphabetically.
    # Source: http://www.ssb.no/a/navn/fornavn-kvinner-100.html
    first_names_female = (
        'Andrea',
        'Anette',
        'Anita',
        'Anna',
        'Anne',
        'Ann',
        'Astrid',
        'Aud',
        'Bente',
        'Berit',
        'Bjørg',
        'Britt',
        'Camilla',
        'Cathrine',
        'Cecilie',
        'Elin',
        'Elisabeth',
        'Elise',
        'Eli',
        'Ellen',
        'Else',
        'Emilie',
        'Emma',
        'Eva',
        'Gerd',
        'Grete',
        'Grethe',
        'Gro',
        'Gunn',
        'Hanna',
        'Hanne',
        'Hege',
        'Heidi',
        'Helene',
        'Hilde',
        'Ida',
        'Ingeborg',
        'Inger',
        'Ingrid',
        'Irene',
        'Janne',
        'Jenny',
        'Jorunn',
        'Julie',
        'Karen',
        'Karin',
        'Kari',
        'Karoline',
        'Kirsten',
        'Kjersti',
        'Kristine',
        'Kristin',
        'Laila',
        'Lene',
        'Linda',
        'Line',
        'Linn',
        'Lise',
        'Liv',
        'Malin',
        'Maren',
        'Marianne',
        'Maria',
        'Marie',
        'Mari',
        'Marit',
        'Marte',
        'Martine',
        'May',
        'Mette',
        'Mona',
        'Monica',
        'Nina',
        'Nora',
        'Ragnhild',
        'Randi',
        'Reidun',
        'Rita',
        'Ruth',
        'Sara',
        'Sigrid',
        'Silje',
        'Siri',
        'Sissel',
        'Siv',
        'Sofie',
        'Solveig',
        'Stine',
        'Synnøve',
        'Thea',
        'Tone',
        'Tonje',
        'Torill',
        'Tove',
        'Trine',
        'Turid',
        'Unni',
        'Vilde',
        'Wenche',
        'Åse',
    )

    first_names = first_names_male + first_names_female

    # 100 most common last names, alphabetically.
    # Source: http://www.ssb.no/a/navn/alf/etter100.html
    last_names = (
        'Aasen',
        'Aas',
        'Abrahamsen',
        'Ahmed',
        'Ali',
        'Amundsen',
        'Andersen',
        'Andreassen',
        'Andresen',
        'Antonsen',
        'Arnesen',
        'Aune',
        'Bakken',
        'Bakke',
        'Berge',
        'Berg',
        'Berntsen',
        'Bøe',
        'Birkeland',
        'Brekke',
        'Christensen',
        'Dahl',
        'Danielsen',
        'ødegård',
        'Edvardsen',
        'Eide',
        'Eliassen',
        'Ellingsen',
        'Engen',
        'Eriksen',
        'Evensen',
        'Fredriksen',
        'Gulbrandsen',
        'Gundersen',
        'Hagen',
        'Halvorsen',
        'Hansen',
        'Hanssen',
        'Haugen',
        'Hauge',
        'Haugland',
        'Haug',
        'Helland',
        'Henriksen',
        'Holm',
        'Isaksen',
        'Iversen',
        'Jacobsen',
        'Jakobsen',
        'Jensen',
        'Jenssen',
        'Johannessen',
        'Johansen',
        'Johnsen',
        'Jørgensen',
        'Karlsen',
        'Knudsen',
        'Knutsen',
        'Kristensen',
        'Kristiansen',
        'Kristoffersen',
        'Larsen',
        'Lien',
        'Lie',
        'Lunde',
        'Lund',
        'Madsen',
        'Martinsen',
        'Mathisen',
        'Mikkelsen',
        'Moen',
        'Moe',
        'Myhre',
        'Myklebust',
        'Nguyen',
        'Nielsen',
        'Nilsen',
        'Næss',
        'Nygård',
        'Olsen',
        'Paulsen',
        'Pedersen',
        'Pettersen',
        'Rasmussen',
        'Rønning',
        'Ruud',
        'Sandvik',
        'Simonsen',
        'Sivertsen',
        'Solberg',
        'Solheim',
        'Sørensen',
        'Sæther',
        'Strand',
        'Strøm',
        'Svendsen',
        'Tangen',
        'Thomassen',
        'Thorsen',
        'Tveit',
        'Vik',
    )

    prefixes = (
        'Dr.', 'Prof.',
    )
