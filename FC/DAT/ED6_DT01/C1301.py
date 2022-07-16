import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '吉尔'),
    TXT(0x02, '乔丝特'),
    TXT(0x03, '空贼阿伦'),
    TXT(0x04, '空贼雷古'),
    TXT(0x05, '空贼蒂诺'),
    TXT(0x06, '空贼莱尔'),
    TXT(0x07, '空贼洛西'),
    TXT(0x08, '空贼罗尔'),
    TXT(0x09, ' '),
    TXT(0x0A, ' '),
    TXT(0x0B, ' '),
    TXT(0x0C, ' '),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1301.x'
    header.mapIndex       = 52
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x176A
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
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT07/CH00360._CH', 'ED6_DT07/CH00360P._CP'),
        ('ED6_DT06/CH20074._CH', 'ED6_DT06/CH20074P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
    ]

# id: 0x10002 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
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
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 800,
            z                   = 500,
            y                   = 500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -500,
            z                   = 500,
            y                   = 900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 500,
            y                   = -700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2300,
            z                   = 500,
            y                   = -2700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -1000,
            z                   = 500,
            y                   = -2800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1000,
            z                   = 500,
            y                   = -1900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x292
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x292
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x292
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -11400,
            triggerZ            = 4000,
            triggerY            = -2400,
            triggerRange        = 1500,
            actorX              = -8930,
            actorZ              = 6520,
            actorY              = -880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9150,
            triggerZ            = 5540,
            triggerY            = -590,
            triggerRange        = 1000,
            actorX              = -10940,
            actorZ              = 5000,
            actorY              = -1870,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2DA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2E8',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0003)

    def _loc_2E8(): pass

    label('loc_2E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 3, 0x353)),
            Expr.Return,
        ),
        'loc_337',
    )

    SetChrPos(0x000D, -11640, 4000, 6760, 55)
    SetChrPos(0x000F, -13460, 4000, 7840, 312)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x000D, 0x0001)
    ClearChrFlags(0x000F, 0x0001)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000F, 0xFF)
    SetChrChipByIndex(0x000D, 4)
    SetChrChipByIndex(0x000F, 4)

    def _loc_337(): pass

    label('loc_337')

    Return()

# id: 0x0001 offset: 0x338
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x339
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_34E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_34E(): pass

    label('loc_34E')

    Return()

