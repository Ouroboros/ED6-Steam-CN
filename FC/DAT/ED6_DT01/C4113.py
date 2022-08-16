import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4113_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4113   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4113.x'
    header.mapIndex       = 1
    header.bgm            = 89
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
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH00400._CH', 'ED6_DT07/CH00400P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00390._CH', 'ED6_DT07/CH00390P._CP'),
        ('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT06/CH20114._CH', 'ED6_DT06/CH20114P._CP'),
        ('ED6_DT06/CH20115._CH', 'ED6_DT06/CH20115P._CP'),
        ('ED6_DT06/CH20116._CH', 'ED6_DT06/CH20116P._CP'),
        ('ED6_DT06/CH20117._CH', 'ED6_DT06/CH20117P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH01790._CH', 'ED6_DT07/CH01790P._CP'),
        ('ED6_DT07/CH00502._CH', 'ED6_DT07/CH00502P._CP'),
        ('ED6_DT07/CH00510._CH', 'ED6_DT07/CH00510P._CP'),
        ('ED6_DT07/CH00511._CH', 'ED6_DT07/CH00511P._CP'),
        ('ED6_DT07/CH00442._CH', 'ED6_DT07/CH00442P._CP'),
    ]

# id: 0x10001 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡露娜',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '库拉茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '克鲁茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 131087,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 131089,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 131089,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 131089,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 131089,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 131089,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 131089,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 131089,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 131089,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '中队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '军用犬',
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
        ScenaNpcData(
            name                = '军用犬',
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
        ScenaNpcData(
            name                = '军用犬',
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
        ScenaNpcData(
            name                = '军用犬',
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
        ScenaNpcData(
            name                = '军用犬',
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
        ScenaNpcData(
            name                = '修理员佩顿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x59A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x59A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 14350,
            y           = -1000,
            z           = -8640,
            range       = 11930,
            dword_10    = 0x000007D0,
            dword_14    = 0x000019F0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 44270,
            y           = 1000,
            z           = 940,
            range       = 48410,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0xFFFFFF10,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 45450,
            y           = 1000,
            z           = 6140,
            range       = 47430,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x00001144,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000016,
        ),
    )

# id: 0x10004 offset: 0x5FA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x5FA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_611',
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

    Event(0, func_02_646)

    def _loc_611(): pass

    label('loc_611')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_61F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_03_B02)

    def _loc_61F(): pass

    label('loc_61F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_62D',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_14_1A64)

    def _loc_62D(): pass

    label('loc_62D')

    Return()

# id: 0x0001 offset: 0x62E
@scena.Code('func_01_62E')
def func_01_62E():
    OP_16(0x02, 4000, -90000, -113000, 196710)
    PlaySE(460, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x646
@scena.Code('func_02_646')
def func_02_646():
    MapClearFlags(0x02000000)
    EventBegin(0x00)
    CameraMove(45860, 0, 7990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(69000, 0)
    OP_6E(325, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, 26320, 0, 2029, 270)
    ChrSetPos(0x0009, 26350, 0, -100, 270)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_06C5')
    def lambda_06C5():
        OP_6C(45000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_06C5)

    Sleep(2000)

    @scena.Lambda('lambda_06DA')
    def lambda_06DA():
        OP_6E(228, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06DA)

    CameraMove(26290, 0, 960, 5000)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x0009, 0x0020)

    ChrTalk(
        0x0008,
        (
            '#2640130558V#5P哈啊……\n',
            '肚子好饿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#2640130559V#5P还没到换班时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#2650130560V喂喂，可别松懈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2650130561V潜伏中的亲卫队\n',
            '随时都有可能出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2640130562V#5P反正在逃中的人\n',
            '连十个都不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2640130563V#5P那些家伙，上校只要想的话，\n',
            '绝对一下就把他们给捉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x000E, 16180, 0, 1410, 90)
    ChrSetPos(0x000F, 15420, 0, 630, 90)
    ChrSetPos(0x0010, 15520, 0, 2230, 90)
    ChrSetPos(0x0011, 14270, 0, 550, 90)
    ChrSetPos(0x0012, 14270, 0, 2230, 90)
    ChrSetSubChip(0x000E, 1)
    ChrSetSubChip(0x000F, 2)
    ChrSetSubChip(0x0010, 2)
    ChrSetSubChip(0x0011, 2)
    ChrSetSubChip(0x0012, 2)
    OP_20(0x000005DC)

    ChrTalk(
        0x000E,
        (
            '#0100130564V#2P……如果你们能办得到的话，\n',
            '就尽管来试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0932')
    def lambda_0932():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0932)

    @scena.Lambda('lambda_0940')
    def lambda_0940():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0940)

    @scena.Lambda('lambda_094E')
    def lambda_094E():
        OP_6E(262, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_094E)

    @scena.Lambda('lambda_095E')
    def lambda_095E():
        CameraMove(20430, 0, 1370, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_095E)

    @scena.Lambda('lambda_0976')
    def lambda_0976():
        OP_6C(315000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0976)

    Sleep(500)

    PlayBGM(89)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#2640130565V#2P什……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2650130566V#2P亲卫队中队长……\n',
            '尤莉亚·舒华兹！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 25)
    ChrSetChipByIndex(0x0009, 25)
    ChrSetSubChip(0x0008, 0)
    ChrSetSubChip(0x0009, 0)
    ChrSetFlags(0x000E, 0x1000)
    ChrSetFlags(0x000F, 0x1000)
    ChrSetFlags(0x0010, 0x1000)
    ChrSetFlags(0x0011, 0x1000)
    ChrSetFlags(0x0012, 0x1000)
    ChrSetChipByIndex(0x000E, 14)

    @scena.Lambda('lambda_0A46')
    def lambda_0A46():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0A46)

    @scena.Lambda('lambda_0A5C')
    def lambda_0A5C():
        CameraMove(24930, 0, 1380, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A5C)

    Sleep(200)

    ChrSetChipByIndex(0x000F, 16)
    ChrSetChipByIndex(0x0010, 16)
    ChrSetChipByIndex(0x0011, 16)
    ChrSetChipByIndex(0x0012, 16)

    @scena.Lambda('lambda_0A8D')
    def lambda_0A8D():
        OP_92(0x00FE, 0x0009, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0A8D)

    Sleep(50)

    @scena.Lambda('lambda_0AA7')
    def lambda_0AA7():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0AA7)

    Sleep(50)

    @scena.Lambda('lambda_0AC1')
    def lambda_0AC1():
        OP_92(0x00FE, 0x0009, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0AC1)

    Sleep(50)

    @scena.Lambda('lambda_0ADB')
    def lambda_0ADB():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0ADB)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xB02
@scena.Code('func_03_B02')
def func_03_B02():
    EventBegin(0x00)
    CameraMove(30000, 0, 630, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(233000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x000E, 28310, 0, 210, 90)
    ChrSetPos(0x000F, 29950, 0, -1020, 47)
    ChrSetPos(0x0010, 29140, 0, 2290, 127)
    ChrSetPos(0x0011, 31010, 0, 1560, 131)
    ChrSetPos(0x0012, 31530, 0, -1200, 11)
    ChrSetChipByIndex(0x0008, 12)
    ChrSetChipByIndex(0x0009, 12)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0009, 0x0800)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, 33200, 0, 2800, 26)
    ChrSetPos(0x0009, 32790, 0, 420, 142)
    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x0018, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x001A, 0x0040)
    ChrSetFlags(0x001B, 0x0040)
    ChrSetFlags(0x001C, 0x0040)
    ChrSetFlags(0x001D, 0x0040)
    ChrSetFlags(0x001E, 0x0040)
    ChrSetFlags(0x001F, 0x0040)
    ChrSetFlags(0x0020, 0x0040)
    ChrSetFlags(0x0021, 0x0040)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x0017, 11630, 0, -2640, 90)
    ChrSetPos(0x0018, 9800, 0, -3930, 90)
    ChrSetPos(0x0019, 9800, 0, -3930, 90)
    ChrSetPos(0x001A, 9800, 0, -3930, 90)
    ChrSetPos(0x001B, 9800, 0, -3930, 90)
    ChrSetPos(0x001C, 9800, 0, -3930, 90)
    ChrSetPos(0x001D, 9890, 0, -2180, 90)
    ChrSetPos(0x001E, 9890, 0, -2180, 90)
    ChrSetPos(0x001F, 9890, 0, -2180, 90)
    ChrSetPos(0x0020, 9890, 0, -2180, 90)
    ChrSetPos(0x0021, 9890, 0, -2180, 90)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrSetFlags(0x0022, 0x0040)
    ChrSetFlags(0x0023, 0x0040)
    ChrSetFlags(0x0024, 0x0040)
    ChrSetFlags(0x0025, 0x0040)
    ChrSetFlags(0x0026, 0x0040)
    ChrSetPos(0x0022, 12030, 0, -4240, 90)
    ChrSetPos(0x0023, 13140, 0, -2490, 72)
    ChrSetPos(0x0024, 11810, 0, -930, 90)
    ChrSetPos(0x0025, 8510, 0, -4850, 90)
    ChrSetPos(0x0026, 8510, 0, -1080, 90)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#0100130571V#176F#5P总算收拾掉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130572V#173F哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000E, 1)
    ChrSetSubChip(0x000F, 1)
    ChrSetSubChip(0x0010, 1)
    ChrSetSubChip(0x0011, 1)
    ChrSetSubChip(0x0012, 1)
    ChrSetFlags(0x000E, 0x0020)
    ChrSetFlags(0x000F, 0x0020)
    ChrSetFlags(0x0010, 0x0020)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetFlags(0x0012, 0x0020)

    @scena.Lambda('lambda_0E33')
    def lambda_0E33():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0E33)

    @scena.Lambda('lambda_0E41')
    def lambda_0E41():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0E41)

    @scena.Lambda('lambda_0E4F')
    def lambda_0E4F():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0E4F)

    @scena.Lambda('lambda_0E5D')
    def lambda_0E5D():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0E5D)

    @scena.Lambda('lambda_0E6B')
    def lambda_0E6B():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0E6B)

    Sleep(100)

    @scena.Lambda('lambda_0E7E')
    def lambda_0E7E():
        CameraMove(19050, 0, 1190, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E7E)

    @scena.Lambda('lambda_0E96')
    def lambda_0E96():
        OP_6C(315000, 2300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0E96)

    Sleep(400)

    CreateThread(0x0022, 0x01, 0x00, func_05_1744)
    CreateThread(0x0023, 0x01, 0x00, func_06_178A)
    CreateThread(0x0024, 0x01, 0x00, func_07_17D0)
    CreateThread(0x0017, 0x01, 0x00, func_04_1711)
    CreateThread(0x0018, 0x01, 0x00, func_0A_187A)
    CreateThread(0x001D, 0x01, 0x00, func_0F_1965)
    Sleep(600)

    @scena.Lambda('lambda_0EDA')
    def lambda_0EDA():
        CameraMove(25500, 0, 390, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EDA)

    @scena.Lambda('lambda_0EF2')
    def lambda_0EF2():
        OP_67(0, 6710, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0EF2)

    CreateThread(0x0019, 0x01, 0x00, func_0B_18AD)
    CreateThread(0x001E, 0x01, 0x00, func_10_1998)
    Sleep(400)

    CreateThread(0x001A, 0x01, 0x00, func_0C_18E0)
    CreateThread(0x001F, 0x01, 0x00, func_11_19CB)
    Sleep(400)

    CreateThread(0x001B, 0x01, 0x00, func_0D_1913)
    CreateThread(0x0020, 0x01, 0x00, func_12_19FE)
    Sleep(400)

    CreateThread(0x001C, 0x01, 0x00, func_0E_1932)
    CreateThread(0x0021, 0x01, 0x00, func_13_1A31)
    Sleep(400)

    CreateThread(0x0025, 0x01, 0x00, func_08_1816)
    CreateThread(0x0026, 0x01, 0x00, func_09_1848)
    Sleep(2500)

    ChrTalk(
        0x0017,
        (
            '#2680130573V愚蠢的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130574V飞艇是上了锁的，\n',
            '不会那么容易被你们抢走的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0100130575V#178F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130576V如果不乖乖服从上校，\n',
            '那么就只有用你们的性命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130577V顽固不化的家伙们，\n',
            '受死吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130578V进攻！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, 12560, 0, -2110, 70)
    ChrSetPos(0x000D, 13660, 0, -70, 90)
    ChrSetPos(0x000C, 13730, 0, -1250, 75)
    ChrSetPos(0x000B, 12340, 0, 1110, 95)

    @scena.Lambda('lambda_10C0')
    def lambda_10C0():
        CameraMove(28050, 0, 980, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_10C0)

    LoadEffect(0x02, 'map\\\\mp019_00.eff')
    LoadEffect(0x00, 'craft\\\\cr201_02.eff')
    ChrSetPos(0x0028, 19080, 0, 510, 0)
    PlayEffect(0x02, 0xFF, 0x000C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x0028, 0, 0, 0, 0)
    Sleep(200)

    ChrSetChipByIndex(0x0022, 11)
    ChrSetChipByIndex(0x0023, 11)
    ChrSetChipByIndex(0x0024, 11)

    @scena.Lambda('lambda_115C')
    def lambda_115C():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_115C)

    @scena.Lambda('lambda_1177')
    def lambda_1177():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_1177)

    @scena.Lambda('lambda_1192')
    def lambda_1192():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_1192)

    Sleep(100)

    ChrSetChipByIndex(0x0018, 20)
    ChrSetChipByIndex(0x001C, 9)

    @scena.Lambda('lambda_11BC')
    def lambda_11BC():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_11BC)

    @scena.Lambda('lambda_11D7')
    def lambda_11D7():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_11D7)

    Sleep(100)

    ChrSetChipByIndex(0x0019, 9)
    ChrSetChipByIndex(0x001D, 9)

    @scena.Lambda('lambda_1201')
    def lambda_1201():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1201)

    @scena.Lambda('lambda_121C')
    def lambda_121C():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_121C)

    PlaySE(506, 0x00, 0x64)
    Sleep(100)

    Sleep(200)

    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001F, 0xFF)
    TerminateThread(0x0020, 0xFF)
    Sleep(100)

    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    TerminateThread(0x0022, 0xFF)
    TerminateThread(0x0023, 0xFF)
    TerminateThread(0x0024, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    ChrSetChipByIndex(0x0017, 23)
    ChrSetChipByIndex(0x0018, 19)
    ChrSetChipByIndex(0x0019, 8)
    ChrSetChipByIndex(0x001A, 19)
    ChrSetChipByIndex(0x001C, 19)
    ChrSetChipByIndex(0x001D, 8)
    ChrSetChipByIndex(0x001E, 19)
    ChrSetChipByIndex(0x001F, 8)
    ChrSetChipByIndex(0x0020, 19)
    ChrSetChipByIndex(0x0021, 8)
    ChrSetChipByIndex(0x0022, 10)
    ChrSetChipByIndex(0x0023, 10)
    ChrSetChipByIndex(0x0024, 10)
    ChrSetChipByIndex(0x0025, 10)
    ChrSetChipByIndex(0x0026, 10)

    @scena.Lambda('lambda_12D6')
    def lambda_12D6():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_12D6)

    @scena.Lambda('lambda_12E4')
    def lambda_12E4():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_12E4)

    @scena.Lambda('lambda_12F2')
    def lambda_12F2():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_12F2)

    @scena.Lambda('lambda_1300')
    def lambda_1300():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1300)

    @scena.Lambda('lambda_130E')
    def lambda_130E():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_130E)

    @scena.Lambda('lambda_131C')
    def lambda_131C():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_131C)

    @scena.Lambda('lambda_132A')
    def lambda_132A():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_132A)

    @scena.Lambda('lambda_1338')
    def lambda_1338():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_1338)

    @scena.Lambda('lambda_1346')
    def lambda_1346():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1346)

    @scena.Lambda('lambda_1354')
    def lambda_1354():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_1354)

    @scena.Lambda('lambda_1362')
    def lambda_1362():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_1362)

    @scena.Lambda('lambda_1370')
    def lambda_1370():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_1370)

    @scena.Lambda('lambda_137E')
    def lambda_137E():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_137E)

    @scena.Lambda('lambda_138C')
    def lambda_138C():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_138C)

    @scena.Lambda('lambda_139A')
    def lambda_139A():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_139A)

    @scena.Lambda('lambda_13A8')
    def lambda_13A8():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_13A8)

    @scena.Lambda('lambda_13B6')
    def lambda_13B6():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_13B6')

    DispatchAsync2(0x0022, 0x0000, lambda_13B6)

    @scena.Lambda('lambda_13C9')
    def lambda_13C9():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_13C9')

    DispatchAsync2(0x0023, 0x0000, lambda_13C9)

    @scena.Lambda('lambda_13DC')
    def lambda_13DC():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_13DC')

    DispatchAsync2(0x0024, 0x0000, lambda_13DC)

    @scena.Lambda('lambda_13EF')
    def lambda_13EF():
        OP_67(0, 4650, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13EF)

    @scena.Lambda('lambda_1407')
    def lambda_1407():
        OP_6C(291000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1407)

    @scena.Lambda('lambda_1417')
    def lambda_1417():
        CameraMove(16070, 0, 1210, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1417)

    Sleep(350)

    PlayEffect(0x00, 0xFF, 0x001B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0020, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001F, 0xFF)
    TerminateThread(0x0020, 0xFF)

    @scena.Lambda('lambda_14DF')
    def lambda_14DF():
        ChrMoveTo(0x001B, 19380, 0, -1920, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_14DF)

    @scena.Lambda('lambda_14FA')
    def lambda_14FA():
        ChrMoveTo(0x001F, 20690, 0, 1130, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_14FA)

    @scena.Lambda('lambda_1515')
    def lambda_1515():
        ChrMoveTo(0x0020, 18740, 0, 2600, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_1515)

    ChrTurnDirection(0x001B, 0x0028, 0)
    ChrTurnDirection(0x001F, 0x0028, 0)
    ChrTurnDirection(0x0020, 0x0028, 0)
    ChrSetChipByIndex(0x001B, 18)
    ChrSetChipByIndex(0x001F, 18)
    ChrSetChipByIndex(0x0020, 18)
    ChrSetFlags(0x001B, 0x0020)
    ChrSetFlags(0x001F, 0x0020)
    ChrSetFlags(0x0020, 0x0020)

    @scena.Lambda('lambda_1563')
    def lambda_1563():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_1563)

    @scena.Lambda('lambda_1573')
    def lambda_1573():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1573)

    @scena.Lambda('lambda_1583')
    def lambda_1583():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_1583)

    Sleep(30)

    @scena.Lambda('lambda_1598')
    def lambda_1598():
        ChrMoveTo(0x001B, 19380, 0, -1920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_1598)

    @scena.Lambda('lambda_15B3')
    def lambda_15B3():
        ChrMoveTo(0x001F, 20690, 0, 1130, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_15B3)

    @scena.Lambda('lambda_15CE')
    def lambda_15CE():
        ChrMoveTo(0x0020, 18740, 0, 2600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_15CE)

    Sleep(30)

    @scena.Lambda('lambda_15EE')
    def lambda_15EE():
        ChrMoveTo(0x001B, 19380, 0, -1920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_15EE)

    @scena.Lambda('lambda_1609')
    def lambda_1609():
        ChrMoveTo(0x001F, 20690, 0, 1130, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_1609)

    @scena.Lambda('lambda_1624')
    def lambda_1624():
        ChrMoveTo(0x0020, 18740, 0, 2600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_1624)

    Sleep(30)

    TerminateThread(0x001B, 0x02)
    TerminateThread(0x001F, 0x02)
    TerminateThread(0x0020, 0x02)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0017,
        (
            '#2680130579V#2P游、游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130580V#2P你们打算与军队为敌吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0330130581V#5P很抱歉……\n',
            '你们的所作所为是违法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0320130582V奉陛下的口谕，\n',
            '前来消灭你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4111._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x1711
@scena.Code('func_04_1711')
def func_04_1711():
    ChrSetChipByIndex(0x00FE, 24)
    ChrWalkTo(0x00FE, 17640, 0, -360, 6000, 0x00)
    ChrWalkTo(0x00FE, 21560, 0, 0, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 23)

    Return()

# id: 0x0005 offset: 0x1744
@scena.Code('func_05_1744')
def func_05_1744():
    ChrSetChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 18430, 10, -2280, 6000, 0x00)
    ChrWalkTo(0x00FE, 22420, 0, -2220, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_177C')
    def lambda_177C():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_177C')

    DispatchAsync2(0x00FE, 0x0000, lambda_177C)

    Return()

# id: 0x0006 offset: 0x178A
@scena.Code('func_06_178A')
def func_06_178A():
    ChrSetChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 19470, 0, -110, 6000, 0x00)
    ChrWalkTo(0x00FE, 23240, 0, -50, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_17C2')
    def lambda_17C2():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_17C2')

    DispatchAsync2(0x00FE, 0x0000, lambda_17C2)

    Return()

# id: 0x0007 offset: 0x17D0
@scena.Code('func_07_17D0')
def func_07_17D0():
    ChrSetChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 17780, 0, 1050, 6000, 0x00)
    ChrWalkTo(0x00FE, 22340, 0, 1920, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_1808')
    def lambda_1808():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1808')

    DispatchAsync2(0x00FE, 0x0000, lambda_1808)

    Return()

# id: 0x0008 offset: 0x1816
@scena.Code('func_08_1816')
def func_08_1816():
    ChrSetChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 17510, 0, -2090, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_183A')
    def lambda_183A():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_183A')

    DispatchAsync2(0x00FE, 0x0000, lambda_183A)

    Return()

# id: 0x0009 offset: 0x1848
@scena.Code('func_09_1848')
def func_09_1848():
    ChrSetChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 17230, 0, 2360, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_186C')
    def lambda_186C():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_186C')

    DispatchAsync2(0x00FE, 0x0000, lambda_186C)

    Return()

# id: 0x000A offset: 0x187A
@scena.Code('func_0A_187A')
def func_0A_187A():
    ChrSetChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 21940, 100, -3370, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 19)

    Return()

