import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0703_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0703   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0703.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x34FE
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
            word_3A         = 0,
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -3400,
            y           = -2000,
            z           = 56200,
            range       = 3400,
            dword_10    = 0x00000BB8,
            dword_14    = 0x0000E09C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10005 offset: 0xC8
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 400,
            triggerY            = 88300,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 400,
            actorY              = 89000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 400,
            triggerY            = -88300,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 400,
            actorY              = -89000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 290,
            triggerZ            = 0,
            triggerY            = 45880,
            triggerRange        = 1000,
            actorX              = 230,
            actorZ              = 800,
            actorY              = 46150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 46950,
            triggerZ            = 0,
            triggerY            = -1000,
            triggerRange        = 1000,
            actorX              = 47050,
            actorZ              = 800,
            actorY              = -840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -46770,
            triggerZ            = 0,
            triggerY            = -750,
            triggerRange        = 1000,
            actorX              = -46750,
            actorZ              = 800,
            actorY              = -440,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -10,
            triggerZ            = 0,
            triggerY            = -47710,
            triggerRange        = 1000,
            actorX              = -60,
            actorZ              = 800,
            actorY              = -47460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1A0
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1C0'),
        (0x00000065, 'loc_1C7'),
        (0x00000066, 'loc_1CE'),
        (0x00000067, 'loc_1D5'),
        (0x00000068, 'loc_1DC'),
        (0x00000069, 'loc_1E3'),
        (-1, 'loc_1EA'),
    )

    def _loc_1C0(): pass

    label('loc_1C0')

    Event(0, 0x000C)

    Jump('loc_1EA')

    def _loc_1C7(): pass

    label('loc_1C7')

    Event(0, 0x000E)

    Jump('loc_1EA')

    def _loc_1CE(): pass

    label('loc_1CE')

    Event(0, 0x0010)

    Jump('loc_1EA')

    def _loc_1D5(): pass

    label('loc_1D5')

    Event(0, 0x0012)

    Jump('loc_1EA')

    def _loc_1DC(): pass

    label('loc_1DC')

    Event(0, 0x0014)

    Jump('loc_1EA')

    def _loc_1E3(): pass

    label('loc_1E3')

    Event(0, 0x0016)

    Jump('loc_1EA')

    def _loc_1EA(): pass

    label('loc_1EA')

    Return()

# id: 0x0001 offset: 0x1EB
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E1, 2, 0x1F0A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FD',
    )

    OP_6F(0x0020, 0)

    Jump('loc_204')

    def _loc_1FD(): pass

    label('loc_1FD')

    OP_6F(0x0020, 60)

    def _loc_204(): pass

    label('loc_204')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E1, 4, 0x1F0C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_216',
    )

    OP_6F(0x0021, 0)

    Jump('loc_21D')

    def _loc_216(): pass

    label('loc_216')

    OP_6F(0x0021, 60)

    def _loc_21D(): pass

    label('loc_21D')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')
    Call(0, 0x0004)
    OP_1B(0x00, 0x00, 0x000D)
    OP_1B(0x01, 0x00, 0x000F)
    OP_1B(0x02, 0x00, 0x0011)
    OP_1B(0x03, 0x00, 0x0013)
    OP_1B(0x04, 0x00, 0x0015)
    OP_1B(0x05, 0x00, 0x0017)

    Return()

