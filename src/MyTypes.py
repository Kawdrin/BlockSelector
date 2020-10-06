from typing import TypeVar, NewType, List
import pygame

Player = TypeVar('Player')
Sprite = TypeVar('Sprite')
Speed = TypeVar('Speed')
Entity = TypeVar('Entity')
Image = TypeVar('Entity')
Group = TypeVar('Group')
Tile = TypeVar('Tile')
Rect = TypeVar('Rect')
Level = TypeVar('Level')
Clock = NewType('Clock', int)
NewGame = TypeVar('NewGame')
RunGame = TypeVar('RunGame')
FileSpriteSheet = TypeVar('FileSpriteSheet')
TileLevel = TypeVar('TileLevel')
EntityLevel = TypeVar('EntityLevel')
Mouse = TypeVar('Mouse')
Estate = TypeVar('Estate')