# id: 0x000B offset: 0x18AD
@scena.Code('func_0B_18AD')
def func_0B_18AD():
    ChrSetChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 20370, 20, -2280, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 8)

    Return()

# id: 0x000C offset: 0x18E0
@scena.Code('func_0C_18E0')
def func_0C_18E0():
    ChrSetChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 20460, 0, -750, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 19)

    Return()

# id: 0x000D offset: 0x1913
@scena.Code('func_0D_1913')
def func_0D_1913():
    ChrSetChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 18470, 0, -690, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 8)

    Return()

# id: 0x000E offset: 0x1932
@scena.Code('func_0E_1932')
def func_0E_1932():
    ChrSetChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 19200, 30, -3090, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 19)

    Return()

# id: 0x000F offset: 0x1965
@scena.Code('func_0F_1965')
def func_0F_1965():
    ChrSetChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 21670, 0, 3110, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 8)

    Return()

# id: 0x0010 offset: 0x1998
@scena.Code('func_10_1998')
def func_10_1998():
    ChrSetChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 20410, 0, 1810, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 19)

    Return()

# id: 0x0011 offset: 0x19CB
@scena.Code('func_11_19CB')
def func_11_19CB():
    ChrSetChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 19710, 0, 540, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 8)

    Return()

