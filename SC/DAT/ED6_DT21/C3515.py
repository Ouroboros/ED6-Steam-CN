import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3515_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3515   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3515.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA8D
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
        ('ED6_DT09/CH10710._CH', 'ED6_DT09/CH10710P._CP'),
        ('ED6_DT09/CH10711._CH', 'ED6_DT09/CH10711P._CP'),
        ('ED6_DT09/CH10720._CH', 'ED6_DT09/CH10720P._CP'),
        ('ED6_DT09/CH10721._CH', 'ED6_DT09/CH10721P._CP'),
        ('ED6_DT09/CH10730._CH', 'ED6_DT09/CH10730P._CP'),
        ('ED6_DT09/CH10731._CH', 'ED6_DT09/CH10731P._CP'),
        ('ED6_DT09/CH10740._CH', 'ED6_DT09/CH10740P._CP'),
        ('ED6_DT09/CH10741._CH', 'ED6_DT09/CH10741P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -8980,
            z                   = 1000,
            y                   = -8790,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -10,
            z           = 0,
            y           = 20060,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F8,
            word_18     = 0x1592,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -12470,
            z           = 0,
            y           = -90,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F7,
            word_18     = 0x1593,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 12450,
            z           = 0,
            y           = -40,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F6,
            word_18     = 0x1594,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x15E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x15E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 9470,
            triggerZ            = 0,
            triggerY            = 8330,
            triggerRange        = 1000,
            actorX              = 9000,
            actorZ              = 0,
            actorY              = 8800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17550,
            triggerZ            = 0,
            triggerY            = -12440,
            triggerRange        = 1000,
            actorX              = 17180,
            actorZ              = 0,
            actorY              = -12940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9430,
            triggerZ            = 0,
            triggerY            = -8330,
            triggerRange        = 1000,
            actorX              = -8980,
            actorZ              = 0,
            actorY              = -8790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12360,
            triggerZ            = 0,
            triggerY            = -17620,
            triggerRange        = 1000,
            actorX              = -12880,
            actorZ              = 0,
            actorY              = -17210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9380,
            triggerZ            = 0,
            triggerY            = -8320,
            triggerRange        = 1000,
            actorX              = 8970,
            actorZ              = 0,
            actorY              = -8790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9250,
            triggerZ            = 0,
            triggerY            = 8430,
            triggerRange        = 1000,
            actorX              = -8800,
            actorZ              = 0,
            actorY              = 8880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x236
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x237
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_249',
    )

    OP_10(0x00, 0x00)
    OP_10(0x04, 0x01)

    def _loc_249(): pass

    label('loc_249')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 3, 0x154B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25B',
    )

    OP_6F(0x0000, 0)

    Jump('loc_262')

    def _loc_25B(): pass

    label('loc_25B')

    OP_6F(0x0000, 60)

    def _loc_262(): pass

    label('loc_262')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 5, 0x154D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_274',
    )

    OP_6F(0x0001, 0)

    Jump('loc_27B')

    def _loc_274(): pass

    label('loc_274')

    OP_6F(0x0001, 60)

    def _loc_27B(): pass

    label('loc_27B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 7, 0x154F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28D',
    )

    OP_6F(0x0002, 0)

    Jump('loc_294')

    def _loc_28D(): pass

    label('loc_28D')

    OP_6F(0x0002, 60)

    def _loc_294(): pass

    label('loc_294')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AA, 1, 0x1551)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A6',
    )

    OP_6F(0x0003, 0)

    Jump('loc_2AD')

    def _loc_2A6(): pass

    label('loc_2A6')

    OP_6F(0x0003, 60)

    def _loc_2AD(): pass

    label('loc_2AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AA, 3, 0x1553)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BF',
    )

    OP_6F(0x0004, 0)

    Jump('loc_2C6')

    def _loc_2BF(): pass

    label('loc_2BF')

    OP_6F(0x0004, 60)

    def _loc_2C6(): pass

    label('loc_2C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AA, 4, 0x1554)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D8',
    )

    OP_6F(0x0005, 0)

    Jump('loc_2DF')

    def _loc_2D8(): pass

    label('loc_2D8')

    OP_6F(0x0005, 60)

    def _loc_2DF(): pass

    label('loc_2DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B2, 2, 0x1592)),
            Expr.Return,
        ),
        'loc_2EB',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_2EB(): pass

    label('loc_2EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B2, 3, 0x1593)),
            Expr.Return,
        ),
        'loc_2F7',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_2F7(): pass

    label('loc_2F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02B2, 4, 0x1594)),
            Expr.Return,
        ),
        'loc_303',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_303(): pass

    label('loc_303')

    Return()