# id: 0x0002 offset: 0x268
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x1A, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E1, 2, 0x1F0A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_345',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0020, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['翠耀石护符'], 1)"),
            Expr.Return,
        ),
        'loc_2DC',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['翠耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F0A)

    Jump('loc_342')

    def _loc_2DC(): pass

    label('loc_2DC')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['翠耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['翠耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0020, 60)
    OP_70(0x0020, 0x00000000)

    def _loc_342(): pass

    label('loc_342')

    Jump('loc_376')

    def _loc_345(): pass

    label('loc_345')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_376(): pass

    label('loc_376')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x384
@scena.Code('func_03_384')
def func_03_384():
    UnlockAchievement(0x02, 0x1B, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E1, 4, 0x1F0C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_461',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0021, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['八卦服'], 1)"),
            Expr.Return,
        ),
        'loc_3F8',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['八卦服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F0C)

    Jump('loc_45E')

    def _loc_3F8(): pass

    label('loc_3F8')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['八卦服']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['八卦服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0021, 60)
    OP_70(0x0021, 0x00000000)

    def _loc_45E(): pass

    label('loc_45E')

    Jump('loc_492')

    def _loc_461(): pass

    label('loc_461')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_492(): pass

    label('loc_492')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4A0
@scena.Code('func_04_4A0')
def func_04_4A0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 1, 0x1E31)),
            Expr.Return,
        ),
        'loc_521',
    )

    OP_72(0x0008, 0x0020)
    OP_72(0x0009, 0x0020)
    OP_72(0x000A, 0x0020)
    OP_72(0x000B, 0x0020)
    OP_72(0x000C, 0x0020)
    OP_72(0x000D, 0x0020)
    OP_72(0x000E, 0x0020)
    OP_72(0x0008, 0x0008)
    OP_72(0x0009, 0x0008)
    OP_72(0x000A, 0x0008)
    OP_72(0x000B, 0x0008)
    OP_72(0x000C, 0x0008)
    OP_72(0x000D, 0x0008)
    OP_72(0x000E, 0x0008)
    OP_6F(0x0008, 360)
    OP_6F(0x0009, 0)
    OP_6F(0x000A, 0)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    OP_6F(0x000E, 0)

    Jump('loc_598')

    def _loc_521(): pass

    label('loc_521')

    OP_72(0x0008, 0x0020)
    OP_72(0x0009, 0x0020)
    OP_72(0x000A, 0x0020)
    OP_72(0x000B, 0x0020)
    OP_72(0x000C, 0x0020)
    OP_72(0x000D, 0x0020)
    OP_72(0x000E, 0x0020)
    OP_72(0x0008, 0x0008)
    OP_72(0x0009, 0x0008)
    OP_72(0x000A, 0x0008)
    OP_72(0x000B, 0x0008)
    OP_72(0x000C, 0x0008)
    OP_72(0x000D, 0x0008)
    OP_72(0x000E, 0x0008)
    OP_6F(0x0008, 0)
    OP_6F(0x0009, 0)
    OP_6F(0x000A, 0)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    OP_6F(0x000E, 0)

    def _loc_598(): pass

    label('loc_598')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 7, 0x1E07)),
            Expr.Return,
        ),
        'loc_62A',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)

    Jump('loc_6B2')

    def _loc_62A(): pass

    label('loc_62A')

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)

    def _loc_6B2(): pass

    label('loc_6B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 0, 0x1E08)),
            Expr.Return,
        ),
        'loc_755',
    )

    OP_72(0x000F, 0x0020)
    OP_72(0x0010, 0x0020)
    OP_72(0x0011, 0x0020)
    OP_72(0x0012, 0x0020)
    OP_72(0x0013, 0x0020)
    OP_72(0x0014, 0x0020)
    OP_72(0x0015, 0x0020)
    OP_72(0x0016, 0x0020)
    OP_72(0x0017, 0x0020)
    OP_72(0x000F, 0x0008)
    OP_72(0x0010, 0x0008)
    OP_72(0x0011, 0x0008)
    OP_72(0x0012, 0x0008)
    OP_72(0x0013, 0x0008)
    OP_72(0x0014, 0x0008)
    OP_72(0x0015, 0x0008)
    OP_72(0x0016, 0x0008)
    OP_72(0x0017, 0x0008)
    OP_6F(0x000F, 0)
    OP_6F(0x0010, 0)
    OP_6F(0x0011, 0)
    OP_6F(0x0012, 0)
    OP_6F(0x0013, 0)
    OP_6F(0x0014, 360)
    OP_6F(0x0015, 0)
    OP_6F(0x0016, 0)
    OP_6F(0x0017, 0)

    Jump('loc_7EE')

    def _loc_755(): pass

    label('loc_755')

    OP_72(0x000F, 0x0020)
    OP_72(0x0010, 0x0020)
    OP_72(0x0011, 0x0020)
    OP_72(0x0012, 0x0020)
    OP_72(0x0013, 0x0020)
    OP_72(0x0014, 0x0020)
    OP_72(0x0015, 0x0020)
    OP_72(0x0016, 0x0020)
    OP_72(0x0017, 0x0020)
    OP_72(0x000F, 0x0008)
    OP_72(0x0010, 0x0008)
    OP_72(0x0011, 0x0008)
    OP_72(0x0012, 0x0008)
    OP_72(0x0013, 0x0008)
    OP_72(0x0014, 0x0008)
    OP_72(0x0015, 0x0008)
    OP_72(0x0016, 0x0008)
    OP_72(0x0017, 0x0008)
    OP_6F(0x000F, 0)
    OP_6F(0x0010, 0)
    OP_6F(0x0011, 0)
    OP_6F(0x0012, 0)
    OP_6F(0x0013, 0)
    OP_6F(0x0014, 0)
    OP_6F(0x0015, 0)
    OP_6F(0x0016, 0)
    OP_6F(0x0017, 0)

    def _loc_7EE(): pass

    label('loc_7EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 1, 0x1E09)),
            Expr.Return,
        ),
        'loc_880',
    )

    OP_72(0x0018, 0x0020)
    OP_72(0x0019, 0x0020)
    OP_72(0x001A, 0x0020)
    OP_72(0x001B, 0x0020)
    OP_72(0x001C, 0x0020)
    OP_72(0x001D, 0x0020)
    OP_72(0x001E, 0x0020)
    OP_72(0x001F, 0x0020)
    OP_72(0x0018, 0x0008)
    OP_72(0x0019, 0x0008)
    OP_72(0x001A, 0x0008)
    OP_72(0x001B, 0x0008)
    OP_72(0x001C, 0x0008)
    OP_72(0x001D, 0x0008)
    OP_72(0x001E, 0x0008)
    OP_72(0x001F, 0x0008)
    OP_6F(0x0018, 360)
    OP_6F(0x0019, 0)
    OP_6F(0x001A, 0)
    OP_6F(0x001B, 0)
    OP_6F(0x001C, 0)
    OP_6F(0x001D, 0)
    OP_6F(0x001E, 0)
    OP_6F(0x001F, 0)

    Jump('loc_908')

    def _loc_880(): pass

    label('loc_880')

    OP_72(0x0018, 0x0020)
    OP_72(0x0019, 0x0020)
    OP_72(0x001A, 0x0020)
    OP_72(0x001B, 0x0020)
    OP_72(0x001C, 0x0020)
    OP_72(0x001D, 0x0020)
    OP_72(0x001E, 0x0020)
    OP_72(0x001F, 0x0020)
    OP_72(0x0018, 0x0008)
    OP_72(0x0019, 0x0008)
    OP_72(0x001A, 0x0008)
    OP_72(0x001B, 0x0008)
    OP_72(0x001C, 0x0008)
    OP_72(0x001D, 0x0008)
    OP_72(0x001E, 0x0008)
    OP_72(0x001F, 0x0008)
    OP_6F(0x0018, 0)
    OP_6F(0x0019, 0)
    OP_6F(0x001A, 0)
    OP_6F(0x001B, 0)
    OP_6F(0x001C, 0)
    OP_6F(0x001D, 0)
    OP_6F(0x001E, 0)
    OP_6F(0x001F, 0)

    def _loc_908(): pass

    label('loc_908')

    Return()