# id: 0x0012 offset: 0x19FE
@scena.Code('func_12_19FE')
def func_12_19FE():
    ChrSetChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 18220, 0, 1520, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 19)

    Return()

# id: 0x0013 offset: 0x1A31
@scena.Code('func_13_1A31')
def func_13_1A31():
    ChrSetChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 19540, 0, 3570, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 8)

    Return()

# id: 0x0014 offset: 0x1A64
@scena.Code('func_14_1A64')
def func_14_1A64():
    EventBegin(0x00)
    CameraMove(46220, -50, 11920, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(366, 0)
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationAddMember(0x00, 0xFF)
    FormationAddMember(0x02, 0xFF)
    FormationAddMember(0x04, 0xFF)
    OP_B5(0x0002, 0x00)
    OP_B5(0x0002, 0x01)
    OP_B5(0x0002, 0x02)
    OP_B5(0x0002, 0x03)
    OP_B5(0x0002, 0x04)
    OP_B5(0x0002, 0x05)
    EquipCmd(0x02, 0x0040)
    EquipCmd(0x02, 0x00F5)
    EquipCmd(0x02, 0x0113)
    EquipCmd(0x02, 0x026E, 0x00)
    EquipCmd(0x02, 0x026B, 0x01)
    EquipCmd(0x02, 0x025F, 0x02)
    EquipCmd(0x02, 0x0262, 0x03)
    EquipCmd(0x02, 0x0268, 0x04)
    EquipCmd(0x02, 0x0271, 0x05)
    AddCraft(0x0002, 0x00AA)
    AddCraft(0x0002, 0x00AB)
    AddSCraft(0x0002, 0x00F0)
    OP_B5(0x0004, 0x00)
    OP_B5(0x0004, 0x05)
    OP_B5(0x0004, 0x04)
    OP_B5(0x0004, 0x03)
    OP_B5(0x0004, 0x02)
    OP_B5(0x0004, 0x01)
    EquipCmd(0x04, 0x007C)
    EquipCmd(0x04, 0x00F5)
    EquipCmd(0x04, 0x0113)
    EquipCmd(0x04, 0x0259, 0x00)
    EquipCmd(0x04, 0x0261, 0x05)
    EquipCmd(0x04, 0x02C8, 0x04)
    EquipCmd(0x04, 0x0264, 0x03)
    EquipCmd(0x04, 0x025F, 0x02)
    EquipCmd(0x04, 0x027E, 0x01)
    AddCraft(0x0004, 0x00BE)
    AddCraft(0x0004, 0x00BF)
    AddSCraft(0x0004, 0x00FA)
    ChrSetPos(0x0101, 46320, -10, -1800, 0)
    ChrSetPos(0x0103, 47360, 0, -2280, 0)
    ChrSetPos(0x0105, 45230, 0, -2280, 0)

    @scena.Lambda('lambda_1B8A')
    def lambda_1B8A():
        CameraMove(46300, -40, -1440, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B8A)

    @scena.Lambda('lambda_1BA2')
    def lambda_1BA2():
        OP_6E(262, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1BA2)

    Sleep(7000)

    ChrTalk(
        0x0101,
        (
            '#000F情报部的特务艇……\n',
            '没想到要在这种情况下乘坐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F怎么说好呢……\n',
            '真是造型随便、低俗的飞艇啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '和空贼艇真是棋逢对手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940001V#040F不过，拥有很强大的性能\n',
            '这一点是没错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060940002V这样的一艘飞船，\n',
            '情报部是怎么得到的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F确实有很多谜团呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0027, 46370, 200, 5440, 180)
    ChrClearFlags(0x0027, 0x0080)

    @scena.Lambda('lambda_1CE9')
    def lambda_1CE9():
        ChrWalkTo(0x00FE, 46370, 200, 1090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_1CE9)

    Sleep(500)

    @scena.Lambda('lambda_1D09')
    def lambda_1D09():
        CameraMove(46270, 200, 430, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D09)

    WaitForThreadExit(0x0027, 0x0001)

    ChrTalk(
        0x0027,
        (
            '呀，是殿下啊。\n',
            '让您久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F佩顿师傅。。\n',
            '你好，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F咦……这个人是?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940003V#040F他是佩顿师傅，\n',
            '『埃尔赛尤号』飞船\n',
            '的维修人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '我是由中央工房\n',
            '外派的技术人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '『埃尔赛尤号』\n',
            '现在还处于测试阶段，\n',
            '不能用于实战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131068V在卢安看到它的时候\n',
            '可是飞的好好的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '一般的飞行当然是可以的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '因为新型的导力引擎开发进度\n',
            '推迟而搭载了旧型的引擎，\n',
            '这样就不能发挥其应有的性能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '而且现在『埃尔赛尤号』又被\n',
            '情报部给夺走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '我在王都走投无路的时候，\n',
            '尤莉亚中尉就让我到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131073V#000F原来是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵……\n',
            '请多多指教哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '好、好的，交给我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '只要解开锁定，\n',
            '就可以启动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0027, 44540, 200, 1020, 2000, 0x00)
    ChrTurnDirection(0x0027, 0x0105, 400)

    @scena.Lambda('lambda_1FFE')
    def lambda_1FFE():
        ChrTurnDirection(0x00FE, 0x0105, 0)
        Yield()

        Jump('lambda_1FFE')

    DispatchAsync2(0x0027, 0x0003, lambda_1FFE)

    ChrTalk(
        0x0027,
        (
            '因为飞艇的机动性很高，\n',
            '所以驾驶时要小心才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那么，\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x2067
@scena.Code('func_15_2067')
def func_15_2067():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 7, 0x65F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 6, 0x65E)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2074',
    )

    Return()

    def _loc_2074(): pass

    label('loc_2074')

    EventBegin(0x00)

    ChrTalk(
        0x0027,
        (
            '#2350131080V……哦，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131081V我带了一些可以调整\n',
            '大家的导力器的工具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131082V还有，虽然种类不多，\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F哎呀，还是挺会办事的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F真是帮了我们大忙了。\n',
            '真是非常感谢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '东、东西不多，希望能派上用场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131087V有需要的话请说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00CB, 7, 0x65F))
    EventEnd(0x01)

    Return()

# id: 0x0016 offset: 0x21B3
@scena.Code('func_16_21B3')
def func_16_21B3():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0105, 46310, 200, 4320, 176)
    ChrSetPos(0x0103, 46840, 200, 3150, 0)
    ChrSetPos(0x0101, 45710, 200, 3160, 0)
    ChrTurnDirection(0x0027, 0x0105, 0)
    CameraMove(46390, 250, 4580, 1000)

    ChrTalk(
        0x0105,
        (
            '#040F距离正午已经\n',
            '没有多少时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131092V要乘坐飞艇\n',
            '并启动引擎吗？',
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '乘坐飞艇\n'),
            TXT(0x01, ' \n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_22B0'),
        (0x00000001, 'loc_22C8'),
        (-1, 'loc_2322'),
    )

    def _loc_22B0(): pass

    label('loc_22B0')

    ChrTalk(
        0x0105,
        (
            '#040F我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2322')

    def _loc_22C8(): pass

    label('loc_22C8')

    ChrTalk(
        0x0105,
        (
            '#040F我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131095V#020F如果想整理装备的话\n',
            '就和修理员师傅说一声吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_2322(): pass

    label('loc_2322')

    SetScenaFlags(ScenaFlag(0x00CC, 0, 0x660))
    OP_28(0x004D, 0x01, 0x0020)
    ChrTurnDirection(0x0105, 0x0027, 400)

    ChrTalk(
        0x0105,
        (
            '#040F……佩顿师傅，\n',
            '请您在后面协助我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '引擎的调整就交给我吧，\n',
            '请殿下专心的驾驶飞艇！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#000F雪拉姐，终于要开始了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030131100V#020F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '任务虽然很艰巨，\n',
            '不过原则是相通的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131102V迅速果敢……以及沉着冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x2449
@scena.Code('func_17_2449')
def func_17_2449():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 6, 0x65E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_25D9',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24E4',
    )

    ChrTurnDirection(0x0105, 0x0000, 400)

    ChrTalk(
        0x0105,
        (
            '#0060940004V#042F嗯，距离正午已经\n',
            '没有多少时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '准备好了的话，\n',
            '我们就上飞艇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#002F嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25BE')

    def _loc_24E4(): pass

    label('loc_24E4')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2562',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030840005V#026F距离作战开始\n',
            '已经没有多少时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840006V#027F确认完装备\n',
            '就赶快上飞艇去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25BE')

    def _loc_2562(): pass

    label('loc_2562')

    ChrTurnDirection(0x0105, 0x0001, 400)

    ChrTalk(
        0x0105,
        (
            '#0060131108V#042F距离正午已经\n',
            '没有多少时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '准备好了的话，\n',
            '我们就上飞艇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25BE(): pass

    label('loc_25BE')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_25D9(): pass

    label('loc_25D9')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
