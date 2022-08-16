import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0010_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0010   ._SN')

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
        ('ED6_DT29/CH12500._CH', 'ED6_DT29/CH12500P._CP'),
        ('ED6_DT29/CH12501._CH', 'ED6_DT29/CH12501P._CP'),
        ('ED6_DT29/CH12502._CH', 'ED6_DT29/CH12502P._CP'),
        ('ED6_DT29/CH12503._CH', 'ED6_DT29/CH12503P._CP'),
        ('ED6_DT29/CH12504._CH', 'ED6_DT29/CH12504P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12510._CH', 'ED6_DT29/CH12510P._CP'),
        ('ED6_DT29/CH12511._CH', 'ED6_DT29/CH12511P._CP'),
        ('ED6_DT29/CH12512._CH', 'ED6_DT29/CH12512P._CP'),
        ('ED6_DT29/CH12513._CH', 'ED6_DT29/CH12513P._CP'),
        ('ED6_DT29/CH12514._CH', 'ED6_DT29/CH12514P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12520._CH', 'ED6_DT29/CH12520P._CP'),
        ('ED6_DT29/CH12521._CH', 'ED6_DT29/CH12521P._CP'),
        ('ED6_DT29/CH12522._CH', 'ED6_DT29/CH12522P._CP'),
        ('ED6_DT29/CH12523._CH', 'ED6_DT29/CH12523P._CP'),
        ('ED6_DT29/CH12524._CH', 'ED6_DT29/CH12524P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
    ]

# id: 0x10001 offset: 0x19A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '12500待机',
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
            name                = '12501移动',
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
            name                = '12502攻击',
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
            name                = '12503伤害',
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
            name                = '12504倒下',
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
            name                = '12510待机',
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
            name                = '12511移动',
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
            name                = '12512攻击',
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
            name                = '12513伤害',
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
            name                = '12514倒下',
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
            name                = '12520待机',
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
            name                = '12521移动',
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
            name                = '12522攻击',
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
            name                = '12523伤害',
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
            name                = '12524倒下',
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
    )

# id: 0x10002 offset: 0x37A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x37A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x37A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x37A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x37B
@scena.Code('func_01_37B')
def func_01_37B():
    Return()

# id: 0x0002 offset: 0x37C
@scena.Code('func_02_37C')
def func_02_37C():
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
        (0x00000000, 'loc_3A9'),
        (0x00000001, 'loc_3B1'),
        (0x00000002, 'loc_3B9'),
        (0x00000003, 'loc_3C1'),
        (0x00000004, 'loc_3C9'),
        (0x00000005, 'loc_3D1'),
        (-1, 'loc_3D9'),
    )

    def _loc_3A9(): pass

    label('loc_3A9')

    Sleep(100)

    Jump('loc_3D9')

    def _loc_3B1(): pass

    label('loc_3B1')

    Sleep(100)

    Jump('loc_3D9')

    def _loc_3B9(): pass

    label('loc_3B9')

    Sleep(200)

    Jump('loc_3D9')

    def _loc_3C1(): pass

    label('loc_3C1')

    Sleep(300)

    Jump('loc_3D9')

    def _loc_3C9(): pass

    label('loc_3C9')

    Sleep(400)

    Jump('loc_3D9')

    def _loc_3D1(): pass

    label('loc_3D1')

    Sleep(500)

    Jump('loc_3D9')

    def _loc_3D9(): pass

    label('loc_3D9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3EE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3D9')

    def _loc_3EE(): pass

    label('loc_3EE')

    Return()

# id: 0x0003 offset: 0x3EF
@scena.Code('func_03_3EF')
def func_03_3EF():
    Return()

# id: 0x0004 offset: 0x3F0
@scena.Code('func_04_3F0')
def func_04_3F0():
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