# id: 0x0005 offset: 0x909
@scena.Code('func_05_909')
def func_05_909():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 6, 0x1E06)),
            Expr.Return,
        ),
        'loc_911',
    )

    Return()

    def _loc_911(): pass

    label('loc_911')

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_936',
    )

    Call(0, 0x000A)
    Call(0, 0x000B)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_936(): pass

    label('loc_936')

    Fade(500)
    OP_6D(-180, 400, 58250, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 1120, 400, 57110, 180)
    SetChrPos(0x0102, -190, 400, 57080, 180)
    SetChrPos(0x00F8, 1030, 400, 58470, 180)
    SetChrPos(0x00F9, -230, 400, 58410, 180)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010340736V#1004F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A00')
    def lambda_0A00():
        OP_6D(240, 400, 48840, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0A00)

    @scena.Lambda('lambda_0A18')
    def lambda_0A18():
        OP_67(0, 4080, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A18)

    @scena.Lambda('lambda_0A30')
    def lambda_0A30():
        OP_6B(3600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A30)

    @scena.Lambda('lambda_0A40')
    def lambda_0A40():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A40)

    @scena.Lambda('lambda_0A50')
    def lambda_0A50():
        OP_6E(290, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A50)

    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_0A65')
    def lambda_0A65():
        OP_8E(0x00FE, 1050, 200, 50180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A65)

    Sleep(300)

    @scena.Lambda('lambda_0A85')
    def lambda_0A85():
        OP_8E(0x00FE, -200, 200, 50110, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A85)

    Sleep(100)

    @scena.Lambda('lambda_0AA5')
    def lambda_0AA5():
        OP_8E(0x00FE, 990, 400, 51350, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0AA5)

    Sleep(300)

    @scena.Lambda('lambda_0AC5')
    def lambda_0AC5():
        OP_8E(0x00FE, -390, 400, 51440, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0AC5)

    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    OP_6D(-890, 0, 45660, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 1040, 200, 43380, 0)
    SetChrPos(0x0102, -180, 200, 43430, 0)
    SetChrPos(0x00F8, 1360, 400, 41830, 0)
    SetChrPos(0x00F9, -80, 400, 42080, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010340737V#1015F#6P这是……\n',
            '好像是什么装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C1B',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340738V#1064F唔～看起来\n',
            '好像是什么终端。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C5B')

    def _loc_C1B(): pass

    label('loc_C1B')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C5B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340739V#064F难不成\n',
            '是什么装置的终端……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C5B(): pass

    label('loc_C5B')

    ChrTalk(
        0x0102,
        (
            '#0020340740V#1040F#5P……调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C8C')
    def lambda_0C8C():
        OP_6D(-140, 400, 46050, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0C8C)

    OP_8F(0x0102, 250, 150, 45610, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340741V#1035F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340742V#1040F……是这个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x009C, 0x00, 0x64)
    OP_B0(0x0008, 0x78)
    OP_70(0x0008, 0x00000168)
    Sleep(2500)

    OP_22(0x009D, 0x00, 0x64)
    OP_B0(0x0009, 0x64)
    OP_B0(0x000D, 0x64)
    OP_B0(0x000E, 0x64)
    OP_70(0x0009, 0x000000F0)
    Sleep(100)

    OP_70(0x000D, 0x000000F0)
    Sleep(100)

    OP_70(0x000E, 0x000000F0)
    Sleep(100)

    OP_22(0x00B9, 0x00, 0x64)

    @scena.Lambda('lambda_0D66')
    def lambda_0D66():
        OP_6D(-970, 890, 46970, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D66)

    @scena.Lambda('lambda_0D7E')
    def lambda_0D7E():
        OP_67(0, 4420, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D7E)

    @scena.Lambda('lambda_0D96')
    def lambda_0D96():
        OP_6B(3790, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D96)

    @scena.Lambda('lambda_0DA6')
    def lambda_0DA6():
        OP_6E(274, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DA6)

    OP_B0(0x000A, 0x64)
    OP_B0(0x000B, 0x64)
    OP_B0(0x000C, 0x64)
    OP_70(0x000A, 0x00000168)
    OP_70(0x000B, 0x00000168)
    OP_70(0x000C, 0x00000168)
    OP_73(0x000A)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010340743V#1004F哇哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340744V#1040F#5P看来是记录\n',
            '情报的终端啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340745V确认内容看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于封印机构（１／４）』\n',
            '　\n',
            '──我的名字是\n',
            '赛雷斯托·Ｄ·奥赛雷丝。\n',
            '是『封■■■』■■创始■\n',
            '『封■计■■■■负责人。\n',
            '　\n',
            '■■，塔■■■■第二结■启动■■■\n',
            '异次■封■■■■■环』■\n',
            '■■■■■时■■■■■\n',
            '留下■■■的■■■■■的载体■■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■读■这■■■息的■■人\n',
            '■■■■■■■■■『环■■复活\n',
            '■把此作为■■那将是■大幸■。\n',
            '■■■看■期■■环』■■■\n',
            '我请求■■新考虑■■■■■。\n',
            '　\n',
            '『■』■力量■■强大■\n',
            '不是人类■■子能够处理的事■。\n',
            '■纳■■之时\n',
            '也■是■们造■■狱■日。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶０']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶０'], 1)
    OP_A2(0x1E31)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_117C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010340746V#1019F什么啊，除了最开始的部分\n',
            '其它部分都无法辨认嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340747V#1004F唔……\n',
            '这个奥赛雷丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060340748V#047F嗯……\n',
            '是利贝尔王室的姓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340749V#040F说不定是有缘之人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B1')

    def _loc_117C(): pass

    label('loc_117C')

    ChrTalk(
        0x0101,
        (
            '#0010340746V#1019F什么啊，除了最开始的部分\n',
            '其它部分都无法辨认嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340747V#1004F唔……\n',
            '这个奥赛雷丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_125E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340752V#023F说到奥赛雷丝\n',
            '是利贝尔王室的姓啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340753V#020F说不定是有关系的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B1')

    def _loc_125E(): pass

    label('loc_125E')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12D0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340754V#053F说到奥赛雷丝\n',
            '是利贝尔王室的姓哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340755V#051F说不定是有关系的人那。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B1')

    def _loc_12D0(): pass

    label('loc_12D0')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1342',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340756V#073F记得奥赛雷丝\n',
            '应该是利贝尔王室的姓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340757V#070F说不定是有缘之人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B1')

    def _loc_1342(): pass

    label('loc_1342')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13B1',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340758V#1060F说到奥赛雷丝\n',
            '是利贝尔王室的姓呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340759V#1065F很可能是有缘之人呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13B1(): pass

    label('loc_13B1')

    OP_8C(0x0102, 180, 400)

    ChrTalk(
        0x0102,
        (
            '#0020340760V#1035F#2P……看来很可能\n',
            '记载着重大的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340761V#1043F要是能想办法读出来就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15E1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010340762V#1007F嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070340763V#064F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340764V#1015F提妲，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070340765V#061F啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340766V#560F这个水晶，和结晶回路\n',
            '构造好像很相似啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340767V也许……\n',
            '如果花点时间，说不定能复原。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340768V#1004F真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070340769V#560F嗯、嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340770V以前爷爷曾经用『卡佩尔』\n',
            '复原过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340771V#1040F那么，这个水晶\n',
            '就交给博士好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1638')

    def _loc_15E1(): pass

    label('loc_15E1')

    ChrTalk(
        0x0101,
        (
            '#0010340772V#1007F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340773V#1006F嗯，可能会有用\n',
            '姑且保存起来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1638(): pass

    label('loc_1638')

    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0008, 360)
    OP_6F(0x0009, 0)
    OP_6F(0x000A, 0)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    OP_6F(0x000E, 0)
    OP_6D(580, 200, 43320, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 580, 200, 43320, 0)
    SetChrPos(0x0001, 580, 200, 43320, 0)
    SetChrPos(0x0002, 580, 200, 43320, 0)
    SetChrPos(0x0003, 580, 200, 43320, 0)
    OP_69(0x0000, 0x00000000)
    OP_A2(0x1E06)
    Sleep(500)

    FadeIn(1000, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0006 offset: 0x171A
@scena.Code('func_06_171A')
def func_06_171A():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于封印机构（１／４）』\n',
            '　\n',
            '──我的名字是\n',
            '赛雷斯托·Ｄ·奥赛雷丝。\n',
            '是『封■■■』■■创始■\n',
            '『封■计■■■■负责人。\n',
            '　\n',
            '■■，塔■■■■第二结■启动■■■\n',
            '异次■封■■■■■环』■\n',
            '■■■■■时■■■■■\n',
            '留下■■■的■■■■■的载体■■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■读■这■■■息的■■人\n',
            '■■■■■■■■■『环■■复活\n',
            '■把此作为■■那将是■大幸■。\n',
            '■■■看■期■■环』■■■\n',
            '我请求■■新考虑■■■■■。\n',
            '　\n',
            '『■』■力量■■强大■\n',
            '不是人类■■子能够处理的事■。\n',
            '■纳■■之时\n',
            '也■是■们造■■狱■日。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x1948
@scena.Code('func_07_1948')
def func_07_1948():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 7, 0x1E07)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C4B',
    )

    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    OP_B0(0x0000, 0x78)
    OP_70(0x0000, 0x00000168)
    Sleep(2500)

    OP_22(0x009D, 0x00, 0x64)
    OP_B0(0x0004, 0x64)
    OP_B0(0x0005, 0x64)
    OP_B0(0x0006, 0x64)
    OP_B0(0x0007, 0x64)
    OP_70(0x0004, 0x000000F0)
    Sleep(100)

    OP_70(0x0005, 0x000000F0)
    Sleep(100)

    OP_70(0x0006, 0x000000F0)
    Sleep(100)

    OP_70(0x0007, 0x000000F0)
    Sleep(100)

    OP_22(0x00B9, 0x00, 0x64)
    OP_B0(0x0001, 0x64)
    OP_B0(0x0002, 0x64)
    OP_B0(0x0003, 0x64)
    OP_70(0x0001, 0x00000168)
    OP_70(0x0002, 0x00000168)
    OP_70(0x0003, 0x00000168)
    OP_73(0x0001)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于封印机构（２／４）』\n',
            '　\n',
            '本■■，为消■■『的■■\n',
            '从而■■人的■■■■\n',
            '■■立\n',
            '　\n',
            '在这里■■■■■大家■\n',
            '■『环』■身\n',
            '■全没有要■配■的■■\n',
            '事■■起■■■\n',
            '■■我们的■弱和对■■』的过分依■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■大的至宝■■■■■■■■■■\n',
            '■■过于■■\n',
            '所以■女神的■悲和全能\n',
            '丝■■■■■■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶１']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶１'], 1)
    OP_A2(0x1E07)
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_6D(47020, 0, -2740, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 47020, 0, -2740, 0)
    SetChrPos(0x0001, 47020, 0, -2740, 0)
    SetChrPos(0x0002, 47020, 0, -2740, 0)
    SetChrPos(0x0003, 47020, 0, -2740, 0)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_1DAD')

    def _loc_1C4B(): pass

    label('loc_1C4B')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于封印机构（２／４）』\n',
            '　\n',
            '本■■，为消■■『的■■\n',
            '从而■■人的■■■■\n',
            '■■立\n',
            '　\n',
            '在这里■■■■■大家■\n',
            '■『环』■身\n',
            '■全没有要■配■的■■\n',
            '事■■起■■■\n',
            '■■我们的■弱和对■■』的过分依■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■大的至宝■■■■■■■■■■\n',
            '■■过于■■\n',
            '所以■女神的■悲和全能\n',
            '丝■■■■■■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_1DAD(): pass

    label('loc_1DAD')

    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x1DB1