# id: 0x0003 offset: 0x34F
@scena.Code('func_03_34F')
def func_03_34F():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-13163, 5000, -2170, 0)
    SetChrPos(0x0101, -4230, 4000, -2740, 0)
    SetChrPos(0x0102, -4230, 4000, -2740, 0)
    SetChrPos(0x0103, -4230, 4000, -2740, 0)
    SetChrPos(0x0104, -4230, 4000, -2740, 0)
    SetChrPos(0x000A, -4230, 4000, -2740, 0)
    SetChrPos(0x000B, -4230, 4000, -2740, 0)
    SetChrPos(0x000C, -4230, 4000, -2740, 0)
    SetChrPos(0x000D, -4230, 4000, -2740, 0)
    SetChrPos(0x000E, -4230, 4000, -2740, 0)
    SetChrPos(0x000F, -4230, 4000, -2740, 0)
    SetChrPos(0x0009, -4230, 4000, -2740, 0)
    SetChrPos(0x0008, -4230, 4000, -2740, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0103, 0x0040)
    SetChrFlags(0x0104, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000F, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x0104, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000E, 0x0004)
    SetChrFlags(0x000F, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    CameraMove(2350, 4000, -39840, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(5220, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    CameraMove(-5000, 4000, -980, 6000)
    Fade(1000)
    CameraMove(-3670, 4000, 210, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3160, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_0587')
    def lambda_0587():
        CameraMove(-10920, 4000, -1950, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0587)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    OP_73(0x0000)
    CreateThread(0x0008, 0x01, 0x00, 0x0004)
    Sleep(600)

    CreateThread(0x0009, 0x01, 0x00, 0x0004)
    Sleep(1200)

    CreateThread(0x000A, 0x01, 0x00, 0x0004)
    Sleep(600)

    CreateThread(0x000B, 0x01, 0x00, 0x0004)
    Sleep(600)

    CreateThread(0x000C, 0x01, 0x00, 0x0004)
    Sleep(600)

    CreateThread(0x000E, 0x01, 0x00, 0x0004)
    Sleep(1500)

    CreateThread(0x000D, 0x01, 0x00, 0x0005)
    Sleep(1000)

    CreateThread(0x000F, 0x01, 0x00, 0x0006)
    Sleep(1500)

    @scena.Lambda('lambda_0610')
    def lambda_0610():
        CameraMove(-12340, 4000, -15850, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0610)

    WaitForThreadExit(0x000D, 0x0001)

    @scena.Lambda('lambda_062D')
    def lambda_062D():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_062D')

    DispatchAsync2(0x000D, 0x0002, lambda_062D)

    WaitForThreadExit(0x000F, 0x0001)

    @scena.Lambda('lambda_0643')
    def lambda_0643():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0643')

    DispatchAsync2(0x000F, 0x0002, lambda_0643)

    ChrTalk(
        0x000D,
        (
            '#0990031367V#2P呼～好困啊～好困啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0990031368V#2P自从来了这里之后，\n',
            '就一直过着昼夜颠倒的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1270031369V#1P好了，再忍耐一段时间吧。\n',
            '这样的生活很快就会结束的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1270031370V#1P跟着多伦老大干事\n',
            '准会有出头的一日的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0990031371V#2P不过最近老大……\n',
            '好像有点怪怪的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0990031372V#2P先不说不跟我们一起行动，\n',
            '就连说话也变得越来越浮躁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1270031373V#1P你这家伙……\n',
            '怎么这么多废话呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1270031374V#1P要是给吉尔大哥和大小姐听到了，\n',
            '当心被踢出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0990031375V#2P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1270031376V#1P睡眠不足会很累的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1270031377V#1P快点收拾一下，\n',
            '然后好好休息去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 5)
    SetChrChipByIndex(0x0102, 7)
    SetChrChipByIndex(0x0103, 9)
    SetChrChipByIndex(0x0104, 11)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0103, 0x0080)
    ClearChrFlags(0x0104, 0x0080)
    SetChrPos(0x0101, -12840, 4000, -6330, 180)
    SetChrPos(0x0102, -12790, 4000, -4890, 180)
    SetChrPos(0x0103, -11570, 4000, -5960, 180)
    SetChrPos(0x0104, -11540, 4000, -4420, 180)

    NpcTalk(
        0x0101,
        '女孩的声音',
        (
            '#0010031378V#2P现在休息不就ＯＫ了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0952')
    def lambda_0952():
        ChrTurnDirection(0x00FE, 0x0103, 500)
        Yield()

        Jump('lambda_0952')

    DispatchAsync2(0x000F, 0x0002, lambda_0952)

    @scena.Lambda('lambda_0963')
    def lambda_0963():
        ChrTurnDirection(0x00FE, 0x0103, 500)
        Yield()

        Jump('lambda_0963')

    DispatchAsync2(0x000D, 0x0002, lambda_0963)

    @scena.Lambda('lambda_0974')
    def lambda_0974():
        CameraMove(-12270, 4000, -10410, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0974)

    Sleep(1200)

    ChrTalk(
        0x000F,
        (
            '#1270031379V啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0990031380V是你们……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031381V#006F太慢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_09FB')
    def lambda_09FB():
        CameraMove(-12970, 4000, -14070, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_09FB)

    @scena.Lambda('lambda_0A13')
    def lambda_0A13():
        ChrWalkTo(0x0101, -13160, 4000, -13140, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A13)

    Sleep(100)

    SetChrChipByIndex(0x000F, 3)

    @scena.Lambda('lambda_0A38')
    def lambda_0A38():
        ChrWalkTo(0x0103, -11870, 4000, -12840, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0A38)

    Sleep(100)

    SetChrChipByIndex(0x000D, 3)

    @scena.Lambda('lambda_0A5D')
    def lambda_0A5D():
        ChrWalkTo(0x0102, -14250, 4000, -11660, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A5D)

    Sleep(100)

    @scena.Lambda('lambda_0A7D')
    def lambda_0A7D():
        ChrWalkTo(0x0104, -12920, 4000, -10960, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0A7D)

    Sleep(300)

    Battle(0x00000388, 0x00000000, 0x02, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_AB0'),
        (-1, 'loc_AB5'),
    )

    def _loc_AB0(): pass

    label('loc_AB0')

    OP_B4(0x00)

    Jump('loc_AB5')

    def _loc_AB5(): pass

    label('loc_AB5')

    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000F, 0xFF)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x0104, 65535)
    SetChrPos(0x0101, -13670, 4000, 2920, 141)
    SetChrPos(0x0102, -12270, 4000, 2580, 171)
    SetChrPos(0x0103, -13420, 4000, 800, 90)
    SetChrPos(0x0104, -12130, 4000, 800, 325)
    SetChrPos(0x000D, -11640, 4000, 6760, 55)
    SetChrPos(0x000F, -13460, 4000, 7840, 312)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x000D, 0x0001)
    ClearChrFlags(0x000F, 0x0001)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000F, 0xFF)
    SetChrChipByIndex(0x000D, 4)
    SetChrChipByIndex(0x000F, 4)
    CameraMove(-11980, 4000, 1620, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3190, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040031382V#030F#1P呵呵……\n',
            '看来已经顺利潜入空贼基地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031383V#027F真是的……\n',
            '没想到你还有这一手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031384V看来这次\n',
            '不向你道谢也不行了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031385V#009F可、可是呢～\n',
            '刚才真是吓死我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031386V要是被他们发现\n',
            '我们藏在那里可怎么办啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031387V#010F没关系，真的被发现的话，\n',
            '我们只要控制空贼飞艇就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031388V飞艇内部的通道狭小，\n',
            '有利于我们与成批的敌人战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031389V奥利维尔……\n',
            '你应该也想到了这点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031390V#031F#1P哎呀，真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031391V我只是觉得藏到\n',
            '敌人阵地比较有趣罢了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031392V#007F你、你还真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031393V#021F算了，这样不是很好吗。\n',
            '反正我们已经顺利潜进来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031394V#020F不过话说回来……\n',
            '这里好像是『迷雾峡谷』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 200)

    ChrTalk(
        0x0101,
        (
            '#0010031395V#501F『迷雾峡谷』……\n',
            '不是在柏斯和洛连特的边境吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031396V对了……\n',
            '怪不得外面有白色的霞光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031397V#010F而且这里是大型飞艇无法进入的\n',
            '高低差很大的复杂地形……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031398V雪拉姐姐的推测，\n',
            '看来是相当正确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031399V#026F唔……\n',
            '应该说是没派上用场的推测吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031400V#020F接下来……\n',
            '不要在这里耽误时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031401V对了，有一点需要大家注意，\n',
            '就是在制服空贼的同时\n',
            '务必确保被囚禁人质的生命安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031402V当然……也包括卡西乌斯老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031403V#006F嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031404V#012F明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)
    ClearChrFlags(0x0103, 0x0004)
    ClearChrFlags(0x0104, 0x0004)
    ClearChrFlags(0x0101, 0x0040)
    ClearChrFlags(0x0102, 0x0040)
    ClearChrFlags(0x0103, 0x0040)
    ClearChrFlags(0x0104, 0x0040)
    Sleep(100)

    Fade(1000)
    CameraMove(-12990, 4000, 980, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -12990, 4000, 980, 141)
    SetChrPos(0x0102, -12990, 4000, 980, 141)
    SetChrPos(0x0103, -12990, 4000, 980, 141)
    SetChrPos(0x0104, -12990, 4000, 980, 141)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x006A, 3, 0x353))
    OP_28(0x0039, 0x01, 0x0001)
    OP_28(0x0039, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x112C
@scena.Code('func_04_112C')
def func_04_112C():
    SetChrPos(0x00FE, -3290, 5600, -1690, 262)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -4410, 5600, -1830, 4000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -4940, 6130, -20, 4000, 0x00)
    ChrWalkTo(0x00FE, -9190, 5540, -520, 4000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    SetChrDirection(0x00FE, 270, 400)
    ChrJumpTo(0x00FE, -11090, 4000, -330, 600, 5000)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -13050, 4000, -860, 4000, 0x00)
    ChrWalkTo(0x00FE, -13130, 4000, -16680, 4000, 0x00)
    ChrWalkTo(0x00FE, -17000, 4000, -16940, 4000, 0x00)
    ChrWalkTo(0x00FE, -17050, 0, -8540, 4000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0005 offset: 0x1206
@scena.Code('func_05_1206')
def func_05_1206():
    SetChrPos(0x00FE, -3290, 5600, -1690, 262)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -4410, 5600, -1830, 4000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -4940, 6130, -20, 4000, 0x00)
    ChrWalkTo(0x00FE, -9190, 5540, -520, 4000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    SetChrDirection(0x00FE, 270, 400)
    ChrJumpTo(0x00FE, -11090, 4000, -330, 600, 4000)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -13740, 4000, -860, 4000, 0x00)
    ChrWalkTo(0x00FE, -13740, 4000, -15190, 4000, 0x00)
    OP_4A(0x00FE, 255)

    Return()

# id: 0x0006 offset: 0x12B7
@scena.Code('func_06_12B7')
def func_06_12B7():
    SetChrPos(0x00FE, -3290, 5600, -1690, 262)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -4410, 5600, -1830, 4000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -4940, 6130, -20, 4000, 0x00)
    ChrWalkTo(0x00FE, -9190, 5540, -520, 4000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    SetChrDirection(0x00FE, 270, 400)
    ChrJumpTo(0x00FE, -11090, 4000, -330, 600, 4000)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -12200, 4000, -860, 4000, 0x00)
    ChrWalkTo(0x00FE, -12200, 4000, -14470, 4000, 0x00)
    OP_4A(0x00FE, 255)

    Return()

# id: 0x0007 offset: 0x1368
@scena.Code('func_07_1368')
def func_07_1368():
    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x01,
        (
            (Expr.GetChrWork, 0x1, 0x1),
            (Expr.GetChrWork, 0x1, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x02,
        (
            (Expr.GetChrWork, 0x1, 0x2),
            (Expr.GetChrWork, 0x1, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x03,
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.GetChrWork, 0x1, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x2, 0x1),
            (Expr.GetChrWork, 0x2, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x2, 0x2),
            (Expr.GetChrWork, 0x2, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x2, 0x3),
            (Expr.GetChrWork, 0x2, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0000, 0x01, 0x00, 0x000B)
    CreateThread(0x0001, 0x01, 0x00, 0x000A)
    CreateThread(0x0002, 0x01, 0x00, 0x0009)
    CreateThread(0x0003, 0x01, 0x00, 0x0008)
    WaitForThreadExit(0x0003, 0x0001)
    OP_30(0x00)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x144C
@scena.Code('func_08_144C')
def func_08_144C():
    SetChrFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x0012, 0, 6000, 0x00)
    OP_92(0x00FE, 0x0011, 0, 6000, 0x00)
    OP_92(0x00FE, 0x0010, 0, 6000, 0x00)
    SetChrDirection(0x00FE, 90, 0)
    SetChrSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -8900, 5510, -640, 2000, 5000)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x0009 offset: 0x14A4
@scena.Code('func_09_14A4')
def func_09_14A4():
    SetChrFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x0011, 0, 6000, 0x00)
    OP_92(0x00FE, 0x0010, 0, 6000, 0x00)
    SetChrDirection(0x00FE, 90, 0)
    SetChrSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -8900, 5510, -640, 2000, 5000)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000A offset: 0x14EE
@scena.Code('func_0A_14EE')
def func_0A_14EE():
    SetChrFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x0010, 0, 6000, 0x00)
    SetChrDirection(0x00FE, 90, 0)
    SetChrSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -8900, 5510, -640, 2000, 5000)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000B offset: 0x152A
