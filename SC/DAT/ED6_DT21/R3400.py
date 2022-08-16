import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3400.x'
    header.mapIndex       = 1
    header.bgm            = 30
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
        ('ED6_DT09/CH10130._CH', 'ED6_DT09/CH10130P._CP'),
        ('ED6_DT09/CH10131._CH', 'ED6_DT09/CH10131P._CP'),
        ('ED6_DT09/CH10750._CH', 'ED6_DT09/CH10750P._CP'),
        ('ED6_DT09/CH10751._CH', 'ED6_DT09/CH10751P._CP'),
        ('ED6_DT09/CH10760._CH', 'ED6_DT09/CH10760P._CP'),
        ('ED6_DT09/CH10761._CH', 'ED6_DT09/CH10761P._CP'),
        ('ED6_DT09/CH10770._CH', 'ED6_DT09/CH10770P._CP'),
        ('ED6_DT09/CH10771._CH', 'ED6_DT09/CH10771P._CP'),
        ('ED6_DT29/CH12410._CH', 'ED6_DT29/CH12410P._CP'),
        ('ED6_DT29/CH12411._CH', 'ED6_DT29/CH12411P._CP'),
        ('ED6_DT09/CH10500._CH', 'ED6_DT09/CH10500P._CP'),
        ('ED6_DT09/CH10501._CH', 'ED6_DT09/CH10501P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾尔·雷登关所方向',
            x                   = -26110,
            z                   = -20,
            y                   = -38940,
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
            name                = '蔡斯方向',
            x                   = 189780,
            z                   = -20,
            y                   = -27490,
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
            name                = '巨鲸蛙',
            x                   = 47000,
            z                   = 0,
            y                   = -25210,
            direction           = 89,
            word_0E             = 10,
            dword_10            = 655360,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 45900,
            z           = 20,
            y           = -46160,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 40140,
            z           = -10,
            y           = -13510,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 121900,
            z           = -40,
            y           = -57020,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 115250,
            z           = 10,
            y           = -35350,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 146080,
            z           = -30,
            y           = -31900,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1F6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -15540,
            y           = 0,
            z           = -43640,
            range       = -12240,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF79F0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 47000,
            y           = -1000,
            z           = -25210,
            range       = 3000,
            dword_10    = 0x00000C80,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10004 offset: 0x236
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 19790,
            triggerZ            = 0,
            triggerY            = -14460,
            triggerRange        = 1000,
            actorX              = 19250,
            actorZ              = 10,
            actorY              = -15050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 55120,
            triggerZ            = -70,
            triggerY            = 8740,
            triggerRange        = 1000,
            actorX              = 55870,
            actorZ              = -70,
            actorY              = 8740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 19690,
            triggerZ            = -90,
            triggerY            = 11550,
            triggerRange        = 1000,
            actorX              = 19240,
            actorZ              = -90,
            actorY              = 11060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 124260,
            triggerZ            = -30,
            triggerY            = -53650,
            triggerRange        = 1000,
            actorX              = 124760,
            actorZ              = -30,
            actorY              = -53160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2C6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 1, 0x2081)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 2, 0x2082)),
            Expr.Return,
        ),
        'loc_2E7',
    )

    SetScenaFlags(ScenaFlag(0x0410, 1, 0x2081))

    Jump('loc_2FE')

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.Eval, "OP_40(0x0150, 0x02)"),
            Expr.Return,
        ),
        'loc_2F7',
    )

    Event(0, func_0A_E91)

    Jump('loc_2FB')

    def _loc_2F7(): pass

    label('loc_2F7')

    Event(0, func_09_AA3)

    def _loc_2FB(): pass

    label('loc_2FB')

    SetScenaFlags(ScenaFlag(0x0410, 1, 0x2081))

    def _loc_2FE(): pass

    label('loc_2FE')

    Return()

