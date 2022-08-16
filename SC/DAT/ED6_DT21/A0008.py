import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0008_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0008   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'T0030.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0005,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT29/CH12400._CH', 'ED6_DT29/CH12400P._CP'),
        ('ED6_DT29/CH12401._CH', 'ED6_DT29/CH12401P._CP'),
        ('ED6_DT29/CH12402._CH', 'ED6_DT29/CH12402P._CP'),
        ('ED6_DT29/CH12403._CH', 'ED6_DT29/CH12403P._CP'),
        ('ED6_DT29/CH12404._CH', 'ED6_DT29/CH12404P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12410._CH', 'ED6_DT29/CH12410P._CP'),
        ('ED6_DT29/CH12411._CH', 'ED6_DT29/CH12411P._CP'),
        ('ED6_DT29/CH12412._CH', 'ED6_DT29/CH12412P._CP'),
        ('ED6_DT29/CH12413._CH', 'ED6_DT29/CH12413P._CP'),
        ('ED6_DT29/CH12414._CH', 'ED6_DT29/CH12414P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12420._CH', 'ED6_DT29/CH12420P._CP'),
        ('ED6_DT29/CH12421._CH', 'ED6_DT29/CH12421P._CP'),
        ('ED6_DT29/CH12422._CH', 'ED6_DT29/CH12422P._CP'),
        ('ED6_DT29/CH12423._CH', 'ED6_DT29/CH12423P._CP'),
        ('ED6_DT29/CH12424._CH', 'ED6_DT29/CH12424P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12430._CH', 'ED6_DT29/CH12430P._CP'),
        ('ED6_DT29/CH12431._CH', 'ED6_DT29/CH12431P._CP'),
        ('ED6_DT29/CH12432._CH', 'ED6_DT29/CH12432P._CP'),
        ('ED6_DT29/CH12433._CH', 'ED6_DT29/CH12433P._CP'),
        ('ED6_DT29/CH12434._CH', 'ED6_DT29/CH12434P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12440._CH', 'ED6_DT29/CH12440P._CP'),
        ('ED6_DT29/CH12441._CH', 'ED6_DT29/CH12441P._CP'),
        ('ED6_DT29/CH12442._CH', 'ED6_DT29/CH12442P._CP'),
        ('ED6_DT29/CH12443._CH', 'ED6_DT29/CH12443P._CP'),
        ('ED6_DT29/CH12444._CH', 'ED6_DT29/CH12444P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
    ]

# id: 0x10001 offset: 0x23A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '12400待机',
            x                   = 4000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12401移动',
            x                   = 4000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12402攻击',
            x                   = 4000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12403伤害',
            x                   = 4000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12404倒下',
            x                   = 4000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12410待机',
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12411移动',
            x                   = 8000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12412攻击',
            x                   = 8000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12413伤害',
            x                   = 8000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12414倒下',
            x                   = 8000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12420待机',
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12421移动',
            x                   = 12000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12422攻击',
            x                   = 12000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12423伤害',
            x                   = 12000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12424倒下',
            x                   = 12000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12430待机',
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12431移动',
            x                   = 16000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12432攻击',
            x                   = 16000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12433伤害',
            x                   = 16000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12434倒下',
            x                   = 16000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12440待机',
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12441移动',
            x                   = 20000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12442攻击',
            x                   = 20000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12443伤害',
            x                   = 20000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '12444倒下',
            x                   = 20000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0x55A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x55A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x55A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x55A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x55B
@scena.Code('func_01_55B')
def func_01_55B():
    Return()

# id: 0x0002 offset: 0x55C
@scena.Code('func_02_55C')
def func_02_55C():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x6),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_589'),
        (0x00000001, 'loc_591'),
        (0x00000002, 'loc_599'),
        (0x00000003, 'loc_5A1'),
        (0x00000004, 'loc_5A9'),
        (0x00000005, 'loc_5B1'),
        (-1, 'loc_5B9'),
    )

    def _loc_589(): pass

    label('loc_589')

    Sleep(100)

    Jump('loc_5B9')

    def _loc_591(): pass

    label('loc_591')

    Sleep(100)

    Jump('loc_5B9')

    def _loc_599(): pass

    label('loc_599')

    Sleep(200)

    Jump('loc_5B9')

    def _loc_5A1(): pass

    label('loc_5A1')

    Sleep(300)

    Jump('loc_5B9')

    def _loc_5A9(): pass

    label('loc_5A9')

    Sleep(400)

    Jump('loc_5B9')

    def _loc_5B1(): pass

    label('loc_5B1')

    Sleep(500)

    Jump('loc_5B9')

    def _loc_5B9(): pass

    label('loc_5B9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5CE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_5B9')

    def _loc_5CE(): pass

    label('loc_5CE')

    Return()

# id: 0x0003 offset: 0x5CF
@scena.Code('func_03_5CF')
def func_03_5CF():
    Return()

# id: 0x0004 offset: 0x5D0
@scena.Code('func_04_5D0')
def func_04_5D0():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗷—',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
