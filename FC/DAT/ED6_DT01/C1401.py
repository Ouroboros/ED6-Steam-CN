import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1401   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1401.x'
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
            word_3A         = 60,
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
        ('ED6_DT09/CH10170._CH', 'ED6_DT09/CH10170P._CP'),
        ('ED6_DT09/CH10171._CH', 'ED6_DT09/CH10171P._CP'),
        ('ED6_DT09/CH11170._CH', 'ED6_DT09/CH11170P._CP'),
        ('ED6_DT09/CH11171._CH', 'ED6_DT09/CH11171P._CP'),
        ('ED6_DT09/CH11180._CH', 'ED6_DT09/CH11180P._CP'),
        ('ED6_DT09/CH11181._CH', 'ED6_DT09/CH11181P._CP'),
        ('ED6_DT09/CH11190._CH', 'ED6_DT09/CH11190P._CP'),
        ('ED6_DT09/CH11191._CH', 'ED6_DT09/CH11191P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卫兵',
            x                   = 1220,
            z                   = -2070,
            y                   = 185310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卫兵',
            x                   = 4000,
            z                   = -2070,
            y                   = 185310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x132
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -31230,
            z           = -30,
            y           = 76720,
            word_0C     = 0x00A5,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -22600,
            z           = 0,
            y           = 45730,
            word_0C     = 0x00E1,
            word_0E     = 0x0005,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00BA,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -1980,
            z           = 40,
            y           = 82660,
            word_0C     = 0x00A4,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00BD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 8330,
            z           = -1840,
            y           = 91320,
            word_0C     = 0x0072,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 2350,
            z           = -1960,
            y           = 58080,
            word_0C     = 0x009C,
            word_0E     = 0x0007,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00BB,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -31080,
            z           = -1990,
            y           = 103160,
            word_0C     = 0x002B,
            word_0E     = 0x0007,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00BE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 5530,
            z           = -1920,
            y           = 140390,
            word_0C     = 0x0125,
            word_0E     = 0x0007,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00BE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 10740,
            z           = -2009,
            y           = 162000,
            word_0C     = 0x011C,
            word_0E     = 0x0005,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 10420,
            z           = -1910,
            y           = 77510,
            word_0C     = 0x0067,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -21780,
            z           = -2050,
            y           = 78280,
            word_0C     = 0x00A2,
            word_0E     = 0x0005,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00B8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x24A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -330,
            y           = -4000,
            z           = 184860,
            range       = 5340,
            dword_10    = 0x000003E8,
            dword_14    = 0x0002C808,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -26110,
            y           = -4000,
            z           = 69000,
            range       = -38850,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00011558,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x28A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -9350,
            triggerZ            = -1950,
            triggerY            = 71290,
            triggerRange        = 1500,
            actorX              = -9350,
            actorZ              = -450,
            actorY              = 71290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 19360,
            triggerZ            = -1990,
            triggerY            = 166110,
            triggerRange        = 1000,
            actorX              = 19810,
            actorZ              = -490,
            actorY              = 166800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2D2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2E9',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_03_36E)

    def _loc_2E9(): pass

    label('loc_2E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_2F7',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_04_3D6)

    def _loc_2F7(): pass

    label('loc_2F7')

    MapSetFlags(0x00000010)
    OP_11(0xFF, 0xFF, 0xFF, 33000, 54000, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 5, 0x35D)),
            Expr.Return,
        ),
        'loc_31D',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    def _loc_31D(): pass

    label('loc_31D')

    Return()

# id: 0x0001 offset: 0x31E
@scena.Code('func_01_31E')
def func_01_31E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 5, 0x35D)),
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 7, 0x357)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_32E',
    )

    OP_71(0x0000, 0x0004)

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 3, 0x363)),
            Expr.Return,
        ),
        'loc_33E',
    )

    OP_71(0x0001, 0x0004)
    OP_64(0x00, 0x0001)

    def _loc_33E(): pass

    label('loc_33E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 7, 0x377)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_350',
    )

    OP_6F(0x0002, 0)

    Jump('loc_357')

    def _loc_350(): pass

    label('loc_350')

    OP_6F(0x0002, 60)

    def _loc_357(): pass

    label('loc_357')

    Return()

