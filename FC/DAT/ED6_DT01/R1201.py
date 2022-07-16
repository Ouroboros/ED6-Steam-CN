import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R1201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1201   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '古罗尼山道方向'),
    TXT(0x02, '拉文努山道方向'),
    TXT(0x03, '柏斯方向'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1201.x'
    header.mapIndex       = 61
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x770
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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
            word_3A         = 61,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10320._CH', 'ED6_DT09/CH10320P._CP'),
        ('ED6_DT09/CH10321._CH', 'ED6_DT09/CH10321P._CP'),
        ('ED6_DT09/CH10350._CH', 'ED6_DT09/CH10350P._CP'),
        ('ED6_DT09/CH10351._CH', 'ED6_DT09/CH10351P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10311._CH', 'ED6_DT09/CH10311P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10870._CH', 'ED6_DT09/CH10870P._CP'),
        ('ED6_DT09/CH10871._CH', 'ED6_DT09/CH10871P._CP'),
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -348670,
            z                   = 150,
            y                   = 8790,
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
        ScenaNpcData(
            x                   = -251150,
            z                   = 0,
            y                   = 36410,
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
        ScenaNpcData(
            x                   = -206940,
            z                   = 0,
            y                   = -15170,
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

# id: 0x10003 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -245780,
            z           = 10,
            y           = -13290,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -283410,
            z           = 510,
            y           = 3500,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -297320,
            z           = -10,
            y           = -50,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -321660,
            z           = 0,
            y           = 7860,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00FA,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1CA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -244460,
            y           = -1000,
            z           = 18100,
            range       = -258140,
            dword_10    = 0x000007D0,
            dword_14    = 0x00005BEA,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
    )

# id: 0x10005 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -254930,
            triggerZ            = 0,
            triggerY            = 140,
            triggerRange        = 1500,
            actorX              = -254930,
            actorZ              = 1300,
            actorY              = 140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -261790,
            triggerZ            = 0,
            triggerY            = -2900,
            triggerRange        = 1500,
            actorX              = -261790,
            actorZ              = 1500,
            actorY              = -2900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x232
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x233
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -400000, -127000, 196634)

    Return()

# id: 0x0002 offset: 0x246
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6AA',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_347',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0103, 0x0101, 0)

    ChrTalk(
        0x0103,
        (
            '#0030151249V#020F艾丝蒂尔，走错路了。\n',
            '这边是拉文努山道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151250V古罗尼连峰\n',
            '要继续往西走才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151251V要去拉文努村的话，\n',
            '等把委托人平安送到目的地后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151252V#000F好～知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DC')

    def _loc_347(): pass

    label('loc_347')

    ChrTalk(
        0x0103,
        (
            '#0030151253V#020F走错路了。\n',
            '这边是拉文努山道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151250V古罗尼连峰\n',
            '要继续往西走才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151251V要去拉文努村的话，\n',
            '等把委托人平安送到目的地后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DC(): pass

    label('loc_3DC')

    Jump('loc_68F')

    def _loc_3DF(): pass

    label('loc_3DF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0103, 0x0102, 0)

    ChrTalk(
        0x0103,
        (
            '#0030151256V#020F约修亚，走错路了。\n',
            '这边是拉文努山道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151250V古罗尼连峰\n',
            '要继续往西走才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151258V要去拉文努村的话，\n',
            '等把委托人平安送到目的地后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151259V#010F好，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_557')

    def _loc_4C2(): pass

    label('loc_4C2')

    ChrTalk(
        0x0103,
        (
            '#0030151253V#020F走错路了。\n',
            '这边是拉文努山道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151250V古罗尼连峰\n',
            '要继续往西走才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151262V要去拉文努村的话，\n',
            '等把委托人平安送到目的地后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_557(): pass

    label('loc_557')

    Jump('loc_68F')

    def _loc_55A(): pass

    label('loc_55A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_68F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_605',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0103,
        (
            '#0030151263V#023F啊……\n',
            '这边是拉文努山道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151264V古罗尼连峰\n',
            '要继续往西走才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151262V要去拉文努村的话，\n',
            '等把委托人平安送到目的地后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68F')

    def _loc_605(): pass

    label('loc_605')

    ChrTalk(
        0x0103,
        (
            '#0030151266V#020F这边是拉文努山道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151264V古罗尼连峰\n',
            '要继续往西走才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151262V要去拉文努村的话，\n',
            '等把委托人平安送到目的地后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_68F(): pass

    label('loc_68F')

    ChrMoveToRelative(0x0000, 0, 0, -2000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_6AA(): pass

    label('loc_6AA')

    Return()

# id: 0x0003 offset: 0x6AB
@scena.Code('func_03_6AB')
def func_03_6AB():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　拉文努村　　１４７塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x6FA
@scena.Code('func_04_6FA')
def func_04_6FA():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　柏斯市　　　１４０塞尔矩\n',
            '西　古罗尼山顶　３０１塞尔矩',
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
