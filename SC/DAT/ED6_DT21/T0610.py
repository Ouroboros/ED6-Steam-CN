import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0610_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0610   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0610.x'
    header.mapIndex       = 17
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0610_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT26/CH20237._CH', 'ED6_DT26/CH20237P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01233._CH', 'ED6_DT07/CH01233P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '罗宾队长',
            x                   = -19380,
            z                   = 0,
            y                   = -980,
            direction           = 98,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '古利乌副队长',
            x                   = -111940,
            z                   = 0,
            y                   = 21850,
            direction           = 87,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '士兵安顿',
            x                   = -7220,
            z                   = 0,
            y                   = 2820,
            direction           = 162,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '萨姆',
            x                   = -90130,
            z                   = 0,
            y                   = -22320,
            direction           = 253,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '亚米丽',
            x                   = -57740,
            z                   = 0,
            y                   = -21510,
            direction           = 352,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '拜舍尔',
            x                   = -63920,
            z                   = 0,
            y                   = -22680,
            direction           = 250,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '利吉',
            x                   = -5350,
            z                   = 0,
            y                   = 880,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '旅行者',
            x                   = -60600,
            z                   = 0,
            y                   = -27550,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '旅行者',
            x                   = -59280,
            z                   = 100,
            y                   = -26820,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '旅行者',
            x                   = -94140,
            z                   = 0,
            y                   = -28140,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '旅行者',
            x                   = -95590,
            z                   = 0,
            y                   = -25980,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
    )

# id: 0x10002 offset: 0x26A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x26A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x26A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -7430,
            triggerZ            = 0,
            triggerY            = 900,
            triggerRange        = 1000,
            actorX              = -7220,
            actorZ              = 1500,
            actorY              = 2820,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -109840,
            triggerZ            = 0,
            triggerY            = 21450,
            triggerRange        = 1000,
            actorX              = -111940,
            actorZ              = 1500,
            actorY              = 21850,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -92220,
            triggerZ            = 0,
            triggerY            = -22040,
            triggerRange        = 1000,
            actorX              = -90130,
            actorZ              = 1500,
            actorY              = -22320,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2D6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2F2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_12_305F)

    def _loc_2F2(): pass

    label('loc_2F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_319',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, -52400, 0, 23230, 0)
    CreateThread(0x0008, 0x00, 0x06, func_02_442)

    Jump('loc_3D9')

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 6, 0x1806)),
            Expr.Return,
        ),
        'loc_360',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_338',
    )

    ChrClearFlags(0x000D, 0x0080)

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 1, 0x1811)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_35D',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

    def _loc_35D(): pass

    label('loc_35D')

    Jump('loc_3D9')

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_36A',
    )

    Jump('loc_3D9')

    def _loc_36A(): pass

    label('loc_36A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_37D',
    )

    ChrSetFlags(0x0009, 0x0080)
    OP_64(0x01, 0x0001)

    Jump('loc_3D9')

    def _loc_37D(): pass

    label('loc_37D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_3BE',
    )

    ChrSetPos(0x0008, -19540, 0, 1620, 109)
    ChrSetFlags(0x0008, 0x0010)
    CreateThread(0x0008, 0x00, 0x06, func_02_442)
    ChrSetPos(0x0009, -17890, 0, 1620, 271)
    ChrSetFlags(0x0009, 0x0010)
    OP_64(0x01, 0x0001)

    Jump('loc_3D9')

    def _loc_3BE(): pass

    label('loc_3BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_3C8',
    )

    Jump('loc_3D9')

    def _loc_3C8(): pass

    label('loc_3C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_3D2',
    )

    Jump('loc_3D9')

    def _loc_3D2(): pass

    label('loc_3D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3D9',
    )

    def _loc_3D9(): pass

    label('loc_3D9')

    Return()

# id: 0x0001 offset: 0x3DA
@scena.Code('func_01_3DA')
def func_01_3DA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F2',
    )

    OP_B1('t0610_y')

    Jump('loc_3FB')

    def _loc_3F2(): pass

    label('loc_3F2')

    OP_B1('t0610_n')

    def _loc_3FB(): pass

    label('loc_3FB')

    OP_1C(0x05, 0x00, 0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_414',
    )

    OP_1B(0x00, 0x00, 0x0015)

    Jump('loc_425')

    def _loc_414(): pass

    label('loc_414')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_425',
    )

    OP_1B(0x01, 0x00, 0x0016)

    def _loc_425(): pass

    label('loc_425')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_441',
    )

    OP_6F(0x0005, 100)
    OP_72(0x0005, 0x0010)
    OP_64(0x01, 0x0001)

    def _loc_441(): pass

    label('loc_441')

    Return()

# id: 0x0002 offset: 0x442
@scena.Code('func_02_442')
def func_02_442():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_465',
    )

    OP_8D(0x00FE, -22660, -4810, -14730, 1940, 3000)

    Jump('func_02_442')

    def _loc_465(): pass

    label('loc_465')

    Return()

# id: 0x0003 offset: 0x466
@scena.Code('func_03_466')
def func_03_466():
    Call(0, 0x0009)

    Return()

# id: 0x0004 offset: 0x46B
@scena.Code('func_04_46B')
def func_04_46B():
    Call(0, 0x0007)

    Return()

# id: 0x0005 offset: 0x470
@scena.Code('func_05_470')
def func_05_470():
    Call(0, 0x0008)

    Return()

