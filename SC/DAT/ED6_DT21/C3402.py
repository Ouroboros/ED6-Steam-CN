import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3402   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ' '),
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
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3402.x'
    header.mapIndex       = 1
    header.bgm            = 125
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x9FB
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
        ('ED6_DT29/CH12110._CH', 'ED6_DT29/CH12110P._CP'),
        ('ED6_DT29/CH12111._CH', 'ED6_DT29/CH12111P._CP'),
        ('ED6_DT29/CH12410._CH', 'ED6_DT29/CH12410P._CP'),
        ('ED6_DT29/CH12411._CH', 'ED6_DT29/CH12411P._CP'),
        ('ED6_DT29/CH12250._CH', 'ED6_DT29/CH12250P._CP'),
        ('ED6_DT29/CH12251._CH', 'ED6_DT29/CH12251P._CP'),
        ('ED6_DT29/CH12130._CH', 'ED6_DT29/CH12130P._CP'),
        ('ED6_DT29/CH12131._CH', 'ED6_DT29/CH12131P._CP'),
        ('ED6_DT09/CH10130._CH', 'ED6_DT09/CH10130P._CP'),
        ('ED6_DT09/CH10131._CH', 'ED6_DT09/CH10131P._CP'),
        ('ED6_DT09/CH10750._CH', 'ED6_DT09/CH10750P._CP'),
        ('ED6_DT09/CH10751._CH', 'ED6_DT09/CH10751P._CP'),
        ('ED6_DT29/CH12270._CH', 'ED6_DT29/CH12270P._CP'),
        ('ED6_DT29/CH12271._CH', 'ED6_DT29/CH12271P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0049,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -21480,
            z           = 0,
            y           = 22770,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -3360,
            z           = 0,
            y           = 13070,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6390,
            z           = 0,
            y           = -12560,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -34010,
            z           = 0,
            y           = -19450,
            word_0C     = 0x002D,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 57480,
            z           = 0,
            y           = -19510,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 28530,
            z           = 0,
            y           = 43350,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 35840,
            z           = 0,
            y           = 38570,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03B2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1FE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1FE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -59190,
            triggerZ            = 0,
            triggerY            = 15820,
            triggerRange        = 1000,
            actorX              = -59910,
            actorZ              = 0,
            actorY              = 16200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 37640,
            triggerZ            = 0,
            triggerY            = 45540,
            triggerRange        = 1000,
            actorX              = 37820,
            actorZ              = 0,
            actorY              = 46220,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60380,
            triggerZ            = 0,
            triggerY            = -16890,
            triggerRange        = 1000,
            actorX              = 61110,
            actorZ              = 0,
            actorY              = -16820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -11940,
            triggerZ            = 0,
            triggerY            = -15660,
            triggerRange        = 1000,
            actorX              = -11860,
            actorZ              = 0,
            actorY              = -16490,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x28E
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x28F
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 2, 0x1562)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A1',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2A8')

    def _loc_2A1(): pass

    label('loc_2A1')

    OP_6F(0x0000, 60)

    def _loc_2A8(): pass

    label('loc_2A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 4, 0x1564)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BA',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2C1')

    def _loc_2BA(): pass

    label('loc_2BA')

    OP_6F(0x0001, 60)

    def _loc_2C1(): pass

    label('loc_2C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 6, 0x1566)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D3',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2DA')

    def _loc_2D3(): pass

    label('loc_2D3')

    OP_6F(0x0002, 60)

    def _loc_2DA(): pass

    label('loc_2DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 7, 0x1567)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EC',
    )

    OP_6F(0x0003, 0)

    Jump('loc_2F3')

    def _loc_2EC(): pass

    label('loc_2EC')

    OP_6F(0x0003, 60)

    def _loc_2F3(): pass

    label('loc_2F3')

    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_328',
    )

    OP_82(0x80, 0x02)
    OP_82(0x81, 0x02)
    OP_82(0x82, 0x02)
    OP_82(0x83, 0x02)
    OP_82(0x84, 0x02)
    OP_82(0x85, 0x02)
    OP_82(0x86, 0x02)
    OP_82(0x87, 0x02)
    OP_82(0x88, 0x02)
    OP_22(0x01C7, 0x00, 0x64)

    Jump('loc_334')

    def _loc_328(): pass

    label('loc_328')

    CreateThread(0x0008, 0x00, 0x00, 0x0006)
    OP_22(0x010B, 0x00, 0x64)

    def _loc_334(): pass

    label('loc_334')

    Return()

# id: 0x0002 offset: 0x335
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xC0, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 2, 0x1562)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_412',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['蓝色猿羊绒'], 1)"),
            Expr.Return,
        ),
        'loc_3A9',
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
    OP_A2(0x1562)

    Jump('loc_40F')

    def _loc_3A9(): pass

    label('loc_3A9')

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
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_40F(): pass

    label('loc_40F')

    Jump('loc_443')

    def _loc_412(): pass

    label('loc_412')

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
    def _loc_443(): pass

    label('loc_443')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x451
