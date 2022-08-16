import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1400.x'
    header.mapIndex       = 60
    header.bgm            = 22
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH11170._CH', 'ED6_DT09/CH11170P._CP'),
        ('ED6_DT09/CH11171._CH', 'ED6_DT09/CH11171P._CP'),
        ('ED6_DT09/CH11180._CH', 'ED6_DT09/CH11180P._CP'),
        ('ED6_DT09/CH11181._CH', 'ED6_DT09/CH11181P._CP'),
        ('ED6_DT09/CH11190._CH', 'ED6_DT09/CH11190P._CP'),
        ('ED6_DT09/CH11191._CH', 'ED6_DT09/CH11191P._CP'),
        ('ED6_DT09/CH10170._CH', 'ED6_DT09/CH10170P._CP'),
        ('ED6_DT09/CH10171._CH', 'ED6_DT09/CH10171P._CP'),
        ('ED6_DT09/CH10840._CH', 'ED6_DT09/CH10840P._CP'),
        ('ED6_DT09/CH10841._CH', 'ED6_DT09/CH10841P._CP'),
        ('ED6_DT29/CH12560._CH', 'ED6_DT29/CH12560P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT26/CH20238._CH', 'ED6_DT26/CH20238P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
        ('ED6_DT26/CH20254._CH', 'ED6_DT26/CH20254P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = -42410,
            z                   = 4019,
            y                   = 103940,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '维姆拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '基库',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x192
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -68750,
            z           = 50,
            y           = 92910,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -112800,
            z           = -50,
            y           = 104070,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -86000,
            z           = 2020,
            y           = 104050,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -91980,
            z           = 2080,
            y           = 122080,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -78470,
            z           = 4059,
            y           = 133110,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -61710,
            z           = 4050,
            y           = 112490,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -46460,
            z           = 4080,
            y           = 83320,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x256
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -42410,
            y           = 3500,
            z           = 103940,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -43500,
            y           = 3500,
            z           = 104740,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = -67400,
            y           = 3000,
            z           = 184200,
            range       = -60300,
            dword_10    = 0x00001770,
            dword_14    = 0x0002D2A8,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000A,
        ),
    )

# id: 0x10004 offset: 0x2B6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -78820,
            triggerZ            = 90,
            triggerY            = 98230,
            triggerRange        = 1000,
            actorX              = -78790,
            actorZ              = 1590,
            actorY              = 97650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -85490,
            triggerZ            = -30,
            triggerY            = 115790,
            triggerRange        = 1000,
            actorX              = -85380,
            actorZ              = 1200,
            actorY              = 115700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2FE
@scena.Code('Init')
def Init():
    OP_11(0xFF, 0xFF, 0xFF, 33000, 58000, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_315',
    )

    def _loc_315(): pass

    label('loc_315')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 6, 0x1A26)),
            Expr.Return,
        ),
        'loc_332',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -42100, 4000, 104960, 135)

    def _loc_332(): pass

    label('loc_332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 7, 0x1A27)),
            Expr.Return,
        ),
        'loc_33E',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_33E(): pass

    label('loc_33E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 5, 0x1A25)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_353',
    )

    MapSetFlags(0x10000000)
    Event(0, func_08_1598)

    def _loc_353(): pass

    label('loc_353')

    Return()

# id: 0x0001 offset: 0x354
@scena.Code('func_01_354')
def func_01_354():
    OP_C4(0x00, 0x00000004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 4, 0x1B14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36C',
    )

    OP_6F(0x0002, 0)

    Jump('loc_373')

    def _loc_36C(): pass

    label('loc_36C')

    OP_6F(0x0002, 60)

    def _loc_373(): pass

    label('loc_373')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 5, 0x1B15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_385',
    )

    OP_6F(0x0006, 0)

    Jump('loc_38C')

    def _loc_385(): pass

    label('loc_385')

    OP_6F(0x0006, 60)

    def _loc_38C(): pass

    label('loc_38C')

    ExecExpressionWithValue(
        0x0008,
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
            (Expr.PushLong, 0xB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x24,
        (
            (Expr.PushLong, 0xB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0000, 0x0004)
    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 0, 0x1A10)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3CD',
    )

    ChrClearFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_3CD(): pass

    label('loc_3CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 6, 0x1A26)),
            Expr.Return,
        ),
        'loc_3DE',
    )

    OP_72(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)

    def _loc_3DE(): pass

    label('loc_3DE')

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x3F0
@scena.Code('func_02_3F0')
def func_02_3F0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_405',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3F0')

    def _loc_405(): pass

    label('loc_405')

    Return()

