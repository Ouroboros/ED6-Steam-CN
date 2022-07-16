import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1302   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔丝特'),
    TXT(0x02, '吉尔'),
    TXT(0x03, '多伦'),
    TXT(0x04, '王国军士兵'),
    TXT(0x05, '王国军士兵'),
    TXT(0x06, '王国军士兵'),
    TXT(0x07, '王国军士兵'),
    TXT(0x08, '王国军军官'),
    TXT(0x09, '理查德上校'),
    TXT(0x0A, '凯诺娜上尉'),
    TXT(0x0B, '摩尔根将军'),
    TXT(0x0C, '奈尔'),
    TXT(0x0D, '朵洛希'),
    TXT(0x0E, '王国军士兵'),
    TXT(0x0F, '王国军士兵'),
    TXT(0x10, '王国军士兵'),
    TXT(0x11, '王国军士兵'),
    TXT(0x12, '王国军士兵'),
    TXT(0x13, '王国军士兵'),
    TXT(0x14, ''),
]

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

# id: 0xFFFF offset: 0x1BCB
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
            word_3A         = 52,
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

# id: 0x10002 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x362
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x362
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x362
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x362
@scena.Code('PreInit')
def PreInit():
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
    Event(0, 0x0003)

    def _loc_37D(): pass

    label('loc_37D')

    Jump('loc_380')

    def _loc_380(): pass

    label('loc_380')

    Return()

# id: 0x0001 offset: 0x381
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x382
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_397',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_397(): pass

    label('loc_397')

    Return()

