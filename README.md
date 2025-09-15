# Life Decision Simulator

A **Team Fortress 2 themed choose-your-own-adventure game** based on the official short film _Meet the Spy_ and events that frequently occur on the map _cft\_2fort_ during a typical game.  
Players make decisions that lead to branching paths in the story that lead to victory or death

## Requirements

Python 3.8 or Higher

## Installation  

1. Clone the Repository 
  
git clone https://github.com/WTCSC/life-decision-simulator-ZoltanHari.git

2. Open the Cloned Repository 
  
cd life-decision-simulator-ZoltanHari

## Usage

1. Run **`decision_tree.py`** With python3 decision_tree.py

2. Read the Text Until You Get to a Decision 

3. Type Either 1 or 2 to Choose an Option

4. Keep Going Until You Either Win or Die

### Examples

![](https://s8.ezgif.com/tmp/ezgif-85881bebcb41dc.gif)

## Path Modification 

To Edit Existing Paths or Add New Ones Open the **`messages.txt`** File and Use the Following Syntax
```python
%msg(message number)%
(your message)
1.(option 1) %(number of message that path leads to)%
2.(option 2) %(number of message that path leads to)%
%msg(message number)%
```
### Example 
```python
%msg0%
(You see a suspicious doorway)
What Will You Do?
1. Enter %1%
2. Walk Away %2%
%msg0%
```

## Flow Chart

![](https://i.imgur.com/W5TrFMK.png)