# id: 0x0002 offset: 0x358
@scena.Code('func_02_358')
def func_02_358():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_36D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_358')

    def _loc_36D(): pass

    label('loc_36D')

    Return()

# id: 0x0003 offset: 0x36E
@scena.Code('func_03_36E')
def func_03_36E():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-6987, -2000, 112486, 0)
    CameraSetDistance(4500, 0)
    OP_6C(288000, 0)

    @scena.Lambda('lambda_039E')
    def lambda_039E():
        CameraMove(630, 3040, 186710, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_039E)

    @scena.Lambda('lambda_03B6')
    def lambda_03B6():
        CameraSetDistance(2500, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_03B6)

    OP_6C(48000, 10000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C1301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x3D6
@scena.Code('func_04_3D6')
def func_04_3D6():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(2616, -2000, 188840, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)

    @scena.Lambda('lambda_0406')
    def lambda_0406():
        OP_67(0, 3600, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0406)

    @scena.Lambda('lambda_041E')
    def lambda_041E():
        CameraSetDistance(3400, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_041E)

    OP_6C(24000, 4000)
    Sleep(1000)

    PlaySE(193, 0x00, 0x64)
    PlayEffect(0x12, 0xFF, 0x00FF, 2616, -2000, 188840, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0101, 2780, -2020, 190580, 209)
    ChrSetPos(0x0103, 2140, -2029, 191100, 190)
    ChrSetPos(0x0102, 2780, -2020, 191990, 178)
    ChrSetPos(0x0104, 2380, -2029, 192390, 184)
    OP_71(0x0000, 0x0004)
    CameraSetDistance(3470, 0)
    CameraSetDistance(3400, 80)
    Sleep(1000)

    @scena.Lambda('lambda_04D6')
    def lambda_04D6():
        CameraMove(2180, -1900, 181510, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_04D6)

    @scena.Lambda('lambda_04EE')
    def lambda_04EE():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_04EE)

    @scena.Lambda('lambda_04FE')
    def lambda_04FE():
        OP_6E(318, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_04FE)

    @scena.Lambda('lambda_050E')
    def lambda_050E():
        ChrWalkTo(0x00FE, 2430, -1960, 184270, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_050E)

    Sleep(200)

    @scena.Lambda('lambda_052E')
    def lambda_052E():
        ChrWalkTo(0x00FE, 1730, -2000, 185340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_052E)

    Sleep(200)

    @scena.Lambda('lambda_054E')
    def lambda_054E():
        ChrWalkTo(0x00FE, 3460, -1960, 184760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_054E)

    Sleep(200)

    @scena.Lambda('lambda_056E')
    def lambda_056E():
        ChrWalkTo(0x00FE, 2900, -1970, 185880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_056E)

    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#0010031533V#004F是、是暗门呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031534V#033F不愧是古老的隐藏堡垒。\n',
            '这可真是华丽的欺骗技巧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031535V#012F这里是……\n',
            '『迷雾峡谷』的一个角落吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031536V雪拉姐姐，\n',
            '先让人质从这里逃走吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_066F')
    def lambda_066F():
        ChrTurnDirection(0x00FE, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_066F)

    @scena.Lambda('lambda_067D')
    def lambda_067D():
        ChrTurnDirection(0x00FE, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_067D)

    ChrTurnDirection(0x0103, 0x0102, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031537V#022F不……\n',
            '还是先去抓空贼的首领。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031538V要是人质逃走时候遇到袭击的话，\n',
            '单凭我们几个是无法保护那么多人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031539V#002F啊，对啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031540V#035F哈·哈·哈。\n',
            '那我们赶快回去和空贼首领对决吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x006A, 7, 0x357))
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x77C
@scena.Code('func_05_77C')
def func_05_77C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 5, 0x35D)),
            Expr.Return,
        ),
        'loc_826',
    )

    EventBegin(0x01)
    OP_4A(0x0008, 0)
    ChrTurnDirection(0x0008, 0x0000, 400)

    @scena.Lambda('lambda_0796')
    def lambda_0796():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0796)

    ChrTurnDirection(0x0001, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#2420031773V现在里面正在进行调查，\n',
            '平民不得入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420031774V对不起，请回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    ChrSetDirection(0x0008, 180, 0)
    OP_4B(0x0008, 0)
    Sleep(50)

    EventEnd(0x04)

    def _loc_826(): pass

    label('loc_826')

    Return()

# id: 0x0006 offset: 0x827
@scena.Code('func_06_827')
def func_06_827():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 3, 0x353)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 5, 0x35D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_977',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D6',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    @scena.Lambda('lambda_084E')
    def lambda_084E():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_084E)

    @scena.Lambda('lambda_085C')
    def lambda_085C():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_085C)

    ChrTurnDirection(0x0104, 0x0103, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031683V#022F还没有把空贼头目抓住，\n',
            '现在离开的话太危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031684V……回空贼基地里去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_95C')

    def _loc_8D6(): pass

    label('loc_8D6')

    ChrTurnDirection(0x0103, 0x0000, 400)

    @scena.Lambda('lambda_08E3')
    def lambda_08E3():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_08E3)

    @scena.Lambda('lambda_08F1')
    def lambda_08F1():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_08F1)

    ChrTurnDirection(0x0104, 0x0103, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031685V#022F等一下，\n',
            '还没有把空贼头目抓住呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031686V赶快回空贼基地里去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_95C(): pass

    label('loc_95C')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_977(): pass

    label('loc_977')

    Return()

# id: 0x0007 offset: 0x978
@scena.Code('func_07_978')
def func_07_978():
    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x02)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0011, 0x01, 0x0004)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A66',
    )

    MapSetFlags(0x08000000)
    OP_28(0x0011, 0x01, 0x8000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 3, 0x363)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A5B',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x0386, 1)"),
            Expr.Return,
        ),
        'loc_A09',
    )

    OP_71(0x0001, 0x0004)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x006C, 3, 0x363))

    Jump('loc_A5B')

    def _loc_A09(): pass

    label('loc_A09')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '发现了，\n',
            (TxtCtl.SetColor, 0x0),
            '不过现有的数量太多，不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_A5B(): pass

    label('loc_A5B')

    MapClearFlags(0x08000000)
    TalkEnd(0x00FF)

    Jump('loc_127C')

    def _loc_A66(): pass

    label('loc_A66')

    OP_28(0x0011, 0x01, 0x0004)
    MapSetFlags(0x08000000)
    EventBegin(0x00)
    Fade(1000)
    OP_6C(125000, 0)
    ChrSetPos(0x0101, -7970, -2000, 71470, 270)
    ChrSetPos(0x0102, -7850, -2070, 72520, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AC2',
    )

    ChrSetPos(0x0103, -6790, -2009, 71120, 270)

    def _loc_AC2(): pass

    label('loc_AC2')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AE1',
    )

    ChrSetPos(0x0104, -6370, -2009, 72240, 270)

    def _loc_AE1(): pass

    label('loc_AE1')

    OP_69(0x0101, 0)
    OP_6C(135000, 2000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 3, 0x363)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BA8',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x0386, 1)"),
            Expr.Return,
        ),
        'loc_B56',
    )

    OP_71(0x0001, 0x0004)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x006C, 3, 0x363))

    Jump('loc_BA8')

    def _loc_B56(): pass

    label('loc_B56')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '发现了，\n',
            (TxtCtl.SetColor, 0x0),
            '不过现有的数量太多，不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_BA8(): pass

    label('loc_BA8')

    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_1127',
    )

    ChrTalk(
        0x0101,
        (
            '#0010150990V#000F呼，终～于找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150991V接下来要做的就是\n',
            '把这个地方告诉超市的老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CE5',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030150992V#020F那么，艾丝蒂尔，\n',
            '我问你一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030150993V你知道这里是什么地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150994V#502F嘿嘿，\n',
            '雪拉姐的问题真无聊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150995V『蜜猪峡谷』，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D7E')

    def _loc_CE5(): pass

    label('loc_CE5')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150996V#014F艾丝蒂尔，\n',
            '你知道这个地方叫什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150997V#502F真是的，别把我当傻瓜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150995V『蜜猪峡谷』，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D7E(): pass

    label('loc_D7E')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E54',
    )

    ChrTalk(
        0x0102,
        (
            '#0020150999V#015F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040151000V#030F哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040151001V不管怎么说\n',
            '真是个能引起食欲的名字啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151002V#017F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151003V这里叫『迷雾峡谷』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F6A')

    def _loc_E54(): pass

    label('loc_E54')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F0D',
    )

    ChrTalk(
        0x0102,
        (
            '#0020150999V#015F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151005V#027F……真是个非常美味的名字啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151002V#017F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151003V这里叫『迷雾峡谷』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F6A')

    def _loc_F0D(): pass

    label('loc_F0D')

    ChrTalk(
        0x0102,
        (
            '#0020150486V#018F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151009V#018F艾丝蒂尔……\n',
            '这里叫『迷雾峡谷』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F6A(): pass

    label('loc_F6A')

    ChrTalk(
        0x0101,
        (
            '#0010151010V#008F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FCE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030151011V#025F……还好事先问了你一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_1004')

    def _loc_FCE(): pass

    label('loc_FCE')

    ChrTalk(
        0x0102,
        (
            '#0020151012V#015F……还好事先问了你一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    def _loc_1004(): pass

    label('loc_1004')

    ChrTalk(
        0x0101,
        (
            '#0010151013V#009F这、这也是没办法的事情啊，\n',
            '人家正处于生长发育旺盛的时期嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151014V#018F这算什么理由啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151015V#008F好、好啦好啦，\n',
            '我们这是在工作中啊，工作中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151016V快点出发吧，好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)

    ChrTalk(
        0x0102,
        (
            '#0020151017V#017F真拿你没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1275')

    def _loc_1127(): pass

    label('loc_1127')

    ChrTalk(
        0x0101,
        (
            '#0010151018V#000F嗯～这是『熊刺草』呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151019V说起来……\n',
            '好像有谁正在找这个东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11F7',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151020V#020F不是在公告板上写着的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151021V看看手册里的记载吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_1254')

    def _loc_11F7(): pass

    label('loc_11F7')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151022V#010F是在公告板上写着的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151023V看看手册里的记载吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    def _loc_1254(): pass

    label('loc_1254')

    ChrTalk(
        0x0101,
        (
            '#0010151024V#006F嗯，好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1275(): pass

    label('loc_1275')

    EventEnd(0x00)
    MapClearFlags(0x08000000)
    def _loc_127C(): pass

    label('loc_127C')

    Return()

# id: 0x0008 offset: 0x127D
@scena.Code('func_08_127D')
def func_08_127D():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 7, 0x377)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1373',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x0116, 1)"),
            Expr.Return,
        ),
        'loc_12F5',
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
            '斯托雷加Ｒ',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x006E, 7, 0x377))

    Jump('loc_1370')

    def _loc_12F5(): pass

    label('loc_12F5')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '斯托雷加Ｒ',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '斯托雷加Ｒ',
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

    def _loc_1370(): pass

    label('loc_1370')

    Jump('loc_13A9')

    def _loc_1373(): pass

    label('loc_1373')

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
    WaitEffect(0x0F, 0x16)
    def _loc_13A9(): pass

    label('loc_13A9')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
