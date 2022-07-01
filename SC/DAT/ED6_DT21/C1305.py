import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1305_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1305   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '穆拉'),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1305.x'
    header.mapIndex       = 52
    header.bgm            = 89
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xDBB
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
        ('ED6_DT09/CH10380._CH', 'ED6_DT09/CH10380P._CP'),
        ('ED6_DT09/CH10381._CH', 'ED6_DT09/CH10381P._CP'),
        ('ED6_DT09/CH10390._CH', 'ED6_DT09/CH10390P._CP'),
        ('ED6_DT09/CH10391._CH', 'ED6_DT09/CH10391P._CP'),
        ('ED6_DT09/CH10250._CH', 'ED6_DT09/CH10250P._CP'),
        ('ED6_DT09/CH10251._CH', 'ED6_DT09/CH10251P._CP'),
        ('ED6_DT07/CH00330._CH', 'ED6_DT07/CH00330P._CP'),
        ('ED6_DT07/CH00331._CH', 'ED6_DT07/CH00331P._CP'),
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x112
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -5080,
            z           = 0,
            y           = 890,
            word_0C     = 0x0085,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00A2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 65660,
            z           = 0,
            y           = -21310,
            word_0C     = 0x00A7,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00A1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -117030,
            z           = 0,
            y           = -197030,
            word_0C     = 0x0163,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00A1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x166
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x166
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -164160,
            triggerZ            = 0,
            triggerY            = -193160,
            triggerRange        = 1000,
            actorX              = -164160,
            actorZ              = 1500,
            actorY              = -193160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -54870,
            triggerZ            = 0,
            triggerY            = 46490,
            triggerRange        = 1000,
            actorX              = -54740,
            actorZ              = 1500,
            actorY              = 47090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -206690,
            triggerZ            = 0,
            triggerY            = -155420,
            triggerRange        = 1000,
            actorX              = -206660,
            actorZ              = 1500,
            actorY              = -154670,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4600,
            triggerZ            = 0,
            triggerY            = 41900,
            triggerRange        = 1000,
            actorX              = 5290,
            actorZ              = 0,
            actorY              = 42020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4550,
            triggerZ            = 0,
            triggerY            = 83030,
            triggerRange        = 1000,
            actorX              = 5170,
            actorZ              = 0,
            actorY              = 82970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 54600,
            triggerZ            = 0,
            triggerY            = 41990,
            triggerRange        = 1000,
            actorX              = 55250,
            actorZ              = 0,
            actorY              = 41960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -51050,
            triggerZ            = 0,
            triggerY            = -136510,
            triggerRange        = 800,
            actorX              = -51050,
            actorZ              = 800,
            actorY              = -136510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x262
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_27C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    Event(0, 0x000B)

    Jump('loc_28E')

    def _loc_27C(): pass

    label('loc_27C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_28E',
    )

    OP_64(0x06, 0x0001)
    OP_A3(0x10F1)
    Event(0, 0x0009)

    def _loc_28E(): pass

    label('loc_28E')

    Return()

# id: 0x0001 offset: 0x28F
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 4, 0x1904)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A1',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2A8')

    def _loc_2A1(): pass

    label('loc_2A1')

    OP_6F(0x0001, 60)

    def _loc_2A8(): pass

    label('loc_2A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 5, 0x1905)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BA',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2C1')

    def _loc_2BA(): pass

    label('loc_2BA')

    OP_6F(0x0002, 60)

    def _loc_2C1(): pass

    label('loc_2C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 6, 0x1906)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D3',
    )

    OP_6F(0x0003, 0)

    Jump('loc_2DA')

    def _loc_2D3(): pass

    label('loc_2D3')

    OP_6F(0x0003, 60)

    def _loc_2DA(): pass

    label('loc_2DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 7, 0x1907)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EC',
    )

    OP_6F(0x0004, 0)

    Jump('loc_2F3')

    def _loc_2EC(): pass

    label('loc_2EC')

    OP_6F(0x0004, 60)

    def _loc_2F3(): pass

    label('loc_2F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0321, 0, 0x1908)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_305',
    )

    OP_6F(0x0005, 0)

    Jump('loc_30C')

    def _loc_305(): pass

    label('loc_305')

    OP_6F(0x0005, 60)

    def _loc_30C(): pass

    label('loc_30C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0321, 1, 0x1909)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31E',
    )

    OP_6F(0x0006, 0)

    Jump('loc_325')

    def _loc_31E(): pass

    label('loc_31E')

    OP_6F(0x0006, 60)

    def _loc_325(): pass

    label('loc_325')

    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 1, 0x1801)),
            Expr.Return,
        ),
        'loc_33D',
    )

    OP_10(0x00, 0x01)
    OP_10(0x01, 0x00)
    OP_10(0x02, 0x00)

    Jump('loc_346')

    def _loc_33D(): pass

    label('loc_33D')

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x01)
    OP_10(0x02, 0x00)

    def _loc_346(): pass

    label('loc_346')

    Return()

# id: 0x0002 offset: 0x347
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x4A, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 4, 0x1904)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_424',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_3BB',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1904)

    Jump('loc_421')

    def _loc_3BB(): pass

    label('loc_3BB')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
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

    def _loc_421(): pass

    label('loc_421')

    Jump('loc_455')

    def _loc_424(): pass

    label('loc_424')

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
    def _loc_455(): pass

    label('loc_455')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x463
