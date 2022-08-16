import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4102   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4102.x'
    header.mapIndex       = 1
    header.bgm            = 21
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
        ('ED6_DT09/CH10780._CH', 'ED6_DT09/CH10780P._CP'),
        ('ED6_DT09/CH10781._CH', 'ED6_DT09/CH10781P._CP'),
        ('ED6_DT09/CH10790._CH', 'ED6_DT09/CH10790P._CP'),
        ('ED6_DT09/CH10791._CH', 'ED6_DT09/CH10791P._CP'),
        ('ED6_DT09/CH10050._CH', 'ED6_DT09/CH10050P._CP'),
        ('ED6_DT09/CH10051._CH', 'ED6_DT09/CH10051P._CP'),
        ('ED6_DT09/CH10800._CH', 'ED6_DT09/CH10800P._CP'),
        ('ED6_DT09/CH10801._CH', 'ED6_DT09/CH10801P._CP'),
        ('ED6_DT09/CH10810._CH', 'ED6_DT09/CH10810P._CP'),
        ('ED6_DT09/CH10811._CH', 'ED6_DT09/CH10811P._CP'),
        ('ED6_DT09/CH10820._CH', 'ED6_DT09/CH10820P._CP'),
        ('ED6_DT09/CH10821._CH', 'ED6_DT09/CH10821P._CP'),
        ('ED6_DT09/CH11220._CH', 'ED6_DT09/CH11220P._CP'),
        ('ED6_DT09/CH11221._CH', 'ED6_DT09/CH11221P._CP'),
        ('ED6_DT09/CH11230._CH', 'ED6_DT09/CH11230P._CP'),
        ('ED6_DT09/CH11231._CH', 'ED6_DT09/CH11231P._CP'),
        ('ED6_DT09/CH11240._CH', 'ED6_DT09/CH11240P._CP'),
        ('ED6_DT09/CH11241._CH', 'ED6_DT09/CH11241P._CP'),
    ]

# id: 0x10001 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾尔贝离宫方向',
            x                   = 77370,
            z                   = 0,
            y                   = -15080,
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
            name                = '庭园大道方向',
            x                   = -79490,
            z                   = 0,
            y                   = 4930,
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
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '丘陵毒蜂3',
            x           = 29090,
            z           = 110,
            y           = -28620,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0261,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '贪婪鳄鱼',
            x           = 35270,
            z           = 0,
            y           = -43590,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '贪婪鳄鱼4',
            x           = 34970,
            z           = 100,
            y           = -63310,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0265,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '地狱火爆麻雀',
            x           = 4820,
            z           = 100,
            y           = -79050,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '迅猛小鹫3',
            x           = 5370,
            z           = 120,
            y           = -58670,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0268,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '丘陵毒蜂',
            x           = 12310,
            z           = 10,
            y           = 7720,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0259,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '地狱火爆麻雀',
            x           = 34490,
            z           = 40,
            y           = 31600,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '地狱火爆麻雀3',
            x           = 21340,
            z           = 10,
            y           = 64120,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0267,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '地狱火爆麻雀2迅猛小鹫2',
            x           = 32640,
            z           = 90,
            y           = 49450,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x026A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '贪婪鳄鱼',
            x           = -6330,
            z           = 140,
            y           = 2330,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 14510,
            z           = 0,
            y           = -15050,
            word_0C     = 0x0000,
            word_0E     = 0x0010,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x05E2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x2CE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2CE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 480,
            triggerZ            = 0,
            triggerY            = -67940,
            triggerRange        = 1000,
            actorX              = 1140,
            actorZ              = 0,
            actorY              = -67940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13310,
            triggerZ            = -30,
            triggerY            = 61150,
            triggerRange        = 1000,
            actorX              = 12570,
            actorZ              = -30,
            actorY              = 61290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7430,
            triggerZ            = 30,
            triggerY            = -17940,
            triggerRange        = 1000,
            actorX              = 7020,
            actorZ              = 30,
            actorY              = -18340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 24020,
            triggerZ            = 500,
            triggerY            = 54480,
            triggerRange        = 1500,
            actorX              = 24020,
            actorZ              = 4000,
            actorY              = 54480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3540,
            triggerZ            = 500,
            triggerY            = -67980,
            triggerRange        = 1500,
            actorX              = 3540,
            actorZ              = 4000,
            actorY              = -67980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x382
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_38E'),
        (-1, 'loc_3A4'),
    )

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 5, 0x615)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A1',
    )

    SetScenaFlags(ScenaFlag(0x00C2, 5, 0x615))
    Event(0, func_03_437)

    def _loc_3A1(): pass

    label('loc_3A1')

    Jump('loc_3A4')

    def _loc_3A4(): pass

    label('loc_3A4')

    ExecExpressionWithReg(
        0x0000,
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x3B1
@scena.Code('func_01_3B1')
def func_01_3B1():
    OP_16(0x02, 4000, -125000, -137000, 196709)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 4, 0x684)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D5',
    )

    OP_6F(0x0000, 0)

    Jump('loc_3DC')

    def _loc_3D5(): pass

    label('loc_3D5')

    OP_6F(0x0000, 60)

    def _loc_3DC(): pass

    label('loc_3DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 6, 0x686)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EE',
    )

    OP_6F(0x0001, 0)

    Jump('loc_3F5')

    def _loc_3EE(): pass

    label('loc_3EE')

    OP_6F(0x0001, 60)

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D1, 0, 0x688)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_407',
    )

    OP_6F(0x0002, 0)

    Jump('loc_40E')

    def _loc_407(): pass

    label('loc_407')

    OP_6F(0x0002, 60)

    def _loc_40E(): pass

    label('loc_40E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_420',
    )

    ChrSetFlags(0x0015, 0x0080)

    def _loc_420(): pass

    label('loc_420')

    Return()

