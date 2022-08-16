import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1302   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1302.x'
    header.mapIndex       = 52
    header.bgm            = 31
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
            word_3A         = 52,
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
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乔丝特',
            x                   = -35700,
            z                   = 0,
            y                   = -85400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '吉尔',
            x                   = -36200,
            z                   = 0,
            y                   = -84300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '多伦',
            x                   = -34100,
            z                   = 0,
            y                   = -82100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 52155,
            z                   = -3000,
            y                   = 17688,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 48810,
            z                   = -3000,
            y                   = 27604,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 72117,
            z                   = 3000,
            y                   = 28437,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 36188,
            z                   = 0,
            y                   = 16750,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军军官',
            x                   = 48683,
            z                   = -3000,
            y                   = 29357,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '理查德上校',
            x                   = 47780,
            z                   = 0,
            y                   = 39390,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = 47780,
            z                   = 0,
            y                   = 39390,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '摩尔根将军',
            x                   = 209710,
            z                   = 0,
            y                   = 11740,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 52155,
            z                   = -3000,
            y                   = 17688,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 48810,
            z                   = -3000,
            y                   = 27604,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 72117,
            z                   = 3000,
            y                   = 28437,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 36188,
            z                   = 0,
            y                   = 16750,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 36188,
            z                   = 0,
            y                   = 16750,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 36188,
            z                   = 0,
            y                   = 16750,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x362
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x362
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x362
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x362
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_36E'),
        (-1, 'loc_380'),
    )

    def _loc_36E(): pass

    label('loc_36E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 4, 0x35C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37D',
    )

    SetScenaFlags(ScenaFlag(0x006B, 4, 0x35C))
    Event(0, func_03_398)

    def _loc_37D(): pass

    label('loc_37D')

    Jump('loc_380')

    def _loc_380(): pass

    label('loc_380')

    Return()

# id: 0x0001 offset: 0x381
@scena.Code('func_01_381')
def func_01_381():
    Return()

# id: 0x0002 offset: 0x382
@scena.Code('func_02_382')
def func_02_382():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_397',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_382')

    def _loc_397(): pass

    label('loc_397')

    Return()