@scena.Code('func_03_463')
def func_03_463():
    UnlockAchievement(0x02, 0x4B, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 5, 0x1905)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_540',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_4D7',
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
    OP_A2(0x1905)

    Jump('loc_53D')

    def _loc_4D7(): pass

    label('loc_4D7')

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

    def _loc_53D(): pass

    label('loc_53D')

    Jump('loc_571')

    def _loc_540(): pass

    label('loc_540')

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
    def _loc_571(): pass

    label('loc_571')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x57F
@scena.Code('func_04_57F')
def func_04_57F():
    UnlockAchievement(0x02, 0x4C, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 6, 0x1906)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_65C',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_5F3',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1906)

    Jump('loc_659')

    def _loc_5F3(): pass

    label('loc_5F3')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
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

    def _loc_659(): pass

    label('loc_659')

    Jump('loc_68D')

    def _loc_65C(): pass

    label('loc_65C')

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
    def _loc_68D(): pass

    label('loc_68D')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x69B
@scena.Code('func_05_69B')
def func_05_69B():
    UnlockAchievement(0x02, 0x4D, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 7, 0x1907)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_778',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_70F',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1907)

    Jump('loc_775')

    def _loc_70F(): pass

    label('loc_70F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['全回复药']),
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

    def _loc_775(): pass

    label('loc_775')

    Jump('loc_7A9')

    def _loc_778(): pass

    label('loc_778')

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
    def _loc_7A9(): pass

    label('loc_7A9')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x7B7
@scena.Code('func_06_7B7')
def func_06_7B7():
    UnlockAchievement(0x02, 0x4E, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0321, 0, 0x1908)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_894',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_82B',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1908)

    Jump('loc_891')

    def _loc_82B(): pass

    label('loc_82B')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
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

    def _loc_891(): pass

    label('loc_891')

    Jump('loc_8C5')

    def _loc_894(): pass

    label('loc_894')

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
    def _loc_8C5(): pass

    label('loc_8C5')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x8D3
@scena.Code('func_07_8D3')
def func_07_8D3():
    UnlockAchievement(0x02, 0x4F, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0321, 1, 0x1909)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9B0',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0006, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_947',
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
    OP_A2(0x1909)

    Jump('loc_9AD')

    def _loc_947(): pass

    label('loc_947')

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
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0x00000000)

    def _loc_9AD(): pass

    label('loc_9AD')

    Jump('loc_9E1')

    def _loc_9B0(): pass

    label('loc_9B0')

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
    def _loc_9E1(): pass

    label('loc_9E1')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x9EF
@scena.Code('func_08_9EF')
def func_08_9EF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 3, 0x1803)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A08',
    )

    EventBegin(0x00)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C1304._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_A68')

    def _loc_A08(): pass

    label('loc_A08')

    ChrTalk(
        0x0102,
        (
            '#0020280239V#1030F（好像在吃饭。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280236V（应该暂时不会动，\n',
            '  就这么走过去吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    def _loc_A68(): pass

    label('loc_A68')

    Return()

# id: 0x0009 offset: 0xA69
@scena.Code('func_09_A69')
def func_09_A69():
    EventBegin(0x00)
    SetChrPos(0x0102, -50940, 0, -136720, 0)
    SetChrPos(0x0146, -51350, 0, -138260, 0)
    SetChrPos(0x0129, -50230, 0, -138010, 0)
    SetChrPos(0x012A, -52460, 0, -137530, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020280232V#1033F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280233V#213F#6P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280234V（唔，怎么了？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 180, 500)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020280235V#1031F（啊啊……\n',
            '  看来是在吃饭。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280236V（应该暂时不会动，\n',
            '  就这么走过去吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280237V#210F#6P（嗯，知道了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280238V#490F（赶快走吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1803)
    OP_65(0x06, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0xBEE
@scena.Code('func_0A_BEE')
def func_0A_BEE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 1, 0x1801)),
            Expr.Return,
        ),
        'loc_C01',
    )

    NewScene('ED6_DT21/C1300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_C0A')

    def _loc_C01(): pass

    label('loc_C01')

    NewScene('ED6_DT21/C1301._SN', 100, 0, 0)
    IdleLoop()

    def _loc_C0A(): pass

    label('loc_C0A')

    Return()

# id: 0x000B offset: 0xC0B
@scena.Code('func_0B_C0B')
def func_0B_C0B():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(2320, 1750, -19320, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0008, 7500, 3500, -20200, 270)
    ClearChrFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_0C7A')
    def lambda_0C7A():
        OP_8E(0x0008, 1290, 0, -20200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0C7A)

    ClearMapFlags(0x02000000)
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0008, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0110280343V#272F#5P得以生还的\n',
            '到底是哪边呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280344V#275F呼呼，我也还不够成熟呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0110280345V#276F#5P不过『哈梅尔』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280346V看来只能帮\n',
            '那个吊儿郎当的家伙一次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    ClearChrFlags(0x0000, 0x0080)
    ClearChrFlags(0x0001, 0x0080)
    ClearChrFlags(0x0002, 0x0080)
    ClearChrFlags(0x0003, 0x0080)
    NewScene('ED6_DT21/E0001._SN', 104, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