# id: 0x0006 offset: 0x475
@scena.Code('func_06_475')
def func_06_475():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_564',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50F',
    )

    ChrTalk(
        0x00FE,
        (
            '不仅仅是这里，\n',
            '王国各地的据点\n',
            '全都处于警戒态势。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '例外的地方\n',
            '也就只有沃尔费要塞了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里总是\n',
            '有自己的一套方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_561')

    def _loc_50F(): pass

    label('loc_50F')

    ChrTalk(
        0x00FE,
        (
            '王国各地的据点\n',
            '全都处于警戒态势。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '例外的地方\n',
            '也就只有沃尔费要塞了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_561(): pass

    label('loc_561')

    Jump('loc_CF6')

    def _loc_564(): pass

    label('loc_564')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_6B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62C',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们是游击士吧。\n',
            '工作辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然用分配的发生器\n',
            '修复了通信机、\n',
            '但是状况依然很严峻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在粮食储备\n',
            '也还充足……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了防止事态长期化，\n',
            '必须尽快制订对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_6B4')

    def _loc_62C(): pass

    label('loc_62C')

    ChrTalk(
        0x00FE,
        (
            '现在，关所加强了警戒、\n',
            '通行的审查也很严格……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于高层部门的命令，\n',
            '游击士可以\n',
            '自由通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，也期待\n',
            '你们有相应的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B4(): pass

    label('loc_6B4')

    Jump('loc_CF6')

    def _loc_6B7(): pass

    label('loc_6B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_7C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_730',
    )

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约也平安签订了，\n',
            '洛连特的雾也都散去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也松了口气，\n',
            '阿斯顿队长也是同样的想法吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BE')

    def _loc_730(): pass

    label('loc_730')

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约也平安签订了，\n',
            '洛连特的雾也都散去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天早上的太阳把两件烦心事\n',
            '同时赶跑了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下就能安心\n',
            '返回日常的任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_7BE(): pass

    label('loc_7BE')

    Jump('loc_CF6')

    def _loc_7C1(): pass

    label('loc_7C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_8B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_82C',
    )

    ChrTalk(
        0x00FE,
        (
            '让人成长\n',
            '最有效的药就是责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '威尔特桥的新兵们，\n',
            '希望这次事件让他们脱胎换骨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B4')

    def _loc_82C(): pass

    label('loc_82C')

    ChrTalk(
        0x00FE,
        (
            '那么说来，阿斯顿队长\n',
            '正为新兵教育而烦恼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让人成长\n',
            '最有效的药就是责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛连特这里的警备任务\n',
            '能让他们成长就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_8B4(): pass

    label('loc_8B4')

    Jump('loc_CF6')

    def _loc_8B7(): pass

    label('loc_8B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_9BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_912',
    )

    ChrTalk(
        0x00FE,
        (
            '威尔特桥的部队不久\n',
            '也将到达洛连特吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '交给他们\n',
            '应该就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9BB')

    def _loc_912(): pass

    label('loc_912')

    ChrTalk(
        0x00FE,
        (
            '洛连特市似乎也发生了\n',
            '令人担心的事件呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军也为了市民的安全\n',
            '决定派遣部队了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '威尔特桥的部队不久\n',
            '也将到达洛连特吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '交给他们\n',
            '应该就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_9BB(): pass

    label('loc_9BB')

    Jump('loc_CF6')

    def _loc_9BE(): pass

    label('loc_9BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_AA3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 1, 0x1811)),
            Expr.Return,
        ),
        'loc_A3C',
    )

    ChrTalk(
        0x00FE,
        (
            '洛连特的雾\n',
            '说不定还挺严重的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雾可能也会\n',
            '扩散到这附近来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是加强一下士兵们\n',
            '的警戒比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AA0')

    def _loc_A3C(): pass

    label('loc_A3C')

    ChrTalk(
        0x00FE,
        (
            '定期船赛希莉亚号\n',
            '好像滞留在洛连特无法起航。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟能让飞船无法出航，\n',
            '这样的雾真是前所未见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AA0(): pass

    label('loc_AA0')

    Jump('loc_CF6')

    def _loc_AA3(): pass

    label('loc_AA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_B34',
    )

    ChrTalk(
        0x00FE,
        (
            '飞在空中的巨大人偶，\n',
            '我们的士兵好像也亲眼看到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说是向湖中央方向\n',
            '飞去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但连王国军自豪的警备艇\n',
            '好像也找不到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF6')

    def _loc_B34(): pass

    label('loc_B34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_BBD',
    )

    ChrTalk(
        0x00FE,
        (
            '『结社』……吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟突然袭击警备本部 \n',
            '所在的离宫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽不知道到底是个什么样的组织，\n',
            '总之还是做好万全的准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF6')

    def _loc_BBD(): pass

    label('loc_BBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_BF4',
    )

    ChrTalk(
        0x00FE,
        (
            '……完毕，请立即\n',
            '组织巡回周游道的部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF6')

    def _loc_BF4(): pass

    label('loc_BF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_C77',
    )

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔留驻的所有部队\n',
            '都接到了强化警备的通知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '签字仪式如能平安进行\n',
            '是最好不过，但预防事态不测\n',
            '是我们的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF6')

    def _loc_C77(): pass

    label('loc_C77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_CBA',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，你好。\n',
            '现在大门四处都能自由参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请自便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF6')

    def _loc_CBA(): pass

    label('loc_CBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_CF6',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想去洛连特时\n',
            '请在接待处办手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CF6(): pass

    label('loc_CF6')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0xCFA
@scena.Code('func_07_CFA')
def func_07_CFA():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_DFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_D6A',
    )

    ChrTalk(
        0x0009,
        (
            '听说在洛连特滞留的\n',
            '定期船也恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '签字仪式的出席者们\n',
            '也按照预定踏上了归途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF8')

    def _loc_D6A(): pass

    label('loc_D6A')

    ChrTalk(
        0x0009,
        (
            '听说在洛连特滞留的\n',
            '定期船也恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '签字仪式的出席者们\n',
            '也按照预定踏上了归途。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然令人捏了一把冷汗，\n',
            '总算是平安结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_DF8(): pass

    label('loc_DF8')

    Jump('loc_1320')

    def _loc_DFB(): pass

    label('loc_DFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_F23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E72',
    )

    ChrTalk(
        0x0009,
        (
            '威尔特桥那里\n',
            '其实也有很好的钓鱼地点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '隐蔽在非常不在意的地方呢。\n',
            '是懂的人才能找到的好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F20')

    def _loc_E72(): pass

    label('loc_E72')

    ChrTalk(
        0x0009,
        (
            '威尔特桥的守备队\n',
            '据说已经开始对\n',
            '洛连特市的警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唔唔，话说回来\n',
            '威尔特桥啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……其实那里\n',
            '也有很好的钓鱼地点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果报名会不会\n',
            '被编入补充部队呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_F20(): pass

    label('loc_F20')

    Jump('loc_1320')

    def _loc_F23(): pass

    label('loc_F23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1013',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_F92',
    )

    ChrTalk(
        0x0009,
        (
            '最近真是诸多事忙啊。\n',
            '钓鱼的机会也减少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '等签字仪式结束了，\n',
            '真想悠闲地垂钓一番啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1010')

    def _loc_F92(): pass

    label('loc_F92')

    ChrTalk(
        0x0009,
        (
            '雾越来越浓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '签字仪式结束之后\n',
            '虽然偷偷盘算着\n',
            '去钓个鱼什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唔唔，这么大的雾\n',
            '附近的钓鱼场也去不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1010(): pass

    label('loc_1010')

    Jump('loc_1320')

    def _loc_1013(): pass

    label('loc_1013')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_10DC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 1, 0x1811)),
            Expr.Return,
        ),
        'loc_104B',
    )

    ChrTalk(
        0x0009,
        (
            '外边好像挺热闹的……\n',
            '有谁来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D9')

    def _loc_104B(): pass

    label('loc_104B')

    ChrTalk(
        0x0009,
        (
            '明天就是签字仪式了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '回想百日战役的事，\n',
            '简直像梦一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，这个先不提了，\n',
            '目前的问题是这个雾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '还好现在旅客比较少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10D9(): pass

    label('loc_10D9')

    Jump('loc_1320')

    def _loc_10DC(): pass

    label('loc_10DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_115A',
    )

    ChrTalk(
        0x0009,
        (
            '迷雾峡谷的训练基地\n',
            '好像被空贼袭击了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '看起来像是顺着格兰赛尔的事件\n',
            '趁火打劫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唉，是我想太多了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1320')

    def _loc_115A(): pass

    label('loc_115A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_1183',
    )

    ChrTalk(
        0x0009,
        (
            '……明白了，\n',
            '我立即安排。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1320')

    def _loc_1183(): pass

    label('loc_1183')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_1218',
    )

    ChrTalk(
        0x0009,
        (
            '收到了情报部余党\n',
            '在柏斯出现的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '他们也有可能会\n',
            '妨碍签字仪式……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '总之\n',
            '我们的任务是守护这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '必须专心执行任务才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1320')

    def _loc_1218(): pass

    label('loc_1218')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_12BC',
    )

    ChrTalk(
        0x0009,
        (
            '帝国大使和共和国大使，\n',
            '听说两人完全处不来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为原本就是两个水火不容的国家，\n',
            '这也难怪、倒是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那样的两国\n',
            '真的能缔结\n',
            '互不侵犯条约吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1320')

    def _loc_12BC(): pass

    label('loc_12BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1320',
    )

    ChrTalk(
        0x0009,
        (
            '嗯？有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '现在正在做\n',
            '警备的编成表呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为马上就是条约的签字仪式了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1320(): pass

    label('loc_1320')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x1324
@scena.Code('func_08_1324')
def func_08_1324():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_141E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13C5',
    )

    ChrTalk(
        0x000A,
        (
            '吃饭时的话题还是\n',
            '那个浮游岛的事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '至今还不清楚那到底是什么。\n',
            '真是令人害怕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然只是浮在那里，\n',
            '但还是感到不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_141B')

    def _loc_13C5(): pass

    label('loc_13C5')

    ChrTalk(
        0x000A,
        (
            '浮游岛到底是什么，\n',
            '好像还不清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然只是浮在那里，\n',
            '还是令人感到不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_141B(): pass

    label('loc_141B')

    Jump('loc_19FC')

    def _loc_141E(): pass

    label('loc_141E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1536',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14E7',
    )

    ChrTalk(
        0x000A,
        (
            '最近那场雾就够惊人的了，\n',
            '真是天外有天啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '导力器竟然不能使用，\n',
            '怎么会发生这种事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '都是因为这个今天早上的点心，\n',
            '感觉也没那么好吃了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '明明吃饭是\n',
            '少有的乐趣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1533')

    def _loc_14E7(): pass

    label('loc_14E7')

    ChrTalk(
        0x000A,
        (
            '食堂的亚米丽也因为\n',
            '不能用炉子而发愁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '明明吃饭是\n',
            '少有的乐趣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1533(): pass

    label('loc_1533')

    Jump('loc_19FC')

    def _loc_1536(): pass

    label('loc_1536')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_15A8',
    )

    ChrTalk(
        0x000A,
        (
            '此次的互不侵犯条约使得外国来的\n',
            '旅客也增加了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '可要妥善对待他们，\n',
            '不能丢了利贝尔人的脸呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19FC')

    def _loc_15A8(): pass

    label('loc_15A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_160E',
    )

    ChrTalk(
        0x000A,
        (
            '七耀教会的巡回神父\n',
            '平安到达洛连特了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这种时候还去洛连特\n',
            '呀～真是有胆量的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19FC')

    def _loc_160E(): pass

    label('loc_160E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_16E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1677',
    )

    ChrTalk(
        0x000A,
        (
            '总，总觉得雾\n',
            '好像越来越浓了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天是签字仪式的日子。\n',
            '希望不要发生什么事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16E0')

    def _loc_1677(): pass

    label('loc_1677')

    ChrTalk(
        0x000A,
        (
            '总，总觉得雾\n',
            '好像越来越浓了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天是签字仪式的重要日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '拜、拜托\n',
            '不要发生什么事啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_16E0(): pass

    label('loc_16E0')

    Jump('loc_19FC')

    def _loc_16E3(): pass

    label('loc_16E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_178E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 1, 0x1811)),
            Expr.Return,
        ),
        'loc_1739',
    )

    ChrTalk(
        0x000A,
        (
            '洛连特起的雾\n',
            '好像比想象中的还厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '旅客们都疲惫不堪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_178B')

    def _loc_1739(): pass

    label('loc_1739')

    ChrTalk(
        0x000A,
        (
            '许可证发下来之前\n',
            '要稍微花费点时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '签字仪式快到了，\n',
            '警备也越来越严了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_178B(): pass

    label('loc_178B')

    Jump('loc_19FC')

    def _loc_178E(): pass

    label('loc_178E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1804',
    )

    ChrTalk(
        0x000A,
        (
            '一开始，听说周游道出现的\n',
            '是『结社』的手下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '结果竟然是特务兵\n',
            '的余党嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19FC')

    def _loc_1804(): pass

    label('loc_1804')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_1828',
    )

    ChrTalk(
        0x000A,
        (
            '啊，副队长去了哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19FC')

    def _loc_1828(): pass

    label('loc_1828')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_1881',
    )

    ChrTalk(
        0x000A,
        (
            '呀，来城墙\n',
            '观赏晚霞吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '现在这个时期来看\n',
            '是最美丽的。\n',
            '慢慢欣赏好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19FC')

    def _loc_1881(): pass

    label('loc_1881')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_1914',
    )

    ChrTalk(
        0x000A,
        (
            '今天早上开始就一直在说\n',
            '情报部余党的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那些家伙，在柏斯地区\n',
            '到底图谋着什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，无论如何\n',
            '他们也过不了这格鲁纳门的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19FC')

    def _loc_1914(): pass

    label('loc_1914')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_19A0',
    )

    ChrTalk(
        0x000A,
        (
            '如果要上城墙上参观，\n',
            '请务必小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听说前几天，有游客\n',
            '在圣海姆门的长城上\n',
            '差点掉下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '千万别受伤了，\n',
            '要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19FC')

    def _loc_19A0(): pass

    label('loc_19A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_19FC',
    )

    ChrTalk(
        0x000A,
        (
            '哎呀，要去洛连特吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '去洛连特请到这边\n',
            '柜台办理手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '……咦，不是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19FC(): pass

    label('loc_19FC')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x1A00
@scena.Code('func_09_1A00')
def func_09_1A00():
    TalkBegin(0x000B)
    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A1D',
    )

    OP_0D()
    OP_A9(0x0A)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_1A1D(): pass

    label('loc_1A1D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A2E',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_1A2E(): pass

    label('loc_1A2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1B25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1ACC',
    )

    ChrTalk(
        0x000B,
        (
            '最近的大雾刚刚散去，\n',
            '现在又是这样的紧急状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '害的我店里\n',
            '生意惨淡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呼，期待下次诞辰庆典啊，\n',
            '真是的、现在就等不及了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1B22')

    def _loc_1ACC(): pass

    label('loc_1ACC')

    ChrTalk(
        0x000B,
        (
            '最近我这里\n',
            '生意惨淡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呼，期待下次诞辰庆典啊，\n',
            '真是的、现在就等不及了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B22(): pass

    label('loc_1B22')

    Jump('loc_2158')

    def _loc_1B25(): pass

    label('loc_1B25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1BB7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B7F',
    )

    ChrTalk(
        0x000B,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这个时候还旅行，\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1BB4')

    def _loc_1B7F(): pass

    label('loc_1B7F')

    ChrTalk(
        0x000B,
        (
            '这个时候还旅行，\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BB4(): pass

    label('loc_1BB4')

    Jump('loc_2158')

    def _loc_1BB7(): pass

    label('loc_1BB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1C89',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1C12',
    )

    ChrTalk(
        0x000B,
        (
            '今天真是久违的\n',
            '好天气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我们的床单现在\n',
            '也散发着太阳的气味哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C86')

    def _loc_1C12(): pass

    label('loc_1C12')

    ChrTalk(
        0x000B,
        (
            '哟，今天是久违的\n',
            '好天气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我们的床单现在\n',
            '也散发着太阳的气味哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '还是干干爽爽的\n',
            '床单感觉舒服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1C86(): pass

    label('loc_1C86')

    Jump('loc_2158')

    def _loc_1C89(): pass

    label('loc_1C89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1D56',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1CE0',
    )

    ChrTalk(
        0x000B,
        (
            '空气这么潮湿，\n',
            '洗了的床单也干不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '干脆塞进\n',
            '烤炉里算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D53')

    def _loc_1CE0(): pass

    label('loc_1CE0')

    ChrTalk(
        0x000B,
        (
            '空气这么潮湿，\n',
            '洗了的床单也干不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '就算是这样，再不替换\n',
            '一会可就要长霉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊啊，蓝天真可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1D53(): pass

    label('loc_1D53')

    Jump('loc_2158')

    def _loc_1D56(): pass

    label('loc_1D56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1E27',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1DA8',
    )

    ChrTalk(
        0x000B,
        (
            '现在床位都空着，\n',
            '可以随便选啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不介意的话就请休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E24')

    def _loc_1DA8(): pass

    label('loc_1DA8')

    ChrTalk(
        0x000B,
        (
            '哟，现在床位都空着，\n',
            '可以随便选啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '今天有签字仪式，\n',
            '但是从早上开始就是这么大雾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这也难怪客人\n',
            '都变少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1E24(): pass

    label('loc_1E24')

    Jump('loc_2158')

    def _loc_1E27(): pass

    label('loc_1E27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1F2B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 1, 0x1811)),
            Expr.Return,
        ),
        'loc_1E7B',
    )

    ChrTalk(
        0x000B,
        (
            '雾有那么厉害吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这格鲁纳门附近\n',
            '从早上开始就是好天气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F28')

    def _loc_1E7B(): pass

    label('loc_1E7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1ED7',
    )

    ChrTalk(
        0x000B,
        (
            '本旅店欢迎任何人。\n',
            '店里招待所有来这里的旅行者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果想住宿\n',
            '就跟我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F28')

    def _loc_1ED7(): pass

    label('loc_1ED7')

    ChrTalk(
        0x000B,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这里是所有人都\n',
            '喜爱的旅店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果想住宿\n',
            '就跟我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1F28(): pass

    label('loc_1F28')

    Jump('loc_2158')

    def _loc_1F2B(): pass

    label('loc_1F2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1FA1',
    )

    ChrTalk(
        0x000B,
        (
            '最近，士兵们\n',
            '看来又忙起来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '要准备签字仪式吧，\n',
            '好像还不止这个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是不是和王都事件有关啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2158')

    def _loc_1FA1(): pass

    label('loc_1FA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_1FE6',
    )

    ChrTalk(
        0x000B,
        (
            '哟，两位客人。\n',
            '要住宿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '抱歉今天旅馆被包下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2158')

    def _loc_1FE6(): pass

    label('loc_1FE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_202E',
    )

    ChrTalk(
        0x000B,
        (
            '嗯？感觉好像\n',
            '很慌张的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哈哈，约会\n',
            '迟到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2158')

    def _loc_202E(): pass

    label('loc_202E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_2084',
    )

    ChrTalk(
        0x000B,
        (
            '好，今天天气好，\n',
            '床单也都干啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '想享受太阳的香味，\n',
            '就住在这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2158')

    def _loc_2084(): pass

    label('loc_2084')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2115',
    )

    ChrTalk(
        0x000B,
        (
            '现在王国军为了互不侵犯条约\n',
            '的准备好像忙得不可开交呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不愧是国家性的签字仪式啊。\n',
            '要是被情报部那些家伙\n',
            '捣乱了那可有失颜面啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2158')

    def _loc_2115(): pass

    label('loc_2115')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2158',
    )

    ChrTalk(
        0x000B,
        (
            '哟，这里是格鲁纳门的旅店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不介意的话，就住下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2158(): pass

    label('loc_2158')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x215C
@scena.Code('func_0A_215C')
def func_0A_215C():
    TalkBegin(0x000C)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2179',
    )

    OP_0D()
    OP_A9(0x0B)
    OP_56(0x00)
    TalkEnd(0x000C)

    Return()

    def _loc_2179(): pass

    label('loc_2179')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_218A',
    )

    TalkEnd(0x000C)

    Return()

    def _loc_218A(): pass

    label('loc_218A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_229A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2247',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正在考虑\n',
            '明天的菜单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果炉子不能使用，\n',
            '干脆就全做冷菜好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '冷汤加沙拉，\n',
            '再加点白汁红肉之类的怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然像饭前零食一样，\n',
            '但好像挺华丽的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_2297')

    def _loc_2247(): pass

    label('loc_2247')

    ChrTalk(
        0x00FE,
        (
            '如果炉子不能使用，\n',
            '干脆全做冷菜好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎样增加分量，\n',
            '好象是个问题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2297(): pass

    label('loc_2297')

    Jump('loc_2A24')

    def _loc_229A(): pass

    label('loc_229A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_238C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2346',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，今天真是糟糕透顶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '炉子不能使用，\n',
            '只能随便做点料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这里的士兵很善良，\n',
            '都说好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我知道那是强颜欢笑，\n',
            '反而更加难过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_2389')

    def _loc_2346(): pass

    label('loc_2346')

    ChrTalk(
        0x00FE,
        (
            '唉，今天真是糟糕透顶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '炉子不能使用，\n',
            '只能随便做点料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2389(): pass

    label('loc_2389')

    Jump('loc_2A24')

    def _loc_238C(): pass

    label('loc_238C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2466',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_23ED',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵们的表情\n',
            '也终于开朗了起来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天的吃饭时间\n',
            '似乎也会热闹起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2463')

    def _loc_23ED(): pass

    label('loc_23ED')

    ChrTalk(
        0x00FE,
        (
            '士兵们的表情\n',
            '也终于开朗了起来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天的吃饭时间\n',
            '似乎也会热闹起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呼呼，我也要\n',
            '努力做饭才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_2463(): pass

    label('loc_2463')

    Jump('loc_2A24')

    def _loc_2466(): pass

    label('loc_2466')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_25BA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_24D1',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的午饭\n',
            '是卢安风味的鱼料理哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '参考东方料理的手法，\n',
            '进行了改进的自信作品呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25B7')

    def _loc_24D1(): pass

    label('loc_24D1')

    ChrTalk(
        0x00FE,
        (
            '今天的午饭\n',
            '是卢安风味的鱼料理哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用香味蔬菜增加香味，\n',
            '再用蒸锅加热。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '参考东方料理的手法，\n',
            '进行了改进的自信作品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '签字仪式的警备加上雾的事件……\n',
            '士兵们也真够辛苦的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少要努力让他们\n',
            '吃得开心才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_25B7(): pass

    label('loc_25B7')

    Jump('loc_2A24')

    def _loc_25BA(): pass

    label('loc_25BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2649',
    )

    ChrTalk(
        0x00FE,
        (
            '东方料理的烹调法\n',
            '有不少值得参考的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能好好利用\n',
            '应该也能用于利贝尔料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '并不是单纯的模仿，\n',
            '而是要取其精粹哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A24')

    def _loc_2649(): pass

    label('loc_2649')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_27BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 1, 0x1811)),
            Expr.Return,
        ),
        'loc_26B1',
    )

    ChrTalk(
        0x00FE,
        (
            '客人们看来\n',
            '都是历经艰苦\n',
            '才好不容易到了这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得让他们\n',
            '吃上好吃的东西才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27B8')

    def _loc_26B1(): pass

    label('loc_26B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2717',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，我买了本书\n',
            '正在学习东方料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了学习到更多的料理手艺，\n',
            '只有不断的挑战哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27B8')

    def _loc_2717(): pass

    label('loc_2717')

    ChrTalk(
        0x00FE,
        (
            '最近，我买了本书\n',
            '正在学习东方料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最感头痛的\n',
            '是调味料不同呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然找了相似的东西\n',
            '尝试着做……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，东方来的客人\n',
            '却说味道完全不一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_27B8(): pass

    label('loc_27B8')

    Jump('loc_2A24')

    def _loc_27BB(): pass

    label('loc_27BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_28BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_286C',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，对自己的\n',
            '手艺感到不满啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最大的原因还是\n',
            '觉得菜式固定化了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然以前也经常\n',
            '挑战新的料理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是还要吸收\n',
            '更多更多的要素才行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_28BA')

    def _loc_286C(): pass

    label('loc_286C')

    ChrTalk(
        0x00FE,
        (
            '虽然以前也经常\n',
            '挑战新的料理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是还要吸收\n',
            '更多更多的要素才行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28BA(): pass

    label('loc_28BA')

    Jump('loc_2A24')

    def _loc_28BD(): pass

    label('loc_28BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_28F4',
    )

    ChrTalk(
        0x00FE,
        (
            '副队长他们突然就走了，\n',
            '发生什么事了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A24')

    def _loc_28F4(): pass

    label('loc_28F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_2956',
    )

    ChrTalk(
        0x00FE,
        (
            '队长和副队长一脸严肃地\n',
            '在开会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了呢？\n',
            '连我也不知不觉紧张起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A24')

    def _loc_2956(): pass

    label('loc_2956')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_29A4',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～这个味道\n',
            '也差不多快吃腻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '士兵们好像\n',
            '也不太喜欢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A24')

    def _loc_29A4(): pass

    label('loc_29A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_29FA',
    )

    ChrTurnDirection(0x00FE, 0x012F, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，小姐，\n',
            '白裙子非常适合你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不介意的话，吃点什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A24')

    def _loc_29FA(): pass

    label('loc_29FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2A24',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎～\n',
            '欢迎来到格鲁纳门食堂！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A24(): pass

    label('loc_2A24')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x2A28
@scena.Code('func_0B_2A28')
def func_0B_2A28():
    TalkBegin(0x000D)

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_2AA5',
    )

    FadeOut(300, 0, 100)

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
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A8E',
    )

    Call(0, 0x000C)

    Jump('loc_2AA2')

    def _loc_2A8E(): pass

    label('loc_2A8E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AA2',
    )

    Call(1, 0x0003)

    Jump('loc_2AA2')

    def _loc_2AA2(): pass

    label('loc_2AA2')

    Jump('loc_2ACC')

    def _loc_2AA5(): pass

    label('loc_2AA5')

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_2AC8',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_2AC1',
    )

    Call(1, 0x0001)

    Jump('loc_2AC5')

    def _loc_2AC1(): pass

    label('loc_2AC1')

    Call(1, 0x0000)

    def _loc_2AC5(): pass

    label('loc_2AC5')

    Jump('loc_2ACC')

    def _loc_2AC8(): pass

    label('loc_2AC8')

    Call(0, 0x000C)
    def _loc_2ACC(): pass

    label('loc_2ACC')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x2AD0
@scena.Code('func_0C_2AD0')
def func_0C_2AD0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2B08',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，就拜托各位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不要出事故哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

    def _loc_2B08(): pass

    label('loc_2B08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2C5C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_2B86',
    )

    ChrTalk(
        0x00FE,
        (
            '钓鱼场的调查有进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雾也散了，\n',
            '应该容易很多了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前去不了的地方\n',
            '麻烦特别仔细调查哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C59')

    def _loc_2B86(): pass

    label('loc_2B86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2BCE',
    )

    ChrTalk(
        0x00FE,
        (
            '那么……\n',
            '总算雾也散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我差不多\n',
            '也该准备出发了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C59')

    def _loc_2BCE(): pass

    label('loc_2BCE')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '那么……\n',
            '总算雾也散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我差不多\n',
            '也该准备出发了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于雾调查的计划\n',
            '大幅度延迟了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再不努力调查\n',
            '团长可要发火了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C59(): pass

    label('loc_2C59')

    Jump('loc_2E81')

    def _loc_2C5C(): pass

    label('loc_2C5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2D2C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_2CD7',
    )

    ChrTalk(
        0x00FE,
        (
            '洛连特周边\n',
            '好像还是有很厉害的雾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '钓鱼场的调查\n',
            '别着急慢慢来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '脚踏实地地\n',
            '做就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D29')

    def _loc_2CD7(): pass

    label('loc_2CD7')

    ChrTalk(
        0x00FE,
        (
            '洛连特周边的雾\n',
            '好像还没散去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，那种状态\n',
            '到底要持续到什么时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D29(): pass

    label('loc_2D29')

    Jump('loc_2E81')

    def _loc_2D2C(): pass

    label('loc_2D2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2DCB',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_2D7C',
    )

    ChrTalk(
        0x00FE,
        (
            '游击士们\n',
            '也要多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天早上雾好象\n',
            '还是很大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC8')

    def _loc_2D7C(): pass

    label('loc_2D7C')

    ChrTalk(
        0x00FE,
        (
            '听说今天早上的雾\n',
            '比昨天更厉害了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下要\n',
            '去街道上实在是太勉强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DC8(): pass

    label('loc_2DC8')

    Jump('loc_2E81')

    def _loc_2DCB(): pass

    label('loc_2DCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2E81',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_2E23',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，怎样？\n',
            '调查有进展吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雾好像很厉害，\n',
            '不着急慢慢来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E81')

    def _loc_2E23(): pass

    label('loc_2E23')

    ChrTalk(
        0x00FE,
        (
            '唉……真无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，起这么大雾、\n',
            '钓鱼也太勉强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在就赏赏花\n',
            '消遣消遣吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E81(): pass

    label('loc_2E81')

    Return()

# id: 0x000D offset: 0x2E82
@scena.Code('func_0D_2E82')
def func_0D_2E82():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呀，艾丝蒂尔你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '委托者们好像比想象中的\n',
            '更加疲惫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '决定今天就在格鲁纳门这休息，\n',
            '明天再出发去王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x2F01
@scena.Code('func_0E_2F01')
def func_0E_2F01():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '想着雾中不知何时\n',
            '会有魔兽来袭，\n',
            '真是吓得要死……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易来到这里，\n',
            '已经精疲力竭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2F67
@scena.Code('func_0F_2F67')
def func_0F_2F67():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呼，总算镇定下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '心宽下来，\n',
            '肚子就饿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2FA5
@scena.Code('func_10_2FA5')
def func_10_2FA5():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呼，那个雾\n',
            '到底是什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是没有游击士陪同，\n',
            '实在太危险了，根本出不去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x3002
@scena.Code('func_11_3002')
def func_11_3002():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '雾散了的时候\n',
            '真是松了口气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到了这里，似乎离王都\n',
            '就很近了，可以放心了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x305F
@scena.Code('func_12_305F')
def func_12_305F():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    CameraMove(-16190, 4000, 40000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1500, 0)
    Sleep(500)

    PlaySE(198, 0x00, 0x64)
    Sleep(1000)

    CreateThread(0x0109, 0x01, 0x00, func_13_3BEE)
    Sleep(1800)

    CreateThread(0x0101, 0x01, 0x00, func_14_3C4A)
    CameraMove(-20500, 4000, 40500, 2000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010261100V#1005F等一下！\n',
            '到底是怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0109, 0x0101, 400)

    ChrTalk(
        0x0109,
        (
            '#0180261101V#1066F#5P啊～……\n',
            '还是不能接受？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261102V#1019F那、那还用说！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261103V#1005F你……\n',
            '到底是什么人！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261104V知道我们的活动\n',
            '和『结社』的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261105V真的只是个单纯的神父而已！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261106V#1060F#5P真真正正，七耀教会的神父哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261107V不过确实……\n',
            '暂时知道我不只是个单纯的神父就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261108V#1009F那这是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261109V#1065F#5P这个稍后再解释吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261110V#1063F刚才也说过\n',
            '现在应该赶紧回协会才是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261111V说不定发生了\n',
            '不得了的大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261112V#1020F不得了的大事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261113V#1007F啊啊受不了……脑子\n',
            '现在一片混乱了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261114V#1027F为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261115V为什么本该能见到约修亚的，\n',
            '却变成这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261116V#1063F#5P这是你那男朋友\n',
            '留下的信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261117V那个，真的是你男朋友写的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261118V#1004F啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261119V#1026F唔，嗯。\n',
            '从转交信的孩子的描述看来\n',
            '只可能是约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261120V#1063F#5P那孩子应该不\n',
            '认识你男朋友吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261121V这样的话，别人故意准备\n',
            '一个特征相似的人来也是可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261122V#1026F但、但是……\n',
            '这很像约修亚的字……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261123V#1065F#5P笔迹这种东西\n',
            '某种程度是能模仿的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261124V要骗骗动摇中的人\n',
            '是很简单的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261125V#1063F请看看我从大圣堂\n',
            '收到的信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '凯文神父从怀中取出一封信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD('ED6_DT24/C_VIS128._CH', 0x00BE, 0x0082, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(380, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010230783V#1020F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1500)

    ChrTalk(
        0x0109,
        (
            '#0180261127V#1060F#5P嘿嘿，看来\n',
            '好像是同样的信封呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261128V信的内容里说\n',
            '能提供我正在\n',
            '调查的事情的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261129V#1020F这么说来……\n',
            '是同一人干的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261130V到底是谁，为什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261131V#1067F#5P这我也不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261132V#1068F能确定的……\n',
            '就是我们都被算计了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261133V#1020F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0101, 5)
    OP_0D()
    Sleep(500)

    OP_9E(0x0101, 15, 0, 300, 4000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010261134V#1022F……别开……笑了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261135V#1064F#5P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261136V#1022F虽然不知道是什么人，\n',
            '但别开玩笑了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261137V装作约修亚\n',
            '把我叫出来？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261138V#1027F不能原谅……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010261139V#1023F#3S绝对不能原谅！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261140V#1070F#5P呼啊……\n',
            '冷静点，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0109,
        (
            '#0180261141V#1065F#5P在这里生气，\n',
            '简直是正中对方下怀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261142V#1060F总之先回协会\n',
            '整理情报吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010261143V#1007F明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261144V#1019F但是凯文先生……\n',
            '我还不是完全相信你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261145V如果骗我……\n',
            '就真的会打飞你哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261146V#1062F#5P啊啊，没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261147V被艾丝蒂尔\n',
            '打飞也是我的宿愿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261148V#1061F为了喜欢的女孩，\n',
            '我可是做好了粉身碎骨的准备⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261149V#1013F说、说什么呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261150V#1007F真是的……\n',
            '真会得意忘形。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261151V#1061F#5P治愈系是我的目标嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261152V#1060F那么艾丝蒂尔。\n',
            '赶快返回协会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261153V#1002F嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C7, 0, 0x1638))
    OP_28(0x008D, 0x01, 0x0004)
    OP_28(0x008D, 0x01, 0x0008)
    OP_28(0x008D, 0x01, 0x0010)
    OP_28(0x008D, 0x01, 0x0020)
    OP_28(0x008D, 0x04, 0x10)
    OP_20(0x000003E8)
    EventEnd(0x00)
    PlayBGM(16)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0013 offset: 0x3BEE
@scena.Code('func_13_3BEE')
def func_13_3BEE():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -15020, 4000, 36500, 0)

    @scena.Lambda('lambda_3C15')
    def lambda_3C15():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3C15)

    ChrWalkTo(0x00FE, -15020, 4000, 39930, 2000, 0x00)
    ChrWalkTo(0x00FE, -20890, 4000, 39930, 2000, 0x00)

    Return()

# id: 0x0014 offset: 0x3C4A
@scena.Code('func_14_3C4A')
def func_14_3C4A():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -15020, 4000, 36500, 0)

    @scena.Lambda('lambda_3C71')
    def lambda_3C71():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3C71)

    ChrWalkTo(0x00FE, -15020, 4000, 39930, 2500, 0x00)
    ChrWalkTo(0x00FE, -18540, 4000, 39930, 2500, 0x00)

    Return()

# id: 0x0015 offset: 0x3CA6
@scena.Code('func_15_3CA6')
def func_15_3CA6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3FD3',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DCB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3D34',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240201V#070F虽说徒步行走是修行，\n',
            '但那样太浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271567V要去柏斯的话，\n',
            '还是用定期船比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DC8')

    def _loc_3D34(): pass

    label('loc_3D34')

    ChrTalk(
        0x0108,
        (
            '#0080271568V#070F这里是洛连特地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240204V虽说徒步行走是修行，\n',
            '但那样太浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271567V要去柏斯的话，\n',
            '还是用定期船比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_3DC8(): pass

    label('loc_3DC8')

    Jump('loc_3FB5')

    def _loc_3DCB(): pass

    label('loc_3DCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3EC7',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DE8',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_3DEF')

    def _loc_3DE8(): pass

    label('loc_3DE8')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_3DEF(): pass

    label('loc_3DEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3E63',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240206V#053F……要走过去\n',
            '说实话太浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271572V#050F要去柏斯、\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EC4')

    def _loc_3E63(): pass

    label('loc_3E63')

    ChrTalk(
        0x0106,
        (
            '#0050271277V#050F这里是洛连特地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271574V要去柏斯的话，\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_3EC4(): pass

    label('loc_3EC4')

    Jump('loc_3FB5')

    def _loc_3EC7(): pass

    label('loc_3EC7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EDD',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_3EE4')

    def _loc_3EDD(): pass

    label('loc_3EDD')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_3EE4(): pass

    label('loc_3EE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3F58',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240210V#026F……要走过去\n',
            '说实话是浪费时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271576V#020F要去柏斯、\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FB5')

    def _loc_3F58(): pass

    label('loc_3F58')

    ChrTalk(
        0x0103,
        (
            '#0030271577V#020F这里是洛连特地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271578V要去柏斯、\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_3FB5(): pass

    label('loc_3FB5')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_429F')

    def _loc_3FD3(): pass

    label('loc_3FD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_4085',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_402A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010271282V#1002F没时间闲逛了。\n',
            '……要赶快返回协会才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4067')

    def _loc_402A(): pass

    label('loc_402A')

    ChrTalk(
        0x0109,
        (
            '#0180271283V#1063F没时间闲逛了。\n',
            '……赶紧去王都协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4067(): pass

    label('loc_4067')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_429F')

    def _loc_4085(): pass

    label('loc_4085')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 7, 0x1637)),
            Expr.Return,
        ),
        'loc_40F8',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010271281V#1003F（……我真是的，要去哪里啊。\n',
            '  约修亚在长城上面哦？)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_429F')

    def _loc_40F8(): pass

    label('loc_40F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_429F',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4174',
    )

    ChrTalk(
        0x0108,
        (
            '#0080271275V#070F噢，这前面是洛连特地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271276V现在没空去其他的地方了，\n',
            '赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4284')

    def _loc_4174(): pass

    label('loc_4174')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_41FD',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4191',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_4198')

    def _loc_4191(): pass

    label('loc_4191')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_4198(): pass

    label('loc_4198')

    ChrTalk(
        0x0106,
        (
            '#0050271277V#050F这里是洛连特地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220142V没时间去别的地方了。\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4284')

    def _loc_41FD(): pass

    label('loc_41FD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4213',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_421A')

    def _loc_4213(): pass

    label('loc_4213')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_421A(): pass

    label('loc_421A')

    ChrTalk(
        0x0103,
        (
            '#0030271279V#020F这里出去就是洛连特地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220144V没时间去其它的地方了，\n',
            '现在还是乖乖回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4284(): pass

    label('loc_4284')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_429F(): pass

    label('loc_429F')

    Return()

# id: 0x0016 offset: 0x42A0
@scena.Code('func_16_42A0')
def func_16_42A0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_451D',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43C7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_432C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300136V#070F……通过这里好象\n',
            '是往柏斯的方向啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300137V要离开洛连特，\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43C4')

    def _loc_432C(): pass

    label('loc_432C')

    ChrTalk(
        0x0108,
        (
            '#0080300138V#070F这边是格兰赛尔地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300139V……通过这里到底是\n',
            '是不是往柏斯方向啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300137V要离开洛连特，\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_43C4(): pass

    label('loc_43C4')

    Jump('loc_44FF')

    def _loc_43C7(): pass

    label('loc_43C7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43DD',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_43E4')

    def _loc_43DD(): pass

    label('loc_43DD')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_43E4(): pass

    label('loc_43E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4463',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300141V#020F……通过这里的话，\n',
            '那就没有去柏斯的时间啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300142V要离开洛连特，\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44FF')

    def _loc_4463(): pass

    label('loc_4463')

    ChrTalk(
        0x0103,
        (
            '#0030300143V#020F这边是格兰赛尔地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300144V……通过这里的话，\n',
            '那就没有去柏斯的时间啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300142V要离开洛连特，\n',
            '还是去定期船飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_44FF(): pass

    label('loc_44FF')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_4908')

    def _loc_451D(): pass

    label('loc_451D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Return,
        ),
        'loc_4640',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4599',
    )

    ChrTalk(
        0x0108,
        (
            '#0080291599V#070F噢，这边是格兰赛尔地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271276V现在没空去其他的地方了，\n',
            '赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4622')

    def _loc_4599(): pass

    label('loc_4599')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45AF',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_45B6')

    def _loc_45AF(): pass

    label('loc_45AF')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_45B6(): pass

    label('loc_45B6')

    ChrTalk(
        0x0103,
        (
            '#0030291601V#022F这前面是格兰赛尔地区哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291602V……没空绕道去王都了。\n',
            '赶紧去东边的神秘森林吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4622(): pass

    label('loc_4622')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_4908')

    def _loc_4640(): pass

    label('loc_4640')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Return,
        ),
        'loc_47FA',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_465F',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_4666')

    def _loc_465F(): pass

    label('loc_465F')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_4666(): pass

    label('loc_4666')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_46CE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030291601V#022F这前面是格兰赛尔地区哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291604V绕道就算了吧，\n',
            '赶紧去帕赛尔农场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47DC')

    def _loc_46CE(): pass

    label('loc_46CE')

    ChrTalk(
        0x0103,
        (
            '#0030291601V#022F这前面是格兰赛尔地区哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291604V绕道就算了吧，\n',
            '赶紧去帕赛尔农场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4768',
    )

    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010291607V#1002F啊、嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_4768(): pass

    label('loc_4768')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_479F',
    )

    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0105,
        (
            '#0060291608V#042F是，对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_479F(): pass

    label('loc_479F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47DC',
    )

    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0107,
        (
            '#0070291609V#062F是、是，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_47DC(): pass

    label('loc_47DC')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_4908')

    def _loc_47FA(): pass

    label('loc_47FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4908',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4876',
    )

    ChrTalk(
        0x0108,
        (
            '#0080291599V#070F噢，这边是格兰赛尔地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271276V现在没空去其他的地方了，\n',
            '赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_48ED')

    def _loc_4876(): pass

    label('loc_4876')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_488C',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_4893')

    def _loc_488C(): pass

    label('loc_488C')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_4893(): pass

    label('loc_4893')

    ChrTalk(
        0x0103,
        (
            '#0030291612V#020F穿过这里就是格兰赛尔地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291613V没空绕道了。\n',
            '赶快回头吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48ED(): pass

    label('loc_48ED')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4908(): pass

    label('loc_4908')

    Return()

# id: 0x0017 offset: 0x4909
@scena.Code('func_17_4909')
def func_17_4909():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