# id: 0x0003 offset: 0x406
@scena.Code('func_03_406')
def func_03_406():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0009,
        (
            '◆没有台词',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x41D
@scena.Code('func_04_41D')
def func_04_41D():
    UnlockAchievement(0x02, 0x0053, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 4, 0x1B14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 30)
    OP_73(0x0002)
    OP_6F(0x0002, 30)
    AddSepith(0x01, 200)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×２００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0362, 4, 0x1B14))

    Jump('loc_4B5')

    def _loc_49B(): pass

    label('loc_49B')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4B5(): pass

    label('loc_4B5')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x4C7
@scena.Code('func_05_4C7')
def func_05_4C7():
    UnlockAchievement(0x02, 0x0054, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 5, 0x1B15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['幸运'], 1)"),
            Expr.Return,
        ),
        'loc_53B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['幸运']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0362, 5, 0x1B15))

    Jump('loc_5A1')

    def _loc_53B(): pass

    label('loc_53B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['幸运']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['幸运']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_5A1(): pass

    label('loc_5A1')

    Jump('loc_5D5')

    def _loc_5A4(): pass

    label('loc_5A4')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_5D5(): pass

    label('loc_5D5')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x5E3
@scena.Code('func_06_5E3')
def func_06_5E3():
    EventBegin(0x01)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
            TxtCtl.Enter,
        ),
    )

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
        32,
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_64C'),
        (0x00000001, 'loc_880'),
        (-1, 'loc_8E8'),
    )

    def _loc_64C(): pass

    label('loc_64C')

    Battle(0x000000BB, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_66D'),
        (0x00000002, 'loc_800'),
        (0x00000001, 'loc_878'),
        (-1, 'loc_87D'),
    )

    def _loc_66D(): pass

    label('loc_66D')

    EventBegin(0x01)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_714',
    )

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
        32,
        0,
        (
            TXT(0x00, '【◇已经消灭了古罗尼山路和琥珀之塔的通缉魔兽】\n'),
            TXT(0x01, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_6FF'),
        (-1, 'loc_714'),
    )

    def _loc_6FF(): pass

    label('loc_6FF')

    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    OP_28(0x00B1, 0x01, 0x0001)
    OP_28(0x00B3, 0x01, 0x0001)

    Jump('loc_714')

    def _loc_714(): pass

    label('loc_714')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 6, 0x1A0E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 7, 0x1A0F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_726',
    )

    Call(0, 0x0007)

    Jump('loc_7FD')

    def _loc_726(): pass

    label('loc_726')

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetPos(0x0000, -40990, 3930, 102060, 315)
    ChrSetPos(0x0001, -40990, 3930, 102060, 315)
    ChrSetPos(0x0002, -40990, 3930, 102060, 315)
    ChrSetPos(0x0003, -40990, 3930, 102060, 315)
    OP_69(0x0000, 0)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了迷雾峡谷的通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    OP_28(0x00B2, 0x01, 0x0001)
    OP_28(0x0093, 0x02, 0x0080)
    OP_28(0x0093, 0x01, 0x0100)
    OP_28(0x0093, 0x01, 0x0200)
    Sleep(400)

    def _loc_7FD(): pass

    label('loc_7FD')

    Jump('loc_87D')

    def _loc_800(): pass

    label('loc_800')

    EventBegin(0x01)
    FadeOut(0, 0, -1)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetPos(0x0000, -40390, 3880, 100330, 315)
    ChrSetPos(0x0001, -40390, 3880, 100330, 315)
    ChrSetPos(0x0002, -40390, 3880, 100330, 315)
    ChrSetPos(0x0003, -40390, 3880, 100330, 315)
    OP_69(0x0000, 0)
    FadeIn(1000, 0)
    OP_0D()

    Jump('loc_87D')

    def _loc_878(): pass

    label('loc_878')

    OP_B4(0x00)

    Jump('loc_87D')

    def _loc_87D(): pass

    label('loc_87D')

    Jump('loc_8E8')

    def _loc_880(): pass

    label('loc_880')

    Fade(500)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetPos(0x0000, -40390, 3880, 100330, 315)
    ChrSetPos(0x0001, -40390, 3880, 100330, 315)
    ChrSetPos(0x0002, -40390, 3880, 100330, 315)
    ChrSetPos(0x0003, -40390, 3880, 100330, 315)
    OP_69(0x0000, 0)
    OP_0D()

    Jump('loc_8E8')

    def _loc_8E8(): pass

    label('loc_8E8')

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x8EB
@scena.Code('func_07_8EB')
def func_07_8EB():
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
        'loc_8FE',
    )

    Call(0, 0x000B)

    def _loc_8FE(): pass

    label('loc_8FE')

    CameraMove(-42350, 4059, 103640, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -41720, 3990, 104460, 225)
    ChrSetPos(0x0106, -43170, 4059, 104220, 135)
    ChrSetPos(0x00F8, -41440, 4030, 102690, 315)
    ChrSetPos(0x00F9, -42900, 4070, 102590, 45)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010300715V#1007F哈～总算是解决了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300716V#1002F不过……\n',
            '这些魔兽的样子似乎很奇怪啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '是哪里和平时不同了呢？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【魔兽变强了】\n'),
            TXT(0x01, '【魔兽变胆怯了】\n'),
            TXT(0x02, '【魔兽非常兴奋】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_AA4'),
        (0x00000001, 'loc_CDD'),
        (0x00000002, 'loc_EF2'),
        (-1, 'loc_1107'),
    )

    def _loc_AA4(): pass

    label('loc_AA4')

    OP_2B(0x0093, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B31',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300717V#072F那也没错……\n',
            '不过更明显的是它们的性情变了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300718V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD4')

    def _loc_B31(): pass

    label('loc_B31')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BBF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300719V#022F那也说的没错……\n',
            '不过更明显的是它们的性情变了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300720V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD4')

    def _loc_BBF(): pass

    label('loc_BBF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C4F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300721V#032F嗯、那也说的不错，\n',
            '不过更明显的是它们的性情变了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300722V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD4')

    def _loc_C4F(): pass

    label('loc_C4F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD4',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300723V#043F那样说也对，\n',
            '不过更明显的是它们的性情变了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300724V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD4(): pass

    label('loc_CD4')

    OP_28(0x0093, 0x01, 0x0400)

    Jump('loc_1107')

    def _loc_CDD(): pass

    label('loc_CDD')

    OP_2B(0x0093, 0x0003)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D66',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300725V#072F啊啊～不管什么样的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300718V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE9')

    def _loc_D66(): pass

    label('loc_D66')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DE8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300727V#022F哎～不管什么样的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300720V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE9')

    def _loc_DE8(): pass

    label('loc_DE8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E6A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300729V#032F嗯，不管什么样的魔兽\n',
            '都好像很奇怪啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300722V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE9')

    def _loc_E6A(): pass

    label('loc_E6A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EE9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300731V#042F是啊，不管什么样的魔兽\n',
            '也都很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300724V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EE9(): pass

    label('loc_EE9')

    OP_28(0x0093, 0x01, 0x1000)

    Jump('loc_1107')

    def _loc_EF2(): pass

    label('loc_EF2')

    OP_2B(0x0093, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F7B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300725V#072F啊啊～不管什么样的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300718V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10FE')

    def _loc_F7B(): pass

    label('loc_F7B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FFD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300727V#022F哎～不管什么样的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300720V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10FE')

    def _loc_FFD(): pass

    label('loc_FFD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_107F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300729V#032F嗯，不管什么样的魔兽\n',
            '都好像很奇怪啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300722V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10FE')

    def _loc_107F(): pass

    label('loc_107F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10FE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300731V#042F是啊，不管什么样的魔兽\n',
            '也都很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300724V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10FE(): pass

    label('loc_10FE')

    OP_28(0x0093, 0x01, 0x0800)

    Jump('loc_1107')

    def _loc_1107(): pass

    label('loc_1107')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1167',
    )

    ChrTalk(
        0x0107,
        (
            '#0070300741V#065F我、我也\n',
            '有那种感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300742V#561F好、好可怕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1284')

    def _loc_1167(): pass

    label('loc_1167')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11C6',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300743V#043F我也……\n',
            '有那种感觉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300744V究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1284')

    def _loc_11C6(): pass

    label('loc_11C6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1225',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300745V#032F我也有\n',
            '同样的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300746V嗯，到底是为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1284')

    def _loc_1225(): pass

    label('loc_1225')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1284',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300747V#026F我也有同感啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300748V#522F嗯……\n',
            '究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1284(): pass

    label('loc_1284')

    ChrTalk(
        0x0106,
        (
            '#0050300749V#057F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300750V#1004F嗯？　怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300751V#555F啊，没什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300752V或许这是\n',
            '某种前兆也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300753V#1020F前兆……\n',
            '难道是『结社』！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300754V#552F这就不得而知了……\n',
            '不过以前也发生过类似的状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300755V魔兽突然就变得\n',
            '仓惶不安…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300756V之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300757V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300758V#1004F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1454',
    )

    ChrTalk(
        0x0107,
        (
            '#0070300759V#063F阿加特哥哥……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1454(): pass

    label('loc_1454')

    ChrTalk(
        0x0106,
        (
            '#0050300760V#053F算了，目前就这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300761V#057F不管怎么说，动物的直觉\n',
            '有时候比人还要更加敏锐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300762V我们也必须准备应付\n',
            '随时可能出现的特殊情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300763V#1002F嗯……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300764V那么…\n',
            '我们暂时先返回协会吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300765V#050F啊啊～就这样办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    OP_28(0x00B2, 0x01, 0x0001)
    OP_28(0x0093, 0x02, 0x0080)
    OP_28(0x0093, 0x01, 0x0100)
    OP_28(0x0093, 0x01, 0x0200)
    OP_28(0x0093, 0x01, 0x2000)

    Return()

# id: 0x0008 offset: 0x1598
@scena.Code('func_08_1598')
def func_08_1598():
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
        'loc_15AF',
    )

    Call(0, 0x000C)
    Call(0, 0x000D)

    def _loc_15AF(): pass

    label('loc_15AF')

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    CameraMove(-69550, -70, 106980, 0)
    OP_67(0, 13560, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(9000, 0)
    OP_6E(342, 0)
    ChrSetPos(0x0101, -43050, 40, 15070, 0)
    ChrSetPos(0x0106, -44190, -50, 15060, 0)
    ChrSetPos(0x0107, -44150, -20, 13590, 0)
    ChrSetPos(0x00F9, -43040, 50, 13500, 0)

    @scena.Lambda('lambda_1659')
    def lambda_1659():
        CameraMove(-44930, -70, 26000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1659)

    @scena.Lambda('lambda_1671')
    def lambda_1671():
        OP_6C(33000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1671)

    OP_C8(0x0200, 0x0046, 'C_PLAC13._CH', 0x01, 0x07D0)
    ShowPlaceName('迷雾峡谷')
    FadeIn(2000, 0)
    OP_0D()
    Sleep(5000)

    @scena.Lambda('lambda_16AF')
    def lambda_16AF():
        ChrWalkTo(0x00FE, -42820, 80, 24620, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_16AF)

    Sleep(200)

    @scena.Lambda('lambda_16CF')
    def lambda_16CF():
        ChrWalkTo(0x00FE, -44060, 70, 24570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_16CF)

    @scena.Lambda('lambda_16EA')
    def lambda_16EA():
        ChrWalkTo(0x00FE, -43760, -90, 23210, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_16EA)

    Sleep(200)

    @scena.Lambda('lambda_170A')
    def lambda_170A():
        ChrWalkTo(0x00FE, -42550, 20, 23340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_170A)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    Fade(1000)
    CameraMove(-43060, 0, 25330, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitForThreadExit(0x00F9, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010310842V#1006F#2P那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310843V先去峡谷东侧的\n',
            '山中小屋吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310844V#050F#5P啊，快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    SetScenaFlags(ScenaFlag(0x0344, 5, 0x1A25))
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x1816
@scena.Code('func_09_1816')
def func_09_1816():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 6, 0x1A26)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 7, 0x1A27)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1823',
    )

    Return()

    def _loc_1823(): pass

    label('loc_1823')

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
        'loc_183A',
    )

    Call(0, 0x000C)
    Call(0, 0x000D)

    def _loc_183A(): pass

    label('loc_183A')

    Fade(1000)
    CameraMove(-41580, 3920, 104490, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(27000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -41200, 4019, 103610, 315)
    ChrSetPos(0x0106, -42230, 4090, 103100, 315)
    ChrSetPos(0x0107, -41860, 4010, 101920, 315)
    ChrSetPos(0x00F9, -40840, 3940, 102310, 315)

    @scena.Lambda('lambda_18C6')
    def lambda_18C6():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_18C6')

    DispatchAsync2(0x0101, 0x0001, lambda_18C6)

    @scena.Lambda('lambda_18D7')
    def lambda_18D7():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_18D7')

    DispatchAsync2(0x0106, 0x0001, lambda_18D7)

    @scena.Lambda('lambda_18E8')
    def lambda_18E8():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_18E8')

    DispatchAsync2(0x0107, 0x0001, lambda_18E8)

    @scena.Lambda('lambda_18F9')
    def lambda_18F9():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_18F9')

    DispatchAsync2(0x00F9, 0x0001, lambda_18F9)

    ChrSetDirection(0x0009, 180, 0)
    OP_4A(0x0009, 255)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#3500310942V#5P……你们\n',
            '总算是来到这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310943V#052F大叔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310944V#1011F是不是…渡过\n',
            '那座桥的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3500310945V#5P嗯，一直向前走\n',
            '就可以看到一座巨大的岩山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3500310946V#5P那里面是中空的，\n',
            '你们只要一直往内部前进\n',
            '就可以爬到最上层了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3500310947V#5P龙应该就栖息在那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310019V#1006F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310949V#051F谢谢你了，大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3500310950V#5P那么……\n',
            '我这就要回小屋去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3500310951V#5P对了，岩山的空洞中应该\n',
            '有很多危险的魔兽在游荡着，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3500310952V#5P如果觉得危险的话\n',
            '最好还是马上回头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3500310953V#5P我的小屋随时可以供你们休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310954V#1018F嗯，谢谢您了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310955V#051F我们会小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0009, -43380, 4120, 102770, 2000, 0x00)
    ChrWalkTo(0x0009, -36810, 3950, 94230, 2000, 0x00)
    ChrSetFlags(0x0009, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0106, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F9, 0x01)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x0344, 7, 0x1A27))
    OP_28(0x0096, 0x01, 0x0100)
    OP_28(0x0096, 0x01, 0x0200)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x1C16
@scena.Code('func_0A_1C16')
def func_0A_1C16():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 7, 0x1A27)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 0, 0x1A28)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1C23',
    )

    Return()

    def _loc_1C23(): pass

    label('loc_1C23')

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
        'loc_1C3A',
    )

    Call(0, 0x000C)
    Call(0, 0x000D)

    def _loc_1C3A(): pass

    label('loc_1C3A')

    Fade(1000)
    CameraMove(-63540, 4100, 187850, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(34000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -64340, 4050, 187170, 0)
    ChrSetPos(0x0106, -63060, 4019, 187180, 0)
    ChrSetPos(0x0107, -62880, 4000, 186090, 0)
    ChrSetPos(0x00F9, -64400, 4090, 185850, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010310956V#1002F这里就是巨龙栖息的岩山……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070310957V#062F呜啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310958V#051F嘿，看来要拿出\n',
            '全部的干劲了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DB5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030310959V#023F#6P先等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310960V#020F现在先和『埃尔赛尤』\n',
            '进行联络比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F15')

    def _loc_1DB5(): pass

    label('loc_1DB5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E2A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060310961V#044F#6P啊，请等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310962V#040F现在还是先和『埃尔赛尤』\n',
            '联络一下比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F15')

    def _loc_1E2A(): pass

    label('loc_1E2A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EA3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040310963V#035F#6P喂，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310964V#030F我想现在还是先和『埃尔赛尤』\n',
            '进行联络比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F15')

    def _loc_1EA3(): pass

    label('loc_1EA3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F15',
    )

    ChrTalk(
        0x0108,
        (
            '#0080310965V#073F#6P啊，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310966V#070F现在还是先和『埃尔赛尤』\n',
            '联络一下比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F15(): pass

    label('loc_1F15')

    ChrTurnDirection(0x0101, 0x00F9, 400)

    ChrTalk(
        0x0101,
        (
            '#0010310967V#1006F#5P嗯，说的也对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2389',
    )

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔把当前的情况记录了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    @scena.Lambda('lambda_1F9F')
    def lambda_1F9F():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_1F9F')

    DispatchAsync2(0x0106, 0x0001, lambda_1F9F)

    @scena.Lambda('lambda_1FB0')
    def lambda_1FB0():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_1FB0')

    DispatchAsync2(0x0107, 0x0001, lambda_1FB0)

    @scena.Lambda('lambda_1FC1')
    def lambda_1FC1():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_1FC1')

    DispatchAsync2(0x00F9, 0x0001, lambda_1FC1)

    @scena.Lambda('lambda_1FD2')
    def lambda_1FD2():
        CameraMove(-65560, 4059, 187340, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FD2)

    @scena.Lambda('lambda_1FEA')
    def lambda_1FEA():
        OP_67(0, 9500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1FEA)

    ChrWalkTo(0x0101, -65920, 4059, 186810, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0106, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F9, 0x01)

    @scena.Lambda('lambda_2027')
    def lambda_2027():
        ChrSetDirection(0x0107, 270, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2027)

    @scena.Lambda('lambda_2035')
    def lambda_2035():
        ChrSetDirection(0x00F9, 270, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2035)

    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010310968V#1005F#5P#3S基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    PlaySE(407, 0x00, 0x64)
    Sleep(1000)

    CameraMove(-68540, 5590, 186890, 1500)
    ChrSetPos(0x000A, -78030, 10000, 185300, 0)
    ChrSetChipByIndex(0x000A, 12)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0040)
    CreateThread(0x000A, 0x00, 0x00, func_02_3F0)
    ChrClearFlags(0x000A, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_20BD')
    def lambda_20BD():
        CameraMove(-65560, 4059, 187340, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20BD)

    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_20DA')
    def lambda_20DA():
        ChrWalkTo(0x000A, -66460, 6000, 187300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_20DA)

    Sleep(2400)

    ChrSetFlags(0x000A, 0x0001)
    WaitForThreadExit(0x000A, 0x0003)
    ChrSetChipByIndex(0x000A, 15)
    ChrSetDirection(0x000A, 180, 100)
    ChrMoveTo(0x000A, -66090, 4200, 187020, 1000, 0x00)
    Fade(250)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetDirection(0x0101, 225, 0)
    ChrSetChipByIndex(0x0101, 13)
    ChrSetSubChip(0x0101, 5)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0440310969V#311F#6P啾啾⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310970V#1016F#5P啊哈哈，你果然\n',
            '一叫就来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070310971V#061F基库，谢谢啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310972V#551F呼～这只鸟还是\n',
            '那样让人感到不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔把纸条绑在了基库的脚上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010310973V#1006F#5P那么，基库。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310974V可以拜托你跟『埃尔赛尤』\n',
            '取得联络吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0440310975V#310F#6P啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(140, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetPos(0x000A, -66090, 4200, 187020, 180)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x000A, 15)

    @scena.Lambda('lambda_22E9')
    def lambda_22E9():
        ChrSetDirection(0x0101, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22E9)

    ChrMoveTo(0x000A, -66460, 6000, 187300, 2000, 0x00)
    ChrSetDirection(0x000A, 270, 100)
    ChrSetChipByIndex(0x000A, 12)

    @scena.Lambda('lambda_2317')
    def lambda_2317():
        CameraMove(-68540, 5590, 186890, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2317)

    @scena.Lambda('lambda_232F')
    def lambda_232F():
        ChrWalkTo(0x000A, -78460, 10000, 185300, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_232F)

    Sleep(100)

    ChrClearFlags(0x000A, 0x0001)
    WaitForThreadExit(0x000A, 0x0003)
    Sleep(1000)

    ChrSetFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_2363')
    def lambda_2363():
        CameraMove(-63540, 4100, 187850, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2363)

    Sleep(1000)

    ChrSetDirection(0x0101, 90, 400)
    WaitForThreadExit(0x0101, 0x0002)

    Jump('loc_27D9')

    def _loc_2389(): pass

    label('loc_2389')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '科洛丝把当前的情况记录了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    @scena.Lambda('lambda_23D3')
    def lambda_23D3():
        ChrTurnDirection(0x00FE, 0x0105, 400)
        Yield()

        Jump('lambda_23D3')

    DispatchAsync2(0x0101, 0x0001, lambda_23D3)

    @scena.Lambda('lambda_23E4')
    def lambda_23E4():
        ChrTurnDirection(0x00FE, 0x0105, 400)
        Yield()

        Jump('lambda_23E4')

    DispatchAsync2(0x0106, 0x0001, lambda_23E4)

    @scena.Lambda('lambda_23F5')
    def lambda_23F5():
        ChrTurnDirection(0x00FE, 0x0105, 400)
        Yield()

        Jump('lambda_23F5')

    DispatchAsync2(0x0107, 0x0001, lambda_23F5)

    @scena.Lambda('lambda_2406')
    def lambda_2406():
        CameraMove(-65560, 4059, 187340, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2406)

    @scena.Lambda('lambda_241E')
    def lambda_241E():
        OP_67(0, 9500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_241E)

    ChrWalkTo(0x0105, -65920, 4059, 186810, 2000, 0x00)

    @scena.Lambda('lambda_244A')
    def lambda_244A():
        ChrSetDirection(0x0105, 270, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_244A)

    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0106, 0x01)
    TerminateThread(0x0107, 0x01)

    @scena.Lambda('lambda_2469')
    def lambda_2469():
        ChrSetDirection(0x0107, 270, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2469)

    @scena.Lambda('lambda_2477')
    def lambda_2477():
        ChrSetDirection(0x0101, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2477)

    Sleep(300)

    ChrTalk(
        0x0105,
        (
            '#0060310976V#042F#5P#3S基库，过来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(407, 0x00, 0x64)
    Sleep(1000)

    CameraMove(-68540, 5590, 186890, 1500)
    ChrSetPos(0x000A, -78030, 10000, 185300, 0)
    ChrSetChipByIndex(0x000A, 12)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0040)
    CreateThread(0x000A, 0x00, 0x00, func_02_3F0)
    ChrClearFlags(0x000A, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_24FF')
    def lambda_24FF():
        CameraMove(-65560, 4059, 187340, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_24FF)

    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_251C')
    def lambda_251C():
        ChrWalkTo(0x000A, -66460, 6000, 187300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_251C)

    Sleep(2400)

    ChrSetFlags(0x000A, 0x0001)
    WaitForThreadExit(0x000A, 0x0003)
    ChrSetChipByIndex(0x000A, 15)

    @scena.Lambda('lambda_254B')
    def lambda_254B():
        ChrSetDirection(0x000A, 180, 100)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_254B)

    @scena.Lambda('lambda_2559')
    def lambda_2559():
        ChrSetDirection(0x0105, 225, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2559)

    ChrSetFlags(0x0105, 0x0020)
    ChrSetChipByIndex(0x0105, 14)
    ChrSetSubChip(0x0105, 2)
    WaitForThreadExit(0x000A, 0x0003)
    ChrMoveTo(0x000A, -66090, 4200, 187020, 1000, 0x00)
    Fade(250)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0105, 14)
    ChrSetSubChip(0x0105, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0440310969V#311F#6P啾啾⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060310978V#048F#5P呵呵，辛苦你啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310979V#1001F谢谢了，基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310972V#551F呼～这只鸟还是\n',
            '那样让人感到不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '科洛丝把纸条绑在了基库的脚上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0105,
        (
            '#0060310981V#042F#5P那么，基库。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310982V和『埃尔赛尤』的联络\n',
            '一切就拜托你了哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0440310975V#310F#6P啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(140, 0x00, 0x64)
    ChrSetChipByIndex(0x0105, 65535)
    ChrClearFlags(0x0105, 0x0020)
    ChrSetPos(0x000A, -66090, 4200, 187020, 180)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x000A, 15)

    @scena.Lambda('lambda_273C')
    def lambda_273C():
        ChrSetDirection(0x0105, 270, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_273C)

    ChrMoveTo(0x000A, -66460, 6000, 187300, 2000, 0x00)
    ChrSetDirection(0x000A, 270, 100)
    ChrSetChipByIndex(0x000A, 12)

    @scena.Lambda('lambda_276A')
    def lambda_276A():
        CameraMove(-68540, 5590, 186890, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_276A)

    @scena.Lambda('lambda_2782')
    def lambda_2782():
        ChrWalkTo(0x000A, -78460, 10000, 185300, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_2782)

    Sleep(100)

    ChrClearFlags(0x000A, 0x0001)
    WaitForThreadExit(0x000A, 0x0003)
    Sleep(1000)

    ChrSetFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_27B6')
    def lambda_27B6():
        CameraMove(-63540, 4100, 187850, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_27B6)

    Sleep(1000)

    ChrSetDirection(0x0105, 90, 400)
    WaitForThreadExit(0x0101, 0x0002)

    def _loc_27D9(): pass

    label('loc_27D9')

    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2823',
    )

    ChrTalk(
        0x0105,
        (
            '#0060310984V#047F那么……\n',
            '大家已经准备好了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28EF')

    def _loc_2823(): pass

    label('loc_2823')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2864',
    )

    ChrTalk(
        0x0103,
        (
            '#0030310985V#026F那么……\n',
            '已经准备好了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28EF')

    def _loc_2864(): pass

    label('loc_2864')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28AB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040310986V#035F那么……\n',
            '想必大家已经准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28EF')

    def _loc_28AB(): pass

    label('loc_28AB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28EF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080310987V#074F那么……\n',
            '想必大家已经准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28EF(): pass

    label('loc_28EF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_293A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010310988V#1002F#2P嗯……\n',
            '打起精神来，继续前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2974')

    def _loc_293A(): pass

    label('loc_293A')

    ChrTalk(
        0x0101,
        (
            '#0010310989V#1002F#5P嗯……\n',
            '打起精神来，继续前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2974(): pass

    label('loc_2974')

    ChrTalk(
        0x0107,
        (
            '#0070310990V#062F#2P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310991V#054F#2P噢噢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-63660, 4000, 183220, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -63660, 4000, 183220, 0)
    ChrSetPos(0x0001, -63660, 4000, 183220, 0)
    ChrSetPos(0x0002, -63660, 4000, 183220, 0)
    ChrSetPos(0x0003, -63660, 4000, 183220, 0)
    OP_69(0x0000, 0)
    SetScenaFlags(ScenaFlag(0x0345, 0, 0x1A28))
    OP_28(0x0096, 0x01, 0x0400)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x2A5F
@scena.Code('func_0B_2A5F')
def func_0B_2A5F():
    FadeOut(0, 0, -1)
    CameraMove(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_2B16'),
        (0x00000001, 'loc_2B1C'),
        (-1, 'loc_2B22'),
    )

    def _loc_2B16(): pass

    label('loc_2B16')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_2B22')

    def _loc_2B1C(): pass

    label('loc_2B1C')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_2B22')

    def _loc_2B22(): pass

    label('loc_2B22')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x000C offset: 0x2B5E
@scena.Code('func_0C_2B5E')
def func_0C_2B5E():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_2BDB'),
        (0x00000001, 'loc_2BE1'),
        (-1, 'loc_2BE7'),
    )

    def _loc_2BDB(): pass

    label('loc_2BDB')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_2BE7')

    def _loc_2BE1(): pass

    label('loc_2BE1')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_2BE7')

    def _loc_2BE7(): pass

    label('loc_2BE7')

    Return()

# id: 0x000D offset: 0x2BE8
@scena.Code('func_0D_2BE8')
def func_0D_2BE8():
    MapClearFlags(0x00000001)
    CameraMove(97010, 0, 95840, 0)
    FadeIn(0, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
