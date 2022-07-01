import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1602_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1602   ._SN')

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
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1602.x'
    header.mapIndex       = 250
    header.bgm            = 125
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x847
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
        ('ED6_DT29/CH12450._CH', 'ED6_DT29/CH12450P._CP'),
        ('ED6_DT29/CH12451._CH', 'ED6_DT29/CH12451P._CP'),
        ('ED6_DT09/CH10840._CH', 'ED6_DT09/CH10840P._CP'),
        ('ED6_DT09/CH10841._CH', 'ED6_DT09/CH10841P._CP'),
        ('ED6_DT29/CH12460._CH', 'ED6_DT29/CH12460P._CP'),
        ('ED6_DT29/CH12461._CH', 'ED6_DT29/CH12461P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10551._CH', 'ED6_DT09/CH10551P._CP'),
        ('ED6_DT29/CH12500._CH', 'ED6_DT29/CH12500P._CP'),
        ('ED6_DT29/CH12501._CH', 'ED6_DT29/CH12501P._CP'),
        ('ED6_DT29/CH12560._CH', 'ED6_DT29/CH12560P._CP'),
        ('ED6_DT29/CH12561._CH', 'ED6_DT29/CH12561P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 33560,
            z           = 0,
            y           = -17800,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 9220,
            z           = -1000,
            y           = -5220,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 10130,
            z           = 0,
            y           = 41950,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -31690,
            z           = 0,
            y           = 17530,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -22920,
            z           = -1000,
            y           = 3720,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17070,
            z           = -500,
            y           = -6360,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 159370,
            z           = 0,
            y           = -1020,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 184150,
            z           = -500,
            y           = -2380,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 186100,
            z           = 0,
            y           = 12660,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 209310,
            z           = 0,
            y           = -1090,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 230690,
            z           = -500,
            y           = -3880,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x23E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x23E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 16510,
            triggerZ            = 0,
            triggerY            = 40840,
            triggerRange        = 1000,
            actorX              = 17170,
            actorZ              = 0,
            actorY              = 40840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 245230,
            triggerZ            = 0,
            triggerY            = 25460,
            triggerRange        = 1000,
            actorX              = 245680,
            actorZ              = 0,
            actorY              = 25970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9970,
            triggerZ            = 0,
            triggerY            = 48740,
            triggerRange        = 1000,
            actorX              = 10010,
            actorZ              = 0,
            actorY              = 49440,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -16170,
            triggerZ            = 0,
            triggerY            = 17900,
            triggerRange        = 1000,
            actorX              = -15800,
            actorZ              = 0,
            actorY              = 18460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2CE
@scena.Code('PreInit')
def PreInit():
    OP_11(0xFF, 0xFF, 0xFF, 0x00009C40, 0x00012110, 0x00000000)

    Return()

# id: 0x0001 offset: 0x2DF
@scena.Code('Init')
def Init():
    OP_22(0x01C7, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0372, 0, 0x1B90)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F6',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2FD')

    def _loc_2F6(): pass

    label('loc_2F6')

    OP_6F(0x0000, 60)

    def _loc_2FD(): pass

    label('loc_2FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0372, 2, 0x1B92)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30F',
    )

    OP_6F(0x0001, 0)

    Jump('loc_316')

    def _loc_30F(): pass

    label('loc_30F')

    OP_6F(0x0001, 60)

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0372, 4, 0x1B94)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_328',
    )

    OP_6F(0x0002, 0)

    Jump('loc_32F')

    def _loc_328(): pass

    label('loc_328')

    OP_6F(0x0002, 60)

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0372, 5, 0x1B95)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_341',
    )

    OP_6F(0x0003, 0)

    Jump('loc_348')

    def _loc_341(): pass

    label('loc_341')

    OP_6F(0x0003, 60)

    def _loc_348(): pass

    label('loc_348')

    ExecExpressionWithValue(
        0x0009,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

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

    ExecExpressionWithValue(
        0x0010,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3C2',
    )

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x578),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3CC')

    def _loc_3C2(): pass

    label('loc_3C2')

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x12C),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3CC(): pass

    label('loc_3CC')

    Return()

# id: 0x0002 offset: 0x3CD
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x63, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0372, 0, 0x1B90)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4AA',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['亚伦之剑'], 1)"),
            Expr.Return,
        ),
        'loc_441',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['亚伦之剑']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B90)

    Jump('loc_4A7')

    def _loc_441(): pass

    label('loc_441')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['亚伦之剑']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['亚伦之剑']),
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

    def _loc_4A7(): pass

    label('loc_4A7')

    Jump('loc_4DB')

    def _loc_4AA(): pass

    label('loc_4AA')

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
    def _loc_4DB(): pass

    label('loc_4DB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x4E9
@scena.Code('func_03_4E9')
def func_03_4E9():
    UnlockAchievement(0x02, 0x64, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0372, 2, 0x1B92)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_584',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000001E)
    OP_73(0x0001)
    OP_6F(0x0001, 30)
    AddSepith(0x00, 0x0064)
    AddSepith(0x06, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B92)

    Jump('loc_59E')

    def _loc_584(): pass

    label('loc_584')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_59E(): pass

    label('loc_59E')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5B0
@scena.Code('func_04_5B0')
def func_04_5B0():
    UnlockAchievement(0x02, 0x65, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0372, 4, 0x1B94)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68D',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_624',
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
    OP_A2(0x1B94)

    Jump('loc_68A')

    def _loc_624(): pass

    label('loc_624')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_68A(): pass

    label('loc_68A')

    Jump('loc_6BE')

    def _loc_68D(): pass

    label('loc_68D')

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
    def _loc_6BE(): pass

    label('loc_6BE')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6CC
@scena.Code('func_05_6CC')
def func_05_6CC():
    UnlockAchievement(0x02, 0x66, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0372, 5, 0x1B95)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A9',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['七色不可思议玉'], 1)"),
            Expr.Return,
        ),
        'loc_740',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['七色不可思议玉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B95)

    Jump('loc_7A6')

    def _loc_740(): pass

    label('loc_740')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['七色不可思议玉']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['七色不可思议玉']),
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

    def _loc_7A6(): pass

    label('loc_7A6')

    Jump('loc_7DA')

    def _loc_7A9(): pass

    label('loc_7A9')

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
    def _loc_7DA(): pass

    label('loc_7DA')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_832',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0030)"),
            Expr.Return,
        ),
        'loc_7F9',
    )

    Jump('loc_832')

    def _loc_7F9(): pass

    label('loc_7F9')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['七色不可思议玉']),
            (TxtCtl.SetColor, 0x0),
            '的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['七色不可思议玉']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_832(): pass

    label('loc_832')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