@scena.Code('func_08_1DB1')
def func_08_1DB1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 0, 0x1E08)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20DA',
    )

    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    OP_B0(0x0014, 0x78)
    OP_70(0x0014, 0x00000168)
    Sleep(2500)

    OP_22(0x009D, 0x00, 0x64)
    OP_B0(0x0012, 0x64)
    OP_B0(0x0013, 0x64)
    OP_B0(0x0015, 0x64)
    OP_B0(0x0016, 0x64)
    OP_B0(0x0017, 0x64)
    OP_70(0x0012, 0x000000F0)
    Sleep(100)

    OP_70(0x0013, 0x000000F0)
    Sleep(100)

    OP_70(0x0015, 0x000000F0)
    Sleep(100)

    OP_70(0x0016, 0x000000F0)
    Sleep(100)

    OP_70(0x0017, 0x000000F0)
    Sleep(100)

    OP_22(0x00B9, 0x00, 0x64)
    OP_B0(0x000F, 0x64)
    OP_B0(0x0010, 0x64)
    OP_B0(0x0011, 0x64)
    OP_70(0x000F, 0x00000168)
    OP_70(0x0010, 0x00000168)
    OP_70(0x0011, 0x00000168)
    OP_73(0x000F)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于封印机构（３／４）』\n',
            '　\n',
            '■印机构■■■\n',
            '完■■越■\n',
            '所谓■民■主义■■\n',
            '　\n',
            '即使在我■■中，\n',
            '■存在着■■\n',
            '认为■当有效■■■有无■■■的『环■■意见',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■是，■『■■■■■■性之后\n',
            '■■以势不可挡■■■\n',
            '给社会■■■生活带■■■■■■\n',
            '■可思议地，■仅仅■■物质■■■■\n',
            '■■■括■精■层■的■■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶２']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶２'], 1)
    OP_A2(0x1E08)
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x000F, 0)
    OP_6F(0x0010, 0)
    OP_6F(0x0011, 0)
    OP_6F(0x0012, 0)
    OP_6F(0x0013, 0)
    OP_6F(0x0014, 360)
    OP_6F(0x0015, 0)
    OP_6F(0x0016, 0)
    OP_6F(0x0017, 0)
    OP_6D(-46490, 200, -3220, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -46490, 200, -3220, 0)
    SetChrPos(0x0001, -46490, 200, -3220, 0)
    SetChrPos(0x0002, -46490, 200, -3220, 0)
    SetChrPos(0x0003, -46490, 200, -3220, 0)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_224B')

    def _loc_20DA(): pass

    label('loc_20DA')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于封印机构（３／４）』\n',
            '　\n',
            '■印机构■■■\n',
            '完■■越■\n',
            '所谓■民■主义■■\n',
            '　\n',
            '即使在我■■中，\n',
            '■存在着■■\n',
            '认为■当有效■■■有无■■■的『环■■意见',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■是，■『■■■■■■性之后\n',
            '■■以势不可挡■■■\n',
            '给社会■■■生活带■■■■■■\n',
            '■可思议地，■仅仅■■物质■■■■\n',
            '■■■括■精■层■的■■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_224B(): pass

    label('loc_224B')

    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x224F