# id: 0x0003 offset: 0x398
@scena.Code('func_03_398')
def func_03_398():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-17060, 3750, -15530, 0)
    OP_67(0, 5310, -10000, 0)
    CameraSetDistance(3740, 0)
    OP_6C(102000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0101, -16500, 2000, -14000, 180)
    SetChrPos(0x0103, -17120, 2000, -13840, 180)
    SetChrPos(0x0102, -16600, 2000, -12660, 180)
    SetChrPos(0x0104, -17460, 2000, -12310, 180)
    SetChrPos(0x000B, -13140, 4000, -23900, 180)
    SetChrPos(0x000A, -13220, 4000, -22610, 180)
    SetChrPos(0x000D, -11860, 4000, -22360, 180)
    SetChrPos(0x0008, -13031, 4000, -21770, 233)
    SetChrPos(0x000C, -13750, 4000, -21750, 180)
    SetChrPos(0x0009, -12600, 4000, -21120, 64)
    SetChrPos(0x000F, -12300, 4000, -20010, 180)
    ChrTurnDirection(0x000B, 0x000A, 0)
    ChrTurnDirection(0x000C, 0x000A, 0)
    ChrTurnDirection(0x000D, 0x000A, 0)
    ChrTurnDirection(0x000F, 0x000A, 0)
    SetChrPos(0x0013, -17040, 4000, -24290, 0)
    SetChrPos(0x0014, -16980, 4000, -25880, 0)

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
        SetChrDirection(0x00FE, 134, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_061E)

    WaitForThreadExit(0x0103, 0x0001)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0648')
    def lambda_0648():
        SetChrDirection(0x00FE, 134, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0648)

    WaitForThreadExit(0x0104, 0x0001)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0672')
    def lambda_0672():
        SetChrDirection(0x00FE, 134, 400)

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

    @scena.Lambda('lambda_0727')
    def lambda_0727():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0727')

    DispatchAsync2(0x0101, 0x0000, lambda_0727)

    @scena.Lambda('lambda_0738')
    def lambda_0738():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0738')

    DispatchAsync2(0x0102, 0x0000, lambda_0738)

    @scena.Lambda('lambda_0749')
    def lambda_0749():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0749')

    DispatchAsync2(0x0103, 0x0000, lambda_0749)

    @scena.Lambda('lambda_075A')
    def lambda_075A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_075A')

    DispatchAsync2(0x0104, 0x0000, lambda_075A)

    PlayBGM(101)

    @scena.Lambda('lambda_076D')
    def lambda_076D():
        CameraMove(-8410, 4000, -22720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_076D)

    @scena.Lambda('lambda_0785')
    def lambda_0785():
        OP_6E(437, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0785)

    @scena.Lambda('lambda_0795')
    def lambda_0795():
        OP_6C(125000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0795)

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

    @scena.Lambda('lambda_08A4')
    def lambda_08A4():
        CameraMove(-14680, 4000, -20970, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08A4)

    @scena.Lambda('lambda_08BC')
    def lambda_08BC():
        OP_67(0, 7970, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_08BC)

    @scena.Lambda('lambda_08D4')
    def lambda_08D4():
        OP_6C(137000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_08D4)

    @scena.Lambda('lambda_08E4')
    def lambda_08E4():
        OP_6E(244, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_08E4)

    CreateThread(0x000B, 0x01, 0x00, 0x0004)
    Sleep(100)

    CreateThread(0x000A, 0x01, 0x00, 0x0004)
    Sleep(200)

    CreateThread(0x000D, 0x01, 0x00, 0x0004)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, 0x0004)
    Sleep(300)

    CreateThread(0x000C, 0x01, 0x00, 0x0004)
    Sleep(300)

    CreateThread(0x0009, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x000F, 0x01, 0x00, 0x0004)
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
    SetChrPos(0x0010, -11930, 4000, -33160, 0)
    SetChrPos(0x0012, -11930, 4000, -33160, 0)
    SetChrPos(0x0011, -11930, 4000, -33160, 0)
    SetChrPos(0x0015, -11450, 4050, -36300, 0)
    SetChrPos(0x0016, -11450, 4050, -36300, 0)
    SetChrPos(0x0017, -11450, 4050, -36300, 0)
    SetChrPos(0x0018, -11450, 4050, -36300, 0)
    SetChrPos(0x0019, -11450, 4050, -36300, 0)
    SetChrPos(0x001A, -11450, 4050, -36300, 0)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    SetChrFlags(0x0015, 0x0040)
    SetChrFlags(0x0016, 0x0040)
    SetChrFlags(0x0017, 0x0040)
    SetChrFlags(0x0018, 0x0040)
    SetChrFlags(0x0019, 0x0040)
    SetChrFlags(0x001A, 0x0040)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0010, 0x0040)
    SetChrFlags(0x0012, 0x0040)
    SetChrFlags(0x0011, 0x0040)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0011, 0x0004)

    @scena.Lambda('lambda_0B19')
    def lambda_0B19():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_0B19')

    DispatchAsync2(0x0014, 0x0001, lambda_0B19)

    @scena.Lambda('lambda_0B2A')
    def lambda_0B2A():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_0B2A')

    DispatchAsync2(0x0013, 0x0001, lambda_0B2A)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)

    @scena.Lambda('lambda_0B4B')
    def lambda_0B4B():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0B4B)

    @scena.Lambda('lambda_0B59')
    def lambda_0B59():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B59)

    @scena.Lambda('lambda_0B67')
    def lambda_0B67():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0B67)

    @scena.Lambda('lambda_0B75')
    def lambda_0B75():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B75)

    @scena.Lambda('lambda_0B83')
    def lambda_0B83():
        CameraMove(-15270, 4000, -25300, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B83)

    @scena.Lambda('lambda_0B9B')
    def lambda_0B9B():
        ChrWalkTo(0x00FE, -14420, 4000, -24480, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0B9B)

    Sleep(400)

    @scena.Lambda('lambda_0BBB')
    def lambda_0BBB():
        ChrWalkTo(0x00FE, -13450, 4000, -25860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0BBB)

    Sleep(400)

    @scena.Lambda('lambda_0BDB')
    def lambda_0BDB():
        ChrWalkTo(0x00FE, -14140, 4000, -27020, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0BDB)

    @scena.Lambda('lambda_0BF6')
    def lambda_0BF6():
        SetChrDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0BF6')

    DispatchAsync2(0x0015, 0x0001, lambda_0BF6)

    @scena.Lambda('lambda_0C07')
    def lambda_0C07():
        SetChrDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C07')

    DispatchAsync2(0x0016, 0x0001, lambda_0C07)

    @scena.Lambda('lambda_0C18')
    def lambda_0C18():
        SetChrDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C18')

    DispatchAsync2(0x0017, 0x0001, lambda_0C18)

    @scena.Lambda('lambda_0C29')
    def lambda_0C29():
        SetChrDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C29')

    DispatchAsync2(0x0018, 0x0001, lambda_0C29)

    @scena.Lambda('lambda_0C3A')
    def lambda_0C3A():
        SetChrDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C3A')

    DispatchAsync2(0x0019, 0x0001, lambda_0C3A)

    @scena.Lambda('lambda_0C4B')
    def lambda_0C4B():
        SetChrDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_0C4B')

    DispatchAsync2(0x001A, 0x0001, lambda_0C4B)

    @scena.Lambda('lambda_0C5C')
    def lambda_0C5C():
        ChrWalkTo(0x00FE, -12200, 4000, -24410, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_0C5C)

    Sleep(400)

    @scena.Lambda('lambda_0C7C')
    def lambda_0C7C():
        ChrWalkTo(0x00FE, -11150, 4000, -24390, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_0C7C)

    Sleep(400)

    @scena.Lambda('lambda_0C9C')
    def lambda_0C9C():
        ChrWalkTo(0x00FE, -11150, 4000, -25510, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_0C9C)

    Sleep(400)

    @scena.Lambda('lambda_0CBC')
    def lambda_0CBC():
        ChrWalkTo(0x00FE, -12270, 4000, -25510, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_0CBC)

    Sleep(400)

    @scena.Lambda('lambda_0CDC')
    def lambda_0CDC():
        ChrWalkTo(0x00FE, -11150, 4000, -26750, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_0CDC)

    Sleep(400)

    @scena.Lambda('lambda_0CFC')
    def lambda_0CFC():
        ChrWalkTo(0x00FE, -12310, 4000, -26750, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_0CFC)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_0D1C')
    def lambda_0D1C():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0D1C)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_0D2F')
    def lambda_0D2F():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0D2F)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_0D42')
    def lambda_0D42():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0D42)

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

    @scena.Lambda('lambda_0F52')
    def lambda_0F52():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0F52')

    DispatchAsync2(0x0010, 0x0002, lambda_0F52)

    @scena.Lambda('lambda_0F63')
    def lambda_0F63():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0F63')

    DispatchAsync2(0x0014, 0x0002, lambda_0F63)

    @scena.Lambda('lambda_0F74')
    def lambda_0F74():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0F74')

    DispatchAsync2(0x0013, 0x0002, lambda_0F74)

    @scena.Lambda('lambda_0F85')
    def lambda_0F85():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0F85')

    DispatchAsync2(0x0011, 0x0002, lambda_0F85)

    @scena.Lambda('lambda_0F96')
    def lambda_0F96():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0F96')

    DispatchAsync2(0x0012, 0x0002, lambda_0F96)

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

    @scena.Lambda('lambda_0FEF')
    def lambda_0FEF():
        CameraMove(-14680, 4000, -23970, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0FEF)

    @scena.Lambda('lambda_1007')
    def lambda_1007():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_1007')

    DispatchAsync2(0x0101, 0x0002, lambda_1007)

    @scena.Lambda('lambda_1018')
    def lambda_1018():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_1018')

    DispatchAsync2(0x0102, 0x0002, lambda_1018)

    @scena.Lambda('lambda_1029')
    def lambda_1029():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_1029')

    DispatchAsync2(0x0103, 0x0002, lambda_1029)

    @scena.Lambda('lambda_103A')
    def lambda_103A():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_103A')

    DispatchAsync2(0x0104, 0x0002, lambda_103A)

    @scena.Lambda('lambda_104B')
    def lambda_104B():
        ChrWalkTo(0x00FE, -13660, 4000, -20310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_104B)

    Sleep(100)

    @scena.Lambda('lambda_106B')
    def lambda_106B():
        ChrWalkTo(0x00FE, -15190, 4000, -20740, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_106B)

    Sleep(100)

    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_1090')
    def lambda_1090():
        ChrWalkTo(0x00FE, -14410, 4000, -19180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1090)

    Sleep(100)

    @scena.Lambda('lambda_10B0')
    def lambda_10B0():
        ChrWalkTo(0x00FE, -15620, 4000, -19480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_10B0)

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
    ClearChrFlags(0x0012, 0x0004)
    SetChrDirection(0x0012, 180, 400)
    CreateThread(0x0012, 0x01, 0x00, 0x0004)
    Sleep(400)

    SetChrDirection(0x001A, 180, 400)
    CreateThread(0x001A, 0x01, 0x00, 0x0004)
    Sleep(300)

    SetChrDirection(0x0019, 180, 400)
    CreateThread(0x0019, 0x01, 0x00, 0x0004)
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
    ClearChrFlags(0x0010, 0x0004)
    ClearChrFlags(0x0011, 0x0004)
    CreateThread(0x0010, 0x01, 0x00, 0x0005)
    Sleep(100)

    CreateThread(0x0011, 0x01, 0x00, 0x0005)

    @scena.Lambda('lambda_1590')
    def lambda_1590():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1590')

    DispatchAsync2(0x0014, 0x0001, lambda_1590)

    @scena.Lambda('lambda_15A1')
    def lambda_15A1():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_15A1')

    DispatchAsync2(0x0013, 0x0001, lambda_15A1)

    @scena.Lambda('lambda_15B2')
    def lambda_15B2():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_15B2')

    DispatchAsync2(0x0101, 0x0002, lambda_15B2)

    @scena.Lambda('lambda_15C3')
    def lambda_15C3():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_15C3')

    DispatchAsync2(0x0102, 0x0002, lambda_15C3)

    @scena.Lambda('lambda_15D4')
    def lambda_15D4():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_15D4')

    DispatchAsync2(0x0103, 0x0002, lambda_15D4)

    @scena.Lambda('lambda_15E5')
    def lambda_15E5():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_15E5')

    DispatchAsync2(0x0104, 0x0002, lambda_15E5)

    Sleep(500)

    CreateThread(0x0015, 0x01, 0x00, 0x0005)
    Sleep(200)

    CreateThread(0x0016, 0x01, 0x00, 0x0005)
    Sleep(400)

    CreateThread(0x0018, 0x01, 0x00, 0x0005)
    Sleep(200)

    CreateThread(0x0017, 0x01, 0x00, 0x0005)
    Sleep(300)

    ChrTalk(
        0x0013,
        (
            '#0270031752V#143F啊，请等等上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_164D')
    def lambda_164D():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_164D')

    DispatchAsync2(0x0101, 0x0002, lambda_164D)

    @scena.Lambda('lambda_165E')
    def lambda_165E():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_165E')

    DispatchAsync2(0x0102, 0x0002, lambda_165E)

    @scena.Lambda('lambda_166F')
    def lambda_166F():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_166F')

    DispatchAsync2(0x0103, 0x0002, lambda_166F)

    @scena.Lambda('lambda_1680')
    def lambda_1680():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_1680')

    DispatchAsync2(0x0104, 0x0002, lambda_1680)

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
    SetChrFlags(0x0013, 0x0040)
    SetChrFlags(0x0014, 0x0040)
    CreateThread(0x0013, 0x01, 0x00, 0x0005)
    Sleep(700)

    CreateThread(0x0014, 0x01, 0x00, 0x0005)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0103, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0104, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    @scena.Lambda('lambda_1795')
    def lambda_1795():
        CameraMove(-15060, 4000, -19760, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1795)

    @scena.Lambda('lambda_17AD')
    def lambda_17AD():
        OP_6E(232, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_17AD)

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

    @scena.Lambda('lambda_19A1')
    def lambda_19A1():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_19A1)

    @scena.Lambda('lambda_19AF')
    def lambda_19AF():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_19AF)

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
        'loc_1AF9',
    )

    OP_28(0x0013, 0x04, 0x40)

    def _loc_1AF9(): pass

    label('loc_1AF9')

    OP_28(0x0037, 0x04, 0x10)
    OP_28(0x0039, 0x01, 0x0100)
    OP_28(0x0039, 0x01, 0x0200)
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x1B22
@scena.Code('func_04_1B22')
def func_04_1B22():
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -10930, 4050, -36370, 3000, 0x00)
    ChrWalkTo(0x00FE, -8109, 4000, -36510, 3000, 0x00)
    ChrWalkTo(0x00FE, -8189, 2000, -32610, 3000, 0x00)
    ChrWalkTo(0x00FE, 4010, 0, -32450, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0005 offset: 0x1B7D
@scena.Code('func_05_1B7D')
def func_05_1B7D():
    ChrWalkTo(0x00FE, -16840, 4000, -20560, 3000, 0x00)
    ChrWalkTo(0x00FE, -17210, 4000, -15830, 3000, 0x00)
    ChrWalkTo(0x00FE, -17070, 750, -10700, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