# id: 0x0003 offset: 0x398
@scena.Code('func_03_398')
def func_03_398():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-17060, 3750, -15530, 0)
    OP_67(0, 5310, -10000, 0)
    CameraSetDistance(3740, 0)
    OP_6C(102000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0101, -16500, 2000, -14000, 180)
    ChrSetPos(0x0103, -17120, 2000, -13840, 180)
    ChrSetPos(0x0102, -16600, 2000, -12660, 180)
    ChrSetPos(0x0104, -17460, 2000, -12310, 180)
    ChrSetPos(0x000B, -13140, 4000, -23900, 180)
    ChrSetPos(0x000A, -13220, 4000, -22610, 180)
    ChrSetPos(0x000D, -11860, 4000, -22360, 180)
    ChrSetPos(0x0008, -13031, 4000, -21770, 233)
    ChrSetPos(0x000C, -13750, 4000, -21750, 180)
    ChrSetPos(0x0009, -12600, 4000, -21120, 64)
    ChrSetPos(0x000F, -12300, 4000, -20010, 180)
    ChrTurnDirection(0x000B, 0x000A, 0)
    ChrTurnDirection(0x000C, 0x000A, 0)
    ChrTurnDirection(0x000D, 0x000A, 0)
    ChrTurnDirection(0x000F, 0x000A, 0)
    ChrSetPos(0x0013, -17040, 4000, -24290, 0)
    ChrSetPos(0x0014, -16980, 4000, -25880, 0)

    @scena.Lambda('lambda_0508')
    def lambda_0508():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0508')

    DispatchAsync2(0x0014, 0x0001, lambda_0508)

    @scena.Lambda('lambda_0519')
    def lambda_0519():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0519')

    DispatchAsync2(0x0013, 0x0001, lambda_0519)

    FadeIn(1000, 0)
    OP_20(0x000005DC)

    @scena.Lambda('lambda_0538')
    def lambda_0538():
        CameraMove(-15280, 4000, -18760, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0538)

    @scena.Lambda('lambda_0550')
    def lambda_0550():
        ChrWalkTo(0x00FE, -17470, 4000, -16090, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0550)

    Sleep(100)

    @scena.Lambda('lambda_0570')
    def lambda_0570():
        ChrWalkTo(0x00FE, -17330, 4000, -18000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0570)

    Sleep(100)

    @scena.Lambda('lambda_0590')
    def lambda_0590():
        ChrWalkTo(0x00FE, -16680, 4000, -16000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0590)

    @scena.Lambda('lambda_05AB')
    def lambda_05AB():
        ChrWalkTo(0x00FE, -16180, 4000, -17400, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05AB)

    Sleep(100)

    @scena.Lambda('lambda_05CB')
    def lambda_05CB():
        ChrWalkTo(0x00FE, -17500, 4000, -16600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_05CB)

    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0102, 0x0001)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_061E')
    def lambda_061E():
        ChrSetDirection(0x00FE, 134, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_061E)

    WaitForThreadExit(0x0103, 0x0001)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0648')
    def lambda_0648():
        ChrSetDirection(0x00FE, 134, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0648)

    WaitForThreadExit(0x0104, 0x0001)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0672')
    def lambda_0672():
        ChrSetDirection(0x00FE, 134, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0672)

    Sleep(1000)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010031705V#004F#1P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0102,
        (
            '#0020031706V#014F这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_21()

    @scena.Lambda('lambda_0731')
    def lambda_0731():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0731')

    DispatchAsync2(0x0101, 0x0000, lambda_0731)

    @scena.Lambda('lambda_0742')
    def lambda_0742():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0742')

    DispatchAsync2(0x0102, 0x0000, lambda_0742)

    @scena.Lambda('lambda_0753')
    def lambda_0753():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0753')

    DispatchAsync2(0x0103, 0x0000, lambda_0753)

    @scena.Lambda('lambda_0764')
    def lambda_0764():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0764')

    DispatchAsync2(0x0104, 0x0000, lambda_0764)

    PlayBGM(101)

    @scena.Lambda('lambda_0777')
    def lambda_0777():
        CameraMove(-8410, 4000, -22720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0777)

    @scena.Lambda('lambda_078F')
    def lambda_078F():
        OP_6E(437, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_078F)

    @scena.Lambda('lambda_079F')
    def lambda_079F():
        OP_6C(125000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_079F)

    Sleep(2000)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0009,
        (
            '#0290031707V#201F#2P混、混帐。\n',
            '军队怎么会知道这地方的！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031708V那个混蛋，给出的消息又有误！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031709V#214F#5P喂、喂！\n',
            '不要随便碰我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031710V#192F喂喂……\n',
            '这到底是怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08C2')
    def lambda_08C2():
        CameraMove(-14680, 4000, -20970, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08C2)

    @scena.Lambda('lambda_08DA')
    def lambda_08DA():
        OP_67(0, 7970, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_08DA)

    @scena.Lambda('lambda_08F2')
    def lambda_08F2():
        OP_6C(137000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_08F2)

    @scena.Lambda('lambda_0902')
    def lambda_0902():
        OP_6E(244, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0902)

    CreateThread(0x000B, 0x01, 0x00, func_04_1C76)
    Sleep(100)

    CreateThread(0x000A, 0x01, 0x00, func_04_1C76)
    Sleep(200)

    CreateThread(0x000D, 0x01, 0x00, func_04_1C76)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, func_04_1C76)
    Sleep(300)

    CreateThread(0x000C, 0x01, 0x00, func_04_1C76)
    Sleep(300)

    CreateThread(0x0009, 0x01, 0x00, func_04_1C76)
    Sleep(50)

    CreateThread(0x000F, 0x01, 0x00, func_04_1C76)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)
    Sleep(600)

    ChrTalk(
        0x0014,
        (
            '#0280031711V#153F#6P哇～这些人\n',
            '就是空贼团的首领啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280031712V还有女孩子在里面，\n',
            '真是不可思议呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0270031713V#144F#6P别站着动口不动手，\n',
            '快点拍照啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270031714V这样的爆炸性新闻\n',
            '可不是经常能遇到的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetPos(0x0010, -11930, 4000, -33160, 0)
    ChrSetPos(0x0012, -11930, 4000, -33160, 0)
    ChrSetPos(0x0011, -11930, 4000, -33160, 0)
    ChrSetPos(0x0015, -11450, 4050, -36300, 0)
    ChrSetPos(0x0016, -11450, 4050, -36300, 0)
    ChrSetPos(0x0017, -11450, 4050, -36300, 0)
    ChrSetPos(0x0018, -11450, 4050, -36300, 0)
    ChrSetPos(0x0019, -11450, 4050, -36300, 0)
    ChrSetPos(0x001A, -11450, 4050, -36300, 0)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetFlags(0x0015, 0x0040)
    ChrSetFlags(0x0016, 0x0040)
    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x0018, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x001A, 0x0040)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetFlags(0x0012, 0x0004)
    ChrSetFlags(0x0011, 0x0004)

    @scena.Lambda('lambda_0B4B')
    def lambda_0B4B():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_0B4B')

    DispatchAsync2(0x0014, 0x0001, lambda_0B4B)

    @scena.Lambda('lambda_0B5C')
    def lambda_0B5C():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_0B5C')

    DispatchAsync2(0x0013, 0x0001, lambda_0B5C)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)

    @scena.Lambda('lambda_0B7D')
    def lambda_0B7D():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0B7D)

    @scena.Lambda('lambda_0B8B')
    def lambda_0B8B():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B8B)

    @scena.Lambda('lambda_0B99')
    def lambda_0B99():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0B99)

    @scena.Lambda('lambda_0BA7')
    def lambda_0BA7():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0BA7)

    @scena.Lambda('lambda_0BB5')
    def lambda_0BB5():
        CameraMove(-15270, 4000, -25300, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0BB5)

    @scena.Lambda('lambda_0BCD')
    def lambda_0BCD():
        ChrWalkTo(0x00FE, -14420, 4000, -24480, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0BCD)

    Sleep(400)

    @scena.Lambda('lambda_0BED')
    def lambda_0BED():
        ChrWalkTo(0x00FE, -13450, 4000, -25860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0BED)

    Sleep(400)

    @scena.Lambda('lambda_0C0D')
    def lambda_0C0D():
        ChrWalkTo(0x00FE, -14140, 4000, -27020, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0C0D)

    @scena.Lambda('lambda_0C28')
    def lambda_0C28():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C28')

    DispatchAsync2(0x0015, 0x0001, lambda_0C28)

    @scena.Lambda('lambda_0C39')
    def lambda_0C39():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C39')

    DispatchAsync2(0x0016, 0x0001, lambda_0C39)

    @scena.Lambda('lambda_0C4A')
    def lambda_0C4A():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C4A')

    DispatchAsync2(0x0017, 0x0001, lambda_0C4A)

    @scena.Lambda('lambda_0C5B')
    def lambda_0C5B():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C5B')

    DispatchAsync2(0x0018, 0x0001, lambda_0C5B)

    @scena.Lambda('lambda_0C6C')
    def lambda_0C6C():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C6C')

    DispatchAsync2(0x0019, 0x0001, lambda_0C6C)

    @scena.Lambda('lambda_0C7D')
    def lambda_0C7D():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C7D')

    DispatchAsync2(0x001A, 0x0001, lambda_0C7D)

    @scena.Lambda('lambda_0C8E')
    def lambda_0C8E():
        ChrWalkTo(0x00FE, -12200, 4000, -24410, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_0C8E)

    Sleep(400)

    @scena.Lambda('lambda_0CAE')
    def lambda_0CAE():
        ChrWalkTo(0x00FE, -11150, 4000, -24390, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_0CAE)

    Sleep(400)

    @scena.Lambda('lambda_0CCE')
    def lambda_0CCE():
        ChrWalkTo(0x00FE, -11150, 4000, -25510, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_0CCE)

    Sleep(400)

    @scena.Lambda('lambda_0CEE')
    def lambda_0CEE():
        ChrWalkTo(0x00FE, -12270, 4000, -25510, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_0CEE)

    Sleep(400)

    @scena.Lambda('lambda_0D0E')
    def lambda_0D0E():
        ChrWalkTo(0x00FE, -11150, 4000, -26750, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_0D0E)

    Sleep(400)

    @scena.Lambda('lambda_0D2E')
    def lambda_0D2E():
        ChrWalkTo(0x00FE, -12310, 4000, -26750, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_0D2E)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_0D4E')
    def lambda_0D4E():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0D4E)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_0D61')
    def lambda_0D61():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0D61)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_0D74')
    def lambda_0D74():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0D74)

    ChrTalk(
        0x0010,
        (
            '#0130031715V#110F怎么样，奈尔先生。\n',
            '这下可以写出很好的报道吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0270031716V#141F这是当然的啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270031717V您能带我们一起来现场，\n',
            '真是感激不尽啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270031718V#147F啊，等一下能否\n',
            '也让我们为上校拍张照呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    ChrTurnDirection(0x0010, 0x0012, 400)

    ChrTalk(
        0x0010,
        (
            '#0130031719V#113F#6P唔……\n',
            '将军，请问这可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0010, 400)

    ChrTalk(
        0x0012,
        (
            '#0600031720V#163F#2P随你的意思吧，\n',
            '这次的作战方案全是你制定的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600031721V#160F能获得成功的确是你的功劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130031722V#115F#6P将军您言重了，\n',
            '其实这应归功于情报部各位的正确分析。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0130031723V#110F而且，还要感谢\n',
            '那边几位的鼎力相助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0FB1')
    def lambda_0FB1():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0FB1')

    DispatchAsync2(0x0010, 0x0002, lambda_0FB1)

    @scena.Lambda('lambda_0FC2')
    def lambda_0FC2():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0FC2')

    DispatchAsync2(0x0014, 0x0002, lambda_0FC2)

    @scena.Lambda('lambda_0FD3')
    def lambda_0FD3():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0FD3')

    DispatchAsync2(0x0013, 0x0002, lambda_0FD3)

    @scena.Lambda('lambda_0FE4')
    def lambda_0FE4():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0FE4')

    DispatchAsync2(0x0011, 0x0002, lambda_0FE4)

    @scena.Lambda('lambda_0FF5')
    def lambda_0FF5():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0FF5')

    DispatchAsync2(0x0012, 0x0002, lambda_0FF5)

    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0600031724V#161F#2P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)

    @scena.Lambda('lambda_1053')
    def lambda_1053():
        CameraMove(-14680, 4000, -23970, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1053)

    @scena.Lambda('lambda_106B')
    def lambda_106B():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_106B')

    DispatchAsync2(0x0101, 0x0002, lambda_106B)

    @scena.Lambda('lambda_107C')
    def lambda_107C():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_107C')

    DispatchAsync2(0x0102, 0x0002, lambda_107C)

    @scena.Lambda('lambda_108D')
    def lambda_108D():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_108D')

    DispatchAsync2(0x0103, 0x0002, lambda_108D)

    @scena.Lambda('lambda_109E')
    def lambda_109E():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_109E')

    DispatchAsync2(0x0104, 0x0002, lambda_109E)

    @scena.Lambda('lambda_10AF')
    def lambda_10AF():
        ChrWalkTo(0x00FE, -13660, 4000, -20310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10AF)

    Sleep(100)

    @scena.Lambda('lambda_10CF')
    def lambda_10CF():
        ChrWalkTo(0x00FE, -15190, 4000, -20740, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_10CF)

    Sleep(100)

    ChrSetFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_10F4')
    def lambda_10F4():
        ChrWalkTo(0x00FE, -14410, 4000, -19180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_10F4)

    Sleep(100)

    @scena.Lambda('lambda_1114')
    def lambda_1114():
        ChrWalkTo(0x00FE, -15620, 4000, -19480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_1114)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010031725V#505F唔……\n',
            '我还是搞不清状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031726V到底发生了什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0270031727V#143F是、是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0280031728V#151F哇～是小艾他们呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0600031729V#162F游、游击士！\n',
            '为什么你们会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031730V#027F为了慎重起见，\n',
            '我们早一步潜进来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031731V这个据点已经被压制住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031732V#010F我们是追着逃跑的\n',
            '空贼首领到这里来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031733V真没想到\n',
            '王国军的警备飞艇也会来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0600031734V#162F唔唔唔……\n',
            '又擅自做出这种越权的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0012, 400)

    ChrTalk(
        0x0010,
        (
            '#0130031735V#115F#6P虽说如此，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130031736V多亏了他们，\n',
            '我们才能如此顺利地进行突击。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130031737V#110F我们应当承认他们这份功劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0600031738V#163F……唔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600031739V#160F算了，\n',
            '接下来就交给你指挥吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600031740V我先回到飞艇上，\n',
            '空贼一伙也一并押上来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130031741V#110F#6P遵命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0012, 0x0004)
    ChrSetDirection(0x0012, 180, 400)
    CreateThread(0x0012, 0x01, 0x00, func_04_1C76)
    Sleep(400)

    ChrSetDirection(0x001A, 180, 400)
    CreateThread(0x001A, 0x01, 0x00, func_04_1C76)
    Sleep(300)

    ChrSetDirection(0x0019, 180, 400)
    CreateThread(0x0019, 0x01, 0x00, func_04_1C76)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010031742V#007F还真是个顽固的老爷爷～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0130031743V#115F他并不是个不讲理的人，\n',
            '只是有时候缺乏变通而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130031744V#112F对了，\n',
            '其他空贼还有人质在什么地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031745V#020F那些空贼\n',
            '应该还倒在那边。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031746V而人质都在\n',
            '被囚禁的房间待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0130031747V#110F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130031748V嗯，真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130031749V包括人质和货物的遣返，\n',
            '后续工作就交由我们处理吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130031750V走吧，凯诺娜上尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0610031751V#182F遵命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0010, 0x0004)
    ChrClearFlags(0x0011, 0x0004)
    CreateThread(0x0010, 0x01, 0x00, func_05_1CD1)
    Sleep(100)

    CreateThread(0x0011, 0x01, 0x00, func_05_1CD1)

    @scena.Lambda('lambda_167B')
    def lambda_167B():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_167B')

    DispatchAsync2(0x0014, 0x0001, lambda_167B)

    @scena.Lambda('lambda_168C')
    def lambda_168C():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_168C')

    DispatchAsync2(0x0013, 0x0001, lambda_168C)

    @scena.Lambda('lambda_169D')
    def lambda_169D():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_169D')

    DispatchAsync2(0x0101, 0x0002, lambda_169D)

    @scena.Lambda('lambda_16AE')
    def lambda_16AE():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_16AE')

    DispatchAsync2(0x0102, 0x0002, lambda_16AE)

    @scena.Lambda('lambda_16BF')
    def lambda_16BF():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_16BF')

    DispatchAsync2(0x0103, 0x0002, lambda_16BF)

    @scena.Lambda('lambda_16D0')
    def lambda_16D0():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_16D0')

    DispatchAsync2(0x0104, 0x0002, lambda_16D0)

    Sleep(500)

    CreateThread(0x0015, 0x01, 0x00, func_05_1CD1)
    Sleep(200)

    CreateThread(0x0016, 0x01, 0x00, func_05_1CD1)
    Sleep(400)

    CreateThread(0x0018, 0x01, 0x00, func_05_1CD1)
    Sleep(200)

    CreateThread(0x0017, 0x01, 0x00, func_05_1CD1)
    Sleep(300)

    ChrTalk(
        0x0013,
        (
            '#0270031752V#143F啊，请等等上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_173D')
    def lambda_173D():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_173D')

    DispatchAsync2(0x0101, 0x0002, lambda_173D)

    @scena.Lambda('lambda_174E')
    def lambda_174E():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_174E')

    DispatchAsync2(0x0102, 0x0002, lambda_174E)

    @scena.Lambda('lambda_175F')
    def lambda_175F():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_175F')

    DispatchAsync2(0x0103, 0x0002, lambda_175F)

    @scena.Lambda('lambda_1770')
    def lambda_1770():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_1770')

    DispatchAsync2(0x0104, 0x0002, lambda_1770)

    Sleep(1000)

    ChrTalk(
        0x0013,
        (
            '#0270031753V#141F我们本来也想\n',
            '给你们做个采访的，\n',
            '不过这次你们就先忙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270031754V下次有机会的话，可要拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0280031755V#151F再见了～！\n',
            '小艾，小约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    CreateThread(0x0013, 0x01, 0x00, func_05_1CD1)
    Sleep(700)

    CreateThread(0x0014, 0x01, 0x00, func_05_1CD1)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0103, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0104, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    @scena.Lambda('lambda_1894')
    def lambda_1894():
        CameraMove(-15060, 4000, -19760, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1894)

    @scena.Lambda('lambda_18AC')
    def lambda_18AC():
        OP_6E(232, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_18AC)

    Sleep(3000)

    OP_63(0x0101)
    OP_63(0x0102)
    OP_63(0x0103)
    OP_63(0x0104)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)
    OP_20(0x000005DC)
    Sleep(1000)

    Fade(1000)
    CameraSetDistance(3010, 0)
    OP_0D()

    ChrTalk(
        0x0104,
        (
            '#0040031756V#035F哎呀呀～\n',
            '感觉最后什么好处都被他们得到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031757V#007F#5P嗯，确实是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031758V#027F呵呵，其实这样已经够了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031759V游击士的本分就是\n',
            '默默奉献自己的力量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031760V被忽视也是没办法的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031761V#010F的确是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031762V其实父亲也一直在\n',
            '坚持着这点而默默地工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031763V#505F#5P咦，是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031764V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010031765V#004F#3S#5P啊啊，老爸！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_1AD2')
    def lambda_1AD2():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1AD2)

    @scena.Lambda('lambda_1AE0')
    def lambda_1AE0():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_1AE0)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031766V#015F嗯……\n',
            '必须认真想想这个问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031767V#013F父亲他究竟在哪里，\n',
            '现在又在做些什么呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031768V为什么不联络我们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031769V#003F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031770V#026F这里已经没什么\n',
            '需要我们帮忙的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031771V总之先回柏斯\n',
            '把这次的事件报告一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031772V#020F然后再仔细考虑老师的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x014E)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C4D',
    )

    OP_28(0x0013, 0x04, 0x40)

    def _loc_1C4D(): pass

    label('loc_1C4D')

    OP_28(0x0037, 0x04, 0x10)
    OP_28(0x0039, 0x01, 0x0100)
    OP_28(0x0039, 0x01, 0x0200)
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x1C76
@scena.Code('func_04_1C76')
def func_04_1C76():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -10930, 4050, -36370, 3000, 0x00)
    ChrWalkTo(0x00FE, -8109, 4000, -36510, 3000, 0x00)
    ChrWalkTo(0x00FE, -8189, 2000, -32610, 3000, 0x00)
    ChrWalkTo(0x00FE, 4010, 0, -32450, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0005 offset: 0x1CD1
@scena.Code('func_05_1CD1')
def func_05_1CD1():
    ChrWalkTo(0x00FE, -16840, 4000, -20560, 3000, 0x00)
    ChrWalkTo(0x00FE, -17210, 4000, -15830, 3000, 0x00)
    ChrWalkTo(0x00FE, -17070, 750, -10700, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