# id: 0x0001 offset: 0x2FF
@scena.Code('func_01_2FF')
def func_01_2FF():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A4',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_72(0x0012, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_79(0x05, 0x0002)
    OP_79(0x06, 0x0002)
    OP_79(0x07, 0x0002)
    OP_79(0x08, 0x0002)
    OP_79(0x09, 0x0002)
    OP_79(0x0A, 0x0002)
    OP_79(0x0B, 0x0002)
    OP_79(0x0C, 0x0002)
    OP_79(0x0D, 0x0002)
    OP_79(0x0F, 0x0002)
    OP_79(0x10, 0x0002)
    OP_7B()
    OP_C4(0x00, 0x00000001)
    OP_78(0x00, 0x00, 0x00)

    Jump('loc_3A4')

    def _loc_3A4(): pass

    label('loc_3A4')

    OP_16(0x02, 4000, -45000, -151000, 2293815)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 0, 0x1520)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C8',
    )

    OP_6F(0x000E, 0)

    Jump('loc_3CF')

    def _loc_3C8(): pass

    label('loc_3C8')

    OP_6F(0x000E, 60)

    def _loc_3CF(): pass

    label('loc_3CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 1, 0x1521)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E1',
    )

    OP_6F(0x000F, 0)

    Jump('loc_3E8')

    def _loc_3E1(): pass

    label('loc_3E1')

    OP_6F(0x000F, 60)

    def _loc_3E8(): pass

    label('loc_3E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 2, 0x1522)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FA',
    )

    OP_6F(0x0010, 0)

    Jump('loc_401')

    def _loc_3FA(): pass

    label('loc_3FA')

    OP_6F(0x0010, 60)

    def _loc_401(): pass

    label('loc_401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 4, 0x1524)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_413',
    )

    OP_6F(0x0011, 0)

    Jump('loc_41A')

    def _loc_413(): pass

    label('loc_413')

    OP_6F(0x0011, 60)

    def _loc_41A(): pass

    label('loc_41A')

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
        0x000A,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_44E',
    )

    ChrSetFlags(0x000A, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)

    Jump('loc_460')

    def _loc_44E(): pass

    label('loc_44E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x029F, 2, 0x14FA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_460',
    )

    ChrClearFlags(0x000A, 0x0080)
    OP_B2(0x01, 0x01, 0x0080)

    def _loc_460(): pass

    label('loc_460')

    Return()

# id: 0x0002 offset: 0x461
@scena.Code('func_02_461')
def func_02_461():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_476',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_461')

    def _loc_476(): pass

    label('loc_476')

    Return()

# id: 0x0003 offset: 0x477
@scena.Code('func_03_477')
def func_03_477():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x029F, 2, 0x14FA)),
            Expr.Return,
        ),
        'loc_47F',
    )

    Return()

    def _loc_47F(): pass

    label('loc_47F')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
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
        (0x00000001, 'loc_564'),
        (-1, 'loc_587'),
    )

    def _loc_564(): pass

    label('loc_564')

    Fade(500)
    OP_89(0x0000, 53120, 0, -24940, 270)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_587(): pass

    label('loc_587')

    Battle(0x00000EE1, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 53120, 0, -24940, 270)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_5C0'),
        (0x00000001, 'loc_5C3'),
        (-1, 'loc_5C6'),
    )

    def _loc_5C0(): pass

    label('loc_5C0')

    EventEnd(0x00)

    Return()

    def _loc_5C3(): pass

    label('loc_5C3')

    OP_B4(0x00)

    Return()

    def _loc_5C6(): pass

    label('loc_5C6')

    EventBegin(0x01)
    ChrSetFlags(0x000A, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x029F, 2, 0x14FA))
    OP_28(0x00A5, 0x04, 0x10)
    OP_28(0x00A5, 0x04, 0x02)
    OP_28(0x00A5, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x632
@scena.Code('func_04_632')
def func_04_632():
    UnlockAchievement(0x02, 0x01F6, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 0, 0x1520)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_70F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000E, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_6A6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x02A4, 0, 0x1520))

    Jump('loc_70C')

    def _loc_6A6(): pass

    label('loc_6A6')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000E, 60)
    OP_70(0x000E, 0)

    def _loc_70C(): pass

    label('loc_70C')

    Jump('loc_740')

    def _loc_70F(): pass

    label('loc_70F')

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
    def _loc_740(): pass

    label('loc_740')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x74E
@scena.Code('func_05_74E')
def func_05_74E():
    UnlockAchievement(0x02, 0x01F7, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 1, 0x1521)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_82B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000F, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_7C2',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x02A4, 1, 0x1521))

    Jump('loc_828')

    def _loc_7C2(): pass

    label('loc_7C2')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 0)

    def _loc_828(): pass

    label('loc_828')

    Jump('loc_85C')

    def _loc_82B(): pass

    label('loc_82B')

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
    def _loc_85C(): pass

    label('loc_85C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x86A
@scena.Code('func_06_86A')
def func_06_86A():
    UnlockAchievement(0x02, 0x01F8, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 2, 0x1522)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_947',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0010, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['死之刃２'], 1)"),
            Expr.Return,
        ),
        'loc_8DE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['死之刃２']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A4, 2, 0x1522))

    Jump('loc_944')

    def _loc_8DE(): pass

    label('loc_8DE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['死之刃２']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['死之刃２']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0010, 60)
    OP_70(0x0010, 0)

    def _loc_944(): pass

    label('loc_944')

    Jump('loc_978')

    def _loc_947(): pass

    label('loc_947')

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
    def _loc_978(): pass

    label('loc_978')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x986
@scena.Code('func_07_986')
def func_07_986():
    UnlockAchievement(0x02, 0x01F9, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A4, 4, 0x1524)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A63',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0011, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['双子星'], 1)"),
            Expr.Return,
        ),
        'loc_9FA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x02A4, 4, 0x1524))

    Jump('loc_A60')

    def _loc_9FA(): pass

    label('loc_9FA')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0011, 60)
    OP_70(0x0011, 0)

    def _loc_A60(): pass

    label('loc_A60')

    Jump('loc_A94')

    def _loc_A63(): pass

    label('loc_A63')

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
    def _loc_A94(): pass

    label('loc_A94')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xAA2
