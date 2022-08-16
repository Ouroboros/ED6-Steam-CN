import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C2209_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2209   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2209.x'
    header.mapIndex       = 84
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/C2209._SN', 'ED6_DT01/C2209_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 84,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
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

# id: 0x10000 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
    ]

# id: 0x10001 offset: 0xF6
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '弗科特老人',
            x                   = 620,
            z                   = 550,
            y                   = -2470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛诺利亚间道方向',
            x                   = 1330,
            z                   = -430,
            y                   = -46450,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x156
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x156
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x156
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -960,
            triggerZ            = 25000,
            triggerY            = -770,
            triggerRange        = 800,
            actorX              = -960,
            actorZ              = 26500,
            actorY              = -770,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x17A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x40)"),
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_198',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)

    Jump('loc_1A2')

    def _loc_198(): pass

    label('loc_198')

    OP_1B(0x01, 0x00, 0x0005)
    OP_1B(0x02, 0x00, 0x0005)

    def _loc_1A2(): pass

    label('loc_1A2')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_1AE'),
        (-1, 'loc_227'),
    )

    def _loc_1AE(): pass

    label('loc_1AE')

    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_216',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 0, 0x4A0)),
            Expr.Return,
        ),
        'loc_213',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 1, 0x4A1)),
            Expr.Return,
        ),
        'loc_213',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 3, 0x4A3)),
            Expr.Return,
        ),
        'loc_213',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 4, 0x4A4)),
            Expr.Return,
        ),
        'loc_213',
    )

    OP_28(0x001C, 0x04, 0x10)
    MapSetFlags(0x00400000)

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20F',
    )

    Event(1, 0x0005)

    Jump('loc_213')

    def _loc_20F(): pass

    label('loc_20F')

    Event(1, 0x0007)

    def _loc_213(): pass

    label('loc_213')

    Jump('loc_224')

    def _loc_216(): pass

    label('loc_216')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_224',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(1, 0x0006)

    def _loc_224(): pass

    label('loc_224')

    Jump('loc_227')

    def _loc_227(): pass

    label('loc_227')

    Return()

# id: 0x0001 offset: 0x228
@scena.Code('func_01_228')
def func_01_228():
    OP_16(0x02, 4000, -128000, -140000, 196688)

    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_25A',
    )

    OP_72(0x0000, 0x0010)

    def _loc_25A(): pass

    label('loc_25A')

    OP_B0(0x0000, 0x78)
    OP_B0(0x0001, 0x78)
    OP_1C(0x00, 0x00, 0x0003)
    OP_1C(0x01, 0x00, 0x0004)
    PlaySE(453, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x272
@scena.Code('func_02_272')
def func_02_272():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_287',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_272')

    def _loc_287(): pass

    label('loc_287')

    Return()

# id: 0x0003 offset: 0x288
@scena.Code('func_03_288')
def func_03_288():
    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2AD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    Call(1, 0x0001)

    Jump('loc_2B3')

    def _loc_2AD(): pass

    label('loc_2AD')

    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    def _loc_2B3(): pass

    label('loc_2B3')

    Return()

# id: 0x0004 offset: 0x2B4
@scena.Code('func_04_2B4')
def func_04_2B4():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

# id: 0x0005 offset: 0x2BB
@scena.Code('func_05_2BB')
def func_05_2BB():
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_21()
    OP_1B(0x01, 0x00, 0xFFFF)
    OP_1B(0x02, 0x00, 0xFFFF)

    Return()

# id: 0x0006 offset: 0x2D6
@scena.Code('func_06_2D6')
def func_06_2D6():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　危险！　　　\n',
            '※工作人员以外禁止进入',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
