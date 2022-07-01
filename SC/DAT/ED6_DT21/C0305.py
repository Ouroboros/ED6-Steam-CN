import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0305_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0305   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0305.x'
    header.mapIndex       = 19
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x95E
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x000088B8,
            dword_04        = 0x00000000,
            dword_08        = 0x00003E80,
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
            word_3A         = 19,
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
        ('ED6_DT29/CH12430._CH', 'ED6_DT29/CH12430P._CP'),
        ('ED6_DT29/CH12431._CH', 'ED6_DT29/CH12431P._CP'),
        ('ED6_DT09/CH10010._CH', 'ED6_DT09/CH10010P._CP'),
        ('ED6_DT09/CH10011._CH', 'ED6_DT09/CH10011P._CP'),
        ('ED6_DT09/CH10280._CH', 'ED6_DT09/CH10280P._CP'),
        ('ED6_DT09/CH10281._CH', 'ED6_DT09/CH10281P._CP'),
        ('ED6_DT29/CH12400._CH', 'ED6_DT29/CH12400P._CP'),
        ('ED6_DT29/CH12401._CH', 'ED6_DT29/CH12401P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 6930,
            z           = 40,
            y           = -26770,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5350,
            z           = -180,
            y           = -27890,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -15690,
            z           = -310,
            y           = 1410,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -3030,
            z           = 410,
            y           = 24850,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 6930,
            z           = 40,
            y           = -26770,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0040,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5350,
            z           = -180,
            y           = -27890,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0041,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -15690,
            z           = -310,
            y           = 1410,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0042,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -3030,
            z           = 410,
            y           = 24850,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0041,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1CA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -14410,
            triggerZ            = -120,
            triggerY            = 8350,
            triggerRange        = 1000,
            actorX              = -14410,
            actorZ              = -120,
            actorY              = 9060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -22500,
            triggerZ            = -150,
            triggerY            = 35130,
            triggerRange        = 1000,
            actorX              = -22500,
            actorZ              = -150,
            actorY              = 35720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 18070,
            triggerZ            = -120,
            triggerY            = 17440,
            triggerRange        = 1000,
            actorX              = 18470,
            actorZ              = -120,
            actorY              = 17840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9770,
            triggerZ            = -170,
            triggerY            = 41560,
            triggerRange        = 1800,
            actorX              = -9770,
            actorZ              = 1200,
            actorY              = 41560,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x25A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x25B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            (Expr.TestScenaFlags, ScenaFlag(0x0316, 0, 0x18B0)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_26A',
    )

    OP_64(0x03, 0x0001)

    def _loc_26A(): pass

    label('loc_26A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 1, 0x1961)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27C',
    )

    OP_6F(0x0004, 0)

    Jump('loc_283')

    def _loc_27C(): pass

    label('loc_27C')

    OP_6F(0x0004, 60)

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 2, 0x1962)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_295',
    )

    OP_6F(0x0005, 0)

    Jump('loc_29C')

    def _loc_295(): pass

    label('loc_295')

    OP_6F(0x0005, 60)

    def _loc_29C(): pass

    label('loc_29C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 4, 0x1964)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AE',
    )

    OP_6F(0x0006, 0)

    Jump('loc_2B5')

    def _loc_2AE(): pass

    label('loc_2AE')

    OP_6F(0x0006, 60)

    def _loc_2B5(): pass

    label('loc_2B5')

    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2FF',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)

    Jump('loc_313')

    def _loc_2FF(): pass

    label('loc_2FF')

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)

    def _loc_313(): pass

    label('loc_313')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_341',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_341',
    )

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000EA60, 0x00000000)
    OP_C4(0x00, 0x00000004)

    def _loc_341(): pass

    label('loc_341')

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)

    Return()

# id: 0x0002 offset: 0x356
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x02, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 1, 0x1961)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_433',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['狼牙鞭'], 1)"),
            Expr.Return,
        ),
        'loc_3CA',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['狼牙鞭']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1961)

    Jump('loc_430')

    def _loc_3CA(): pass

    label('loc_3CA')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['狼牙鞭']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['狼牙鞭']),
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

    def _loc_430(): pass

    label('loc_430')

    Jump('loc_464')

    def _loc_433(): pass

    label('loc_433')

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
    def _loc_464(): pass

    label('loc_464')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x472
@scena.Code('func_03_472')
def func_03_472():
    UnlockAchievement(0x02, 0x03, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 2, 0x1962)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['岩钉靴子'], 1)"),
            Expr.Return,
        ),
        'loc_4E6',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['岩钉靴子']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1962)

    Jump('loc_54C')

    def _loc_4E6(): pass

    label('loc_4E6')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['岩钉靴子']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['岩钉靴子']),
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

    def _loc_54C(): pass

    label('loc_54C')

    Jump('loc_580')

    def _loc_54F(): pass

    label('loc_54F')

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
    def _loc_580(): pass

    label('loc_580')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x58E
@scena.Code('func_04_58E')
def func_04_58E():
    UnlockAchievement(0x02, 0x04, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 4, 0x1964)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66B',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0006, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_602',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1964)

    Jump('loc_668')

    def _loc_602(): pass

    label('loc_602')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0x00000000)

    def _loc_668(): pass

    label('loc_668')

    Jump('loc_69C')

    def _loc_66B(): pass

    label('loc_66B')

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
    def _loc_69C(): pass

    label('loc_69C')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6AA
@scena.Code('func_05_6AA')
def func_05_6AA():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0103, -7530, -30, 39130, 315)
    SetChrPos(0x0101, -8530, -80, 38500, 315)
    SetChrPos(0x00F8, -7670, -50, 37260, 315)
    SetChrPos(0x00F9, -6710, 30, 37730, 315)
    OP_6D(-7900, -60, 38750, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290567V#1004F#6P咦……？',
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
        'loc_791',
    )

    ChrTalk(
        0x0107,
        (
            '#0070290568V#064F怎么了，姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_876')

    def _loc_791(): pass

    label('loc_791')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7CB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290569V#044F艾丝蒂尔，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_876')

    def _loc_7CB(): pass

    label('loc_7CB')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_805',
    )

    ChrTalk(
        0x0104,
        (
            '#0040290570V#033F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_876')

    def _loc_805(): pass

    label('loc_805')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_83F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050290571V#053F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_876')

    def _loc_83F(): pass

    label('loc_83F')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_876',
    )

    ChrTalk(
        0x0108,
        (
            '#0080290572V#073F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_876(): pass

    label('loc_876')

    ChrTalk(
        0x0101,
        (
            '#0010290573V#1016F#6P啊，嗯，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290574V#1015F（之前来的时候，记得这里\n',
            '好像有路来着……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350036V（好久没来神秘森林了\n',
            '　是迷路了吗……？)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290575V#022F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x18B0)
    OP_64(0x03, 0x0001)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