@scena.Code('func_08_AA2')
def func_08_AA2():
    Return()

# id: 0x0009 offset: 0xAA3
@scena.Code('func_09_AA3')
def func_09_AA3():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    CameraMove(-12000, 30, -38910, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -18500, 40, -40040, 90)
    ChrSetPos(0x0102, -18500, 20, -38760, 90)
    ChrSetPos(0x00F8, -20000, 40, -40040, 90)
    ChrSetPos(0x00F9, -20000, 40, -38760, 90)

    @scena.Lambda('lambda_0B36')
    def lambda_0B36():
        ChrMoveTo(0x00FE, -12260, 20, -39450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B36)

    Sleep(50)

    @scena.Lambda('lambda_0B56')
    def lambda_0B56():
        ChrMoveTo(0x00FE, -12390, 10, -38320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B56)

    Sleep(50)

    @scena.Lambda('lambda_0B76')
    def lambda_0B76():
        ChrMoveTo(0x00FE, -13490, 40, -39640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0B76)

    Sleep(50)

    @scena.Lambda('lambda_0B96')
    def lambda_0B96():
        ChrMoveTo(0x00FE, -13670, 30, -38590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0B96)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010370001V#1020F这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C2B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370002V#072F#6P不行啊……\n',
            '眼前完全一片漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB3')

    def _loc_C2B(): pass

    label('loc_C2B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C73',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370003V#055F#6P喂喂……\n',
            '根本什么都看不见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB3')

    def _loc_C73(): pass

    label('loc_C73')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CB3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370004V#022F#6P不行啊……完全一片漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB3(): pass

    label('loc_CB3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D09',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370005V#065F#6P没、没有了导力灯，\n',
            '这里竟然会变得这么暗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DAA')

    def _loc_D09(): pass

    label('loc_D09')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D5B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370006V#025F#6P……没有导力灯，\n',
            '这里竟然会这样黑暗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DAA')

    def _loc_D5B(): pass

    label('loc_D5B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DAA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370007V#057F#6P没有了导力灯，\n',
            '这里竟然会变得这么暗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DAA(): pass

    label('loc_DAA')

    ChrTalk(
        0x0102,
        (
            '#0020370008V#1043F#5P如果不戴上『夜视眼镜』的话\n',
            '想通过这里实在太困难了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370009V#1042F如果身上没有的话\n',
            '就回城里的道具店找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370010V#1007F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370011V#1002F这样也好，\n',
            '顺便还能整备一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0xE91
@scena.Code('func_0A_E91')
def func_0A_E91():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    CameraMove(-12000, 30, -38910, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -18500, 40, -40040, 90)
    ChrSetPos(0x0102, -18500, 20, -38760, 90)
    ChrSetPos(0x00F8, -20000, 40, -40040, 90)
    ChrSetPos(0x00F9, -20000, 40, -38760, 90)

    @scena.Lambda('lambda_0F24')
    def lambda_0F24():
        ChrMoveTo(0x00FE, -12260, 20, -39450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F24)

    Sleep(50)

    @scena.Lambda('lambda_0F44')
    def lambda_0F44():
        ChrMoveTo(0x00FE, -12390, 10, -38320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0F44)

    Sleep(50)

    @scena.Lambda('lambda_0F64')
    def lambda_0F64():
        ChrMoveTo(0x00FE, -13490, 40, -39640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0F64)

    Sleep(50)

    @scena.Lambda('lambda_0F84')
    def lambda_0F84():
        ChrMoveTo(0x00FE, -13670, 30, -38590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0F84)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010370012V#1019F还好有夜视眼镜，\n',
            '总算可以看见路了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370013V但如果把它摘下来的话\n',
            '又会什么都看不见了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370014V#1035F#5P嗯，完全一片漆黑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370015V#1042F如果不想迷路的话，\n',
            '在这里行走的时候\n',
            '就一定要戴着夜视眼镜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370016V#1002F嗯，了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