# id: 0x0002 offset: 0x421
@scena.Code('func_02_421')
def func_02_421():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_436',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_421')

    def _loc_436(): pass

    label('loc_436')

    Return()

# id: 0x0003 offset: 0x437
@scena.Code('func_03_437')
def func_03_437():
    EventBegin(0x00)
    CameraMove(-62530, 0, 5200, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -66840, 0, 6300, 270)
    ChrSetPos(0x0102, -66930, 0, 4930, 270)

    @scena.Lambda('lambda_049E')
    def lambda_049E():
        CameraMove(-60360, 0, 5200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_049E)

    @scena.Lambda('lambda_04B6')
    def lambda_04B6():
        ChrWalkTo(0x00FE, -60360, 0, 5950, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04B6)

    @scena.Lambda('lambda_04D1')
    def lambda_04D1():
        ChrWalkTo(0x00FE, -60500, 0, 4470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_04D1)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010101345V#501F这就是艾尔贝周游道啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101346V在森林中有用石头铺成的大路，\n',
            '真是有趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101347V#010F作为王都市民休憩的场所，\n',
            '好像是很久之前就建造的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101348V大概，已经有数百年的历史了吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101349V#000F嗯……\n',
            '不愧是女王的脚下啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101350V#505F不过，怎么感觉有魔兽的气息呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101351V#015F真是敏锐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101352V#012F我也感觉到这里\n',
            '有比刚才路上更厉害的魔兽呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101353V一边保持警惕一边找金先生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x6DC
@scena.Code('func_04_6DC')
def func_04_6DC():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 4, 0x684)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_880',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 5, 0x685)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7B8',
    )

    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetPos(0x000A, 1700, 2500, -68060, 320)
    ChrTurnDirection(0x000A, 0x0000, 0)

    @scena.Lambda('lambda_072B')
    def lambda_072B():
        ChrMoveTo(0x00FE, 1700, 1000, -68060, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_072B)

    @scena.Lambda('lambda_0746')
    def lambda_0746():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0746)

    ChrClearFlags(0x000A, 0x0080)

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
    Battle(0x0000026C, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x000A, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_793'),
        (0x00000002, 'loc_7A5'),
        (0x00000001, 'loc_7B5'),
        (-1, 'loc_7B8'),
    )

    def _loc_793(): pass

    label('loc_793')

    SetScenaFlags(ScenaFlag(0x00D0, 5, 0x685))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_7B8')

    def _loc_7A5(): pass

    label('loc_7A5')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_7B5(): pass

    label('loc_7B5')

    OP_B4(0x00)

    Return()

    def _loc_7B8(): pass

    label('loc_7B8')

    If(
        (
            (Expr.Eval, "AddItem(0x0263, 1)"),
            Expr.Return,
        ),
        'loc_80C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '防御３',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D0, 4, 0x684))

    Jump('loc_87D')

    def _loc_80C(): pass

    label('loc_80C')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '防御３',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '防御３',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_87D(): pass

    label('loc_87D')

    Jump('loc_8B6')

    def _loc_880(): pass

    label('loc_880')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x3D)
    def _loc_8B6(): pass

    label('loc_8B6')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x8C4
@scena.Code('func_05_8C4')
def func_05_8C4():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 6, 0x686)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A68',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 7, 0x687)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9A0',
    )

    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetPos(0x000A, 12570, 2500, 61290, 320)
    ChrTurnDirection(0x000A, 0x0000, 0)

    @scena.Lambda('lambda_0913')
    def lambda_0913():
        ChrMoveTo(0x00FE, 12570, 1000, 61290, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0913)

    @scena.Lambda('lambda_092E')
    def lambda_092E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_092E)

    ChrClearFlags(0x000A, 0x0080)

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
    Battle(0x0000026C, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x000A, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_97B'),
        (0x00000002, 'loc_98D'),
        (0x00000001, 'loc_99D'),
        (-1, 'loc_9A0'),
    )

    def _loc_97B(): pass

    label('loc_97B')

    SetScenaFlags(ScenaFlag(0x00D0, 7, 0x687))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_9A0')

    def _loc_98D(): pass

    label('loc_98D')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_99D(): pass

    label('loc_99D')

    OP_B4(0x00)

    Return()

    def _loc_9A0(): pass

    label('loc_9A0')

    If(
        (
            (Expr.Eval, "AddItem(0x0269, 1)"),
            Expr.Return,
        ),
        'loc_9F4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '魔防３',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D0, 6, 0x686))

    Jump('loc_A65')

    def _loc_9F4(): pass

    label('loc_9F4')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '魔防３',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '魔防３',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_A65(): pass

    label('loc_A65')

    Jump('loc_A9E')

    def _loc_A68(): pass

    label('loc_A68')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x3E)
    def _loc_A9E(): pass

    label('loc_A9E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xAAC
@scena.Code('func_06_AAC')
def func_06_AAC():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D1, 0, 0x688)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B9C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_B22',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D1, 0, 0x688))

    Jump('loc_B99')

    def _loc_B22(): pass

    label('loc_B22')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_B99(): pass

    label('loc_B99')

    Jump('loc_BD2')

    def _loc_B9C(): pass

    label('loc_B9C')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x3F)
    def _loc_BD2(): pass

    label('loc_BD2')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xBE0
@scena.Code('func_07_BE0')
def func_07_BE0():
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着古老的苍耀石石碑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0xC22
@scena.Code('func_08_C22')
def func_08_C22():
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着古老的红耀石石碑。',
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
