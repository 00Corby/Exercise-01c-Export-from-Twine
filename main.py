#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "7DB00939-184B-44C2-A2C5-B6FCDAEAE597",
  "name": "Zork",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1630611443057,
  "passages": [
    {
      "name": "West of House",
      "tags": "",
      "id": "1",
      "text": "This is an open field west of a white house, with a boarded front door.\n\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[WEST->Forest]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
          "original": "[[NORTH->North of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of House",
          "original": "[[SOUTH->South of House]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Forest",
          "original": "[[WEST->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is an open field west of a white house, with a boarded front door."
    },
    {
      "name": "North of House",
      "tags": "",
      "id": "2",
      "text": "You are facing the north side of a white house. There is no door here, and all the windows are barred.\n\nWEST->[[West of House]]\nEAST->[[East of House]]\nNORTH->[[Forest]]",
      "links": [
        {
          "linkText": "West of House",
          "passageName": "West of House",
          "original": "[[West of House]]"
        },
        {
          "linkText": "East of House",
          "passageName": "East of House",
          "original": "[[East of House]]"
        },
        {
          "linkText": "Forest",
          "passageName": "Forest",
          "original": "[[Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the north side of a white house. There is no door here, and all the windows are barred.\n\nWEST->\nEAST->\nNORTH->"
    },
    {
      "name": "South of House",
      "tags": "",
      "id": "3",
      "text": "You are facing the south side of a white house. There is no door here, and all the windows are barred.\n\nWEST->[[West of House]]\nEAST->[[East of House]]\nSOUTH->[[Forest]]",
      "links": [
        {
          "linkText": "West of House",
          "passageName": "West of House",
          "original": "[[West of House]]"
        },
        {
          "linkText": "East of House",
          "passageName": "East of House",
          "original": "[[East of House]]"
        },
        {
          "linkText": "Forest",
          "passageName": "Forest",
          "original": "[[Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the south side of a white house. There is no door here, and all the windows are barred.\n\nWEST->\nEAST->\nSOUTH->"
    },
    {
      "name": "Forest",
      "tags": "",
      "id": "4",
      "text": "This is a forest, with trees in all directions around you.\n\nNORTH->[[Sunlit Forest]]\nEAST->[[Forest]]\nSOUTH->[[Forest]]\nWEST->[[Forest]]",
      "links": [
        {
          "linkText": "Sunlit Forest",
          "passageName": "Sunlit Forest",
          "original": "[[Sunlit Forest]]"
        },
        {
          "linkText": "Forest",
          "passageName": "Forest",
          "original": "[[Forest]]"
        },
        {
          "linkText": "Forest",
          "passageName": "Forest",
          "original": "[[Forest]]"
        },
        {
          "linkText": "Forest",
          "passageName": "Forest",
          "original": "[[Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is a forest, with trees in all directions around you.\n\nNORTH->\nEAST->\nSOUTH->\nWEST->"
    },
    {
      "name": "East of House",
      "tags": "",
      "id": "5",
      "text": "You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is slightly ajar.\n\nNORTH->[[North of House]]\nSOUTH->[[South of House]]\nEAST->[[Sunlit Forest]]\nWEST->[[Kitchen]]\nENTER->[[Kitchen]]",
      "links": [
        {
          "linkText": "North of House",
          "passageName": "North of House",
          "original": "[[North of House]]"
        },
        {
          "linkText": "South of House",
          "passageName": "South of House",
          "original": "[[South of House]]"
        },
        {
          "linkText": "Sunlit Forest",
          "passageName": "Sunlit Forest",
          "original": "[[Sunlit Forest]]"
        },
        {
          "linkText": "Kitchen",
          "passageName": "Kitchen",
          "original": "[[Kitchen]]"
        },
        {
          "linkText": "Kitchen",
          "passageName": "Kitchen",
          "original": "[[Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is slightly ajar.\n\nNORTH->\nSOUTH->\nEAST->\nWEST->\nENTER->"
    },
    {
      "name": "Sunlit Forest",
      "tags": "",
      "id": "6",
      "text": "This is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here.\n\nNORTH->[[Forest]]\nSOUTH->[[Forest]]\nEAST->[[Forest]]\nWEST->[[East of House]]\nUP->[[Tree]]",
      "links": [
        {
          "linkText": "Forest",
          "passageName": "Forest",
          "original": "[[Forest]]"
        },
        {
          "linkText": "Forest",
          "passageName": "Forest",
          "original": "[[Forest]]"
        },
        {
          "linkText": "Forest",
          "passageName": "Forest",
          "original": "[[Forest]]"
        },
        {
          "linkText": "East of House",
          "passageName": "East of House",
          "original": "[[East of House]]"
        },
        {
          "linkText": "Tree",
          "passageName": "Tree",
          "original": "[[Tree]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here.\n\nNORTH->\nSOUTH->\nEAST->\nWEST->\nUP->"
    },
    {
      "name": "Kitchen",
      "tags": "",
      "id": "7",
      "text": "You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open.\n\nEAST->[[East of House]]",
      "links": [
        {
          "linkText": "East of House",
          "passageName": "East of House",
          "original": "[[East of House]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open.\n\nEAST->"
    },
    {
      "name": "Tree",
      "tags": "",
      "id": "8",
      "text": "You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest.\n\nDOWN->[[Sunlit Forest]]",
      "links": [
        {
          "linkText": "Sunlit Forest",
          "passageName": "Sunlit Forest",
          "original": "[[Sunlit Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest.\n\nDOWN->"
    }
  ]
}

if "name" in world and "passages" in world:
    print(world["name"])
    print()
    for passage in world["passages"]:
        print(passage["name"])
        print(passage["cleanText"])
        for link in passage["links"]:
            print(link["linkText"])
        print()