@scena.Code('func_09_224F')
def func_09_224F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 1, 0x1E09)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25ED',
    )

    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    OP_B0(0x0018, 0x78)
    OP_70(0x0018, 0x00000168)
    Sleep(2500)

    OP_22(0x009D, 0x00, 0x64)
    OP_B0(0x001C, 0x64)
    OP_B0(0x001D, 0x64)
    OP_B0(0x001E, 0x64)
    OP_B0(0x001F, 0x64)
    OP_70(0x001C, 0x000000F0)
    Sleep(100)

    OP_70(0x001D, 0x000000F0)
    Sleep(100)

    OP_70(0x001E, 0x000000F0)
    Sleep(100)

    OP_70(0x001F, 0x000000F0)
    Sleep(500)

    OP_22(0x00B9, 0x00, 0x64)
    OP_B0(0x0019, 0x64)
    OP_B0(0x001A, 0x64)
    OP_B0(0x001B, 0x64)
    OP_70(0x0019, 0x00000168)
    OP_70(0x001A, 0x00000168)
    OP_70(0x001B, 0x00000168)
    OP_73(0x0019)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于封印机构（４／４）』\n',
            '　\n',
            '■■『环』■■■福音』\n',
            '■市民■■■■来幸■■的■想■实，\n',
            '■■■至■■控制■■内■质。\n',
            '　\n',
            '■可■■时摄■这方面\n',
            '■与■力无穷■■品和致■剂■■■致\n',
            '然■■■的■，\n',
            '这种■■■理方■并没■副■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■恩惠■给人类的真实■在\n',
            '带来■样深■■■■啊■…\n',
            '　\n',
            '这种■■已经在■多市民■■■■现出■，\n',
            '■■■■的时间太■■。\n',
            '因此我们■■■意见的■■\n',
            '在精神上■可能出现的一切困难■■了思■准备\n',
            '■手■■了■■■■■』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶３']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶３'], 1)
    OP_A2(0x1E09)
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0018, 360)
    OP_6F(0x0019, 0)
    OP_6F(0x001A, 0)
    OP_6F(0x001B, 0)
    OP_6F(0x001C, 0)
    OP_6F(0x001D, 0)
    OP_6F(0x001E, 0)
    OP_6F(0x001F, 0)
    OP_6D(340, 200, -50000, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 340, 200, -50000, 0)
    SetChrPos(0x0001, 340, 200, -50000, 0)
    SetChrPos(0x0002, 340, 200, -50000, 0)
    SetChrPos(0x0003, 340, 200, -50000, 0)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_27EA')

    def _loc_25ED(): pass

    label('loc_25ED')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于封印机构（４／４）』\n',
            '　\n',
            '■■『环』■■■福音』\n',
            '■市民■■■■来幸■■的■想■实，\n',
            '■■■至■■控制■■内■质。\n',
            '　\n',
            '■可■■时摄■这方面\n',
            '■与■力无穷■■品和致■剂■■■致\n',
            '然■■■的■，\n',
            '这种■■■理方■并没■副■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■恩惠■给人类的真实■在\n',
            '带来■样深■■■■啊■…\n',
            '　\n',
            '这种■■已经在■多市民■■■■现出■，\n',
            '■■■■的时间太■■。\n',
            '因此我们■■■意见的■■\n',
            '在精神上■可能出现的一切困难■■了思■准备\n',
            '■手■■了■■■■■』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_27EA(): pass

    label('loc_27EA')

    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0x27EE