# id: 0x0002 offset: 0x304
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_319',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_319(): pass

    label('loc_319')

    Return()

# id: 0x0003 offset: 0x31A
@scena.Code('func_03_31A')
def func_03_31A():
    UnlockAchievement(0x02, 0xCF, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 3, 0x154B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F7',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['溜冰鞋'], 1)"),
            Expr.Return,
        ),
        'loc_38E',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['溜冰鞋']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x154B)

    Jump('loc_3F4')

    def _loc_38E(): pass

    label('loc_38E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['溜冰鞋']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['溜冰鞋']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_3F4(): pass

    label('loc_3F4')

    Jump('loc_428')

    def _loc_3F7(): pass

    label('loc_3F7')

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
    def _loc_428(): pass

    label('loc_428')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x436
@scena.Code('func_04_436')
def func_04_436():
    UnlockAchievement(0x02, 0xD0, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 5, 0x154D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_513',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['蓝色猿羊绒'], 1)"),
            Expr.Return,
        ),
        'loc_4AA',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['蓝色猿羊绒']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x154D)

    Jump('loc_510')

    def _loc_4AA(): pass

    label('loc_4AA')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['蓝色猿羊绒']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['蓝色猿羊绒']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_510(): pass

    label('loc_510')

    Jump('loc_544')

    def _loc_513(): pass

    label('loc_513')

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
    def _loc_544(): pass

    label('loc_544')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x552
@scena.Code('func_05_552')
def func_05_552():
    UnlockAchievement(0x02, 0xD1, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A9, 7, 0x154F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6EA',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AA, 0, 0x1550)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_636',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_05A9')
    def lambda_05A9():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05A9)

    @scena.Lambda('lambda_05C4')
    def lambda_05C4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_05C4)

    ClearChrFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001F9, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_611'),
        (0x00000002, 'loc_623'),
        (0x00000001, 'loc_633'),
        (-1, 'loc_636'),
    )

    def _loc_611(): pass

    label('loc_611')

    OP_A2(0x1550)
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_636')

    def _loc_623(): pass

    label('loc_623')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_633(): pass

    label('loc_633')

    OP_B4(0x00)

    Return()

    def _loc_636(): pass

    label('loc_636')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['攻击３'], 1)"),
            Expr.Return,
        ),
        'loc_685',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['攻击３']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x154F)

    Jump('loc_6E7')

    def _loc_685(): pass

    label('loc_685')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['攻击３']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['攻击３']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_6E7(): pass

    label('loc_6E7')

    Jump('loc_719')

    def _loc_6EA(): pass

    label('loc_6EA')

    FadeOut(300, 0, 100)

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
    def _loc_719(): pass

    label('loc_719')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x727
@scena.Code('func_06_727')
def func_06_727():
    UnlockAchievement(0x02, 0xD2, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AA, 1, 0x1551)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_804',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['红色夹克'], 1)"),
            Expr.Return,
        ),
        'loc_79B',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['红色夹克']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1551)

    Jump('loc_801')

    def _loc_79B(): pass

    label('loc_79B')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['红色夹克']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['红色夹克']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)

    def _loc_801(): pass

    label('loc_801')

    Jump('loc_835')

    def _loc_804(): pass

    label('loc_804')

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
    def _loc_835(): pass

    label('loc_835')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x843
@scena.Code('func_07_843')
def func_07_843():
    UnlockAchievement(0x02, 0xD3, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AA, 3, 0x1553)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_920',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_8B7',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1553)

    Jump('loc_91D')

    def _loc_8B7(): pass

    label('loc_8B7')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0x00000000)

    def _loc_91D(): pass

    label('loc_91D')

    Jump('loc_951')

    def _loc_920(): pass

    label('loc_920')

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
    def _loc_951(): pass

    label('loc_951')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x95F
@scena.Code('func_08_95F')
def func_08_95F():
    UnlockAchievement(0x02, 0xD4, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AA, 4, 0x1554)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A3C',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['五轮棍'], 1)"),
            Expr.Return,
        ),
        'loc_9D3',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['五轮棍']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1554)

    Jump('loc_A39')

    def _loc_9D3(): pass

    label('loc_9D3')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['五轮棍']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['五轮棍']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0x00000000)

    def _loc_A39(): pass

    label('loc_A39')

    Jump('loc_A6D')

    def _loc_A3C(): pass

    label('loc_A3C')

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
    def _loc_A6D(): pass

    label('loc_A6D')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