@scena.Code('func_03_451')
def func_03_451():
    UnlockAchievement(0x02, 0xC1, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 4, 0x1564)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['双子星'], 1)"),
            Expr.Return,
        ),
        'loc_4C5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['双子星']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1564)

    Jump('loc_52B')

    def _loc_4C5(): pass

    label('loc_4C5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['双子星']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['双子星']),
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

    def _loc_52B(): pass

    label('loc_52B')

    Jump('loc_55F')

    def _loc_52E(): pass

    label('loc_52E')

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
    def _loc_55F(): pass

    label('loc_55F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x56D
@scena.Code('func_04_56D')
def func_04_56D():
    UnlockAchievement(0x02, 0xC2, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 6, 0x1566)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_64A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['七色不可思议玉'], 1)"),
            Expr.Return,
        ),
        'loc_5E1',
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
    OP_A2(0x1566)

    Jump('loc_647')

    def _loc_5E1(): pass

    label('loc_5E1')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_647(): pass

    label('loc_647')

    Jump('loc_67B')

    def _loc_64A(): pass

    label('loc_64A')

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
    def _loc_67B(): pass

    label('loc_67B')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6D3',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0030)"),
            Expr.Return,
        ),
        'loc_69A',
    )

    Jump('loc_6D3')

    def _loc_69A(): pass

    label('loc_69A')

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

    def _loc_6D3(): pass

    label('loc_6D3')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6DC
@scena.Code('func_05_6DC')
def func_05_6DC():
    UnlockAchievement(0x02, 0xC3, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02AC, 7, 0x1567)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7B9',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_750',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1567)

    Jump('loc_7B6')

    def _loc_750(): pass

    label('loc_750')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
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

    def _loc_7B6(): pass

    label('loc_7B6')

    Jump('loc_7EA')

    def _loc_7B9(): pass

    label('loc_7B9')

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
    def _loc_7EA(): pass

    label('loc_7EA')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x7F8
@scena.Code('func_06_7F8')
def func_06_7F8():
    Call(0, 0x0007)
    CreateThread(0x0008, 0x03, 0x00, 0x0008)
    PlayEffect(0x9A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9A, 0x01, 0x0000006E)
    Call(0, 0x0007)
    PlayEffect(0x9B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9B, 0x01, 0x0000006E)
    Call(0, 0x0007)
    PlayEffect(0x9C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9C, 0x01, 0x0000006E)
    Call(0, 0x0007)
    PlayEffect(0x9D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9D, 0x01, 0x0000006E)
    Call(0, 0x0007)
    PlayEffect(0x9E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9E, 0x01, 0x0000006E)
    Call(0, 0x0007)
    PlayEffect(0x9F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C1(0x9F, 0x01, 0x0000006E)

    Return()

# id: 0x0007 offset: 0x980
@scena.Code('func_07_980')
def func_07_980():
    Switch(
        (
            Expr.Rand,
            (Expr.PushLong, 0x5),
            Expr.Mod,
            Expr.Return,
        ),
        (0x00000000, 'loc_9A1'),
        (0x00000001, 'loc_9A9'),
        (0x00000002, 'loc_9B1'),
        (0x00000003, 'loc_9B9'),
        (0x00000004, 'loc_9C1'),
        (-1, 'loc_9C9'),
    )

    def _loc_9A1(): pass

    label('loc_9A1')

    Sleep(500)

    Jump('loc_9D1')

    def _loc_9A9(): pass

    label('loc_9A9')

    Sleep(1000)

    Jump('loc_9D1')

    def _loc_9B1(): pass

    label('loc_9B1')

    Sleep(1500)

    Jump('loc_9D1')

    def _loc_9B9(): pass

    label('loc_9B9')

    Sleep(2000)

    Jump('loc_9D1')

    def _loc_9C1(): pass

    label('loc_9C1')

    Sleep(2500)

    Jump('loc_9D1')

    def _loc_9C9(): pass

    label('loc_9C9')

    Sleep(3000)

    Jump('loc_9D1')

    def _loc_9D1(): pass

    label('loc_9D1')

    Return()

# id: 0x0008 offset: 0x9D2
@scena.Code('func_08_9D2')
def func_08_9D2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9E8',
    )

    OP_22(0x010D, 0x00, 0x64)
    Sleep(7000)

    Jump('func_08_9D2')

    def _loc_9E8(): pass

    label('loc_9E8')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