@scena.Code('func_0B_152A')
def func_0B_152A():
    SetChrFlags(0x00FE, 0x0004)
    SetChrDirection(0x00FE, 90, 0)
    SetChrSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -8900, 5510, -640, 2000, 5000)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000C offset: 0x1558
@scena.Code('func_0C_1558')
def func_0C_1558():
    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x01,
        (
            (Expr.GetChrWork, 0x1, 0x1),
            (Expr.GetChrWork, 0x1, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x02,
        (
            (Expr.GetChrWork, 0x1, 0x2),
            (Expr.GetChrWork, 0x1, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x03,
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.GetChrWork, 0x1, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x2, 0x1),
            (Expr.GetChrWork, 0x2, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x2, 0x2),
            (Expr.GetChrWork, 0x2, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x2, 0x3),
            (Expr.GetChrWork, 0x2, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0000, 0x01, 0x00, 0x0010)
    CreateThread(0x0001, 0x01, 0x00, 0x000F)
    CreateThread(0x0002, 0x01, 0x00, 0x000E)
    CreateThread(0x0003, 0x01, 0x00, 0x000D)
    WaitForThreadExit(0x0003, 0x0001)
    OP_30(0x00)
    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x163C
@scena.Code('func_0D_163C')
def func_0D_163C():
    SetChrFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x0012, 0, 6000, 0x00)
    OP_92(0x00FE, 0x0011, 0, 6000, 0x00)
    OP_92(0x00FE, 0x0010, 0, 6000, 0x00)
    SetChrDirection(0x00FE, 270, 0)
    SetChrSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -11000, 4000, -1990, 500, 5000)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000E offset: 0x1694
@scena.Code('func_0E_1694')
def func_0E_1694():
    SetChrFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x0011, 0, 6000, 0x00)
    OP_92(0x00FE, 0x0010, 0, 6000, 0x00)
    SetChrDirection(0x00FE, 270, 0)
    SetChrSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -11000, 4000, -1990, 500, 5000)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000F offset: 0x16DE
@scena.Code('func_0F_16DE')
def func_0F_16DE():
    SetChrFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x0010, 0, 6000, 0x00)
    SetChrDirection(0x00FE, 270, 0)
    SetChrSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -11000, 4000, -1990, 500, 5000)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x0010 offset: 0x171A
@scena.Code('func_10_171A')
def func_10_171A():
    SetChrFlags(0x00FE, 0x0004)
    SetChrDirection(0x00FE, 270, 0)
    SetChrSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -11000, 4000, -1990, 500, 5000)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