@scena.Code('func_0A_27EE')
def func_0A_27EE():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2868'),
        (0x00000001, 'loc_286E'),
        (-1, 'loc_2874'),
    )

    def _loc_2868(): pass

    label('loc_2868')

    OP_A2(0x1200)

    Jump('loc_2874')

    def _loc_286E(): pass

    label('loc_286E')

    OP_A2(0x1201)

    Jump('loc_2874')

    def _loc_2874(): pass

    label('loc_2874')

    Return()

# id: 0x000B offset: 0x2875
@scena.Code('func_0B_2875')
def func_0B_2875():
    FadeOut(0, 0, -1)
    OP_6D(-33260, 200, 68720, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x000C offset: 0x2904
@scena.Code('func_0C_2904')
def func_0C_2904():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 250, 81590, 0)
    SetChrPos(0x0101, 500, 250, 81090, 180)
    SetChrPos(0x0102, -500, 250, 81090, 180)
    SetChrPos(0x00F8, 500, 250, 82090, 180)
    SetChrPos(0x00F9, -500, 250, 82090, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(0, 300, 78810, 0)
    SetChrPos(0x0000, 0, 300, 78810, 180)
    SetChrPos(0x0001, 0, 300, 78810, 180)
    SetChrPos(0x0002, 0, 300, 78810, 180)
    SetChrPos(0x0003, 0, 300, 78810, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000D offset: 0x2A04
@scena.Code('func_0D_2A04')
def func_0D_2A04():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(0, 250, 81590, 0)
    SetChrPos(0x0101, -500, 250, 82090, 0)
    SetChrPos(0x0102, 500, 250, 82090, 0)
    SetChrPos(0x00F8, -500, 250, 81090, 0)
    SetChrPos(0x00F9, 500, 250, 81090, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0702._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x2A7C
@scena.Code('func_0E_2A7C')
def func_0E_2A7C():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(15310, -9350, 15430, 0)
    SetChrPos(0x0101, 15810, -9350, 14930, 180)
    SetChrPos(0x0102, 14810, -9350, 14930, 180)
    SetChrPos(0x00F8, 15810, -9350, 15930, 180)
    SetChrPos(0x00F9, 14810, -9350, 15930, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(15150, -9300, 12650, 0)
    SetChrPos(0x0000, 15150, -9300, 12650, 180)
    SetChrPos(0x0001, 15150, -9300, 12650, 180)
    SetChrPos(0x0002, 15150, -9300, 12650, 180)
    SetChrPos(0x0003, 15150, -9300, 12650, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000F offset: 0x2B7C
@scena.Code('func_0F_2B7C')
def func_0F_2B7C():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(15310, -9350, 15430, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 14810, -9350, 15930, 0)
    SetChrPos(0x0102, 15810, -9350, 15930, 0)
    SetChrPos(0x00F8, 14810, -9350, 14930, 0)
    SetChrPos(0x00F9, 15810, -9350, 14930, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0702._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x2C20
@scena.Code('func_10_2C20')
def func_10_2C20():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-15300, -9350, -15300, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, -15810, -9350, -14800, 0)
    SetChrPos(0x0102, -14810, -9350, -14800, 0)
    SetChrPos(0x00F8, -15810, -9350, -15800, 0)
    SetChrPos(0x00F9, -14810, -9350, -15800, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(-15320, -9650, -10940, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, -15320, -9650, -10940, 0)
    SetChrPos(0x0001, -15320, -9650, -10940, 0)
    SetChrPos(0x0002, -15320, -9650, -10940, 0)
    SetChrPos(0x0003, -15320, -9650, -10940, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0011 offset: 0x2D32
@scena.Code('func_11_2D32')
def func_11_2D32():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(-15300, -9350, -15300, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, -14810, -9350, -15800, 180)
    SetChrPos(0x0102, -15810, -9350, -15800, 180)
    SetChrPos(0x00F8, -14810, -9350, -14800, 180)
    SetChrPos(0x00F9, -15810, -9350, -14800, 180)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0702._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x2DB3
@scena.Code('func_12_2DB3')
def func_12_2DB3():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 250, -81500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, -500, 250, -81000, 0)
    SetChrPos(0x0102, 500, 250, -81000, 0)
    SetChrPos(0x00F8, -500, 250, -82000, 0)
    SetChrPos(0x00F9, 500, 250, -82000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(40, -50, -77230, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, 40, -50, -77230, 0)
    SetChrPos(0x0001, 40, -50, -77230, 0)
    SetChrPos(0x0002, 40, -50, -77230, 0)
    SetChrPos(0x0003, 40, -50, -77230, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0013 offset: 0x2EC5
@scena.Code('func_13_2EC5')
def func_13_2EC5():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(0, 250, -81500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, 500, 250, -82000, 180)
    SetChrPos(0x0102, -500, 250, -82000, 180)
    SetChrPos(0x00F8, 500, 250, -81000, 180)
    SetChrPos(0x00F9, -500, 250, -81000, 180)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0704._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x2F46
@scena.Code('func_14_2F46')
def func_14_2F46():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(15000, -5750, -15500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, 14500, -5750, -15000, 0)
    SetChrPos(0x0102, 15500, -5750, -15000, 0)
    SetChrPos(0x00F8, 14500, -5750, -16000, 0)
    SetChrPos(0x00F9, 15500, -5750, -16000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(15170, -6050, -11100, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, 15170, -6050, -11100, 0)
    SetChrPos(0x0001, 15170, -6050, -11100, 0)
    SetChrPos(0x0002, 15170, -6050, -11100, 0)
    SetChrPos(0x0003, 15170, -6050, -11100, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0015 offset: 0x3058
@scena.Code('func_15_3058')
def func_15_3058():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(15000, -5750, -15500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, 15500, -5750, -16000, 180)
    SetChrPos(0x0102, 14500, -5750, -16000, 180)
    SetChrPos(0x00F8, 15500, -5750, -15000, 180)
    SetChrPos(0x00F9, 14500, -5750, -15000, 180)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0704._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x30D9
@scena.Code('func_16_30D9')
def func_16_30D9():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-15300, -5750, 15500, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0101, -14800, -5750, 15000, 180)
    SetChrPos(0x0102, -15800, -5750, 15000, 180)
    SetChrPos(0x00F8, -14800, -5750, 16000, 180)
    SetChrPos(0x00F9, -15800, -5750, 16000, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(-15280, -5720, 12800, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, -15280, -5720, 12800, 180)
    SetChrPos(0x0001, -15280, -5720, 12800, 180)
    SetChrPos(0x0002, -15280, -5720, 12800, 180)
    SetChrPos(0x0003, -15280, -5720, 12800, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0017 offset: 0x31EB
@scena.Code('func_17_31EB')
def func_17_31EB():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(-15300, -5750, 15500, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0101, -15800, -5750, 16000, 0)
    SetChrPos(0x0102, -14800, -5750, 16000, 0)
    SetChrPos(0x00F8, -15800, -5750, 15000, 0)
    SetChrPos(0x00F9, -14800, -5750, 15000, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0704._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x326C
@scena.Code('func_18_326C')
def func_18_326C():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0019 offset: 0x334B
@scena.Code('func_19_334B')
def func_19_334B():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x001A offset: 0x342A
@scena.Code('func_1A_342A')
def func_1A_342A():
    @scena.Lambda('lambda_3430')
    def lambda_3430():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3430)

    @scena.Lambda('lambda_3442')
    def lambda_3442():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3442)

    @scena.Lambda('lambda_3454')
    def lambda_3454():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3454)

    @scena.Lambda('lambda_3466')
    def lambda_3466():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3466)

    Sleep(2500)

    Return()

# id: 0x001B offset: 0x3478
@scena.Code('func_1B_3478')
def func_1B_3478():
    @scena.Lambda('lambda_347E')
    def lambda_347E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_347E)

    @scena.Lambda('lambda_3490')
    def lambda_3490():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3490)

    @scena.Lambda('lambda_34A2')
    def lambda_34A2():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_34A2)

    @scena.Lambda('lambda_34B4')
    def lambda_34B4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_34B4)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
