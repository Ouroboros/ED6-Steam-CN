import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4111.x'
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
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT09/CH10820._CH', 'ED6_DT09/CH10820P._CP'),
        ('ED6_DT09/CH10821._CH', 'ED6_DT09/CH10821P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00172._CH', 'ED6_DT07/CH00172P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
        ('ED6_DT07/CH00112._CH', 'ED6_DT07/CH00112P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT06/CH20116._CH', 'ED6_DT06/CH20116P._CP'),
        ('ED6_DT06/CH20117._CH', 'ED6_DT06/CH20117P._CP'),
    ]

# id: 0x10001 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '修女艾伦',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            dword_10            = 9,
            chipIndex           = 9,
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
            dword_10            = 9,
            chipIndex           = 9,
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
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 14,
            chipIndex           = 14,
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
            dword_10            = 15,
            chipIndex           = 15,
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
            dword_10            = 16,
            chipIndex           = 16,
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
            dword_10            = 17,
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
            dword_10            = 17,
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
            dword_10            = 17,
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
            dword_10            = 17,
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
            dword_10            = 17,
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
            dword_10            = 17,
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
            dword_10            = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x44A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x44A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 32110,
            y           = -1000,
            z           = -45500,
            range       = 35850,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF84AE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = -88800,
            y           = -1000,
            z           = -3040,
            range       = -85900,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFB7EE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = 70260,
            y           = -1000,
            z           = 32570,
            range       = 56300,
            dword_10    = 0x000007D0,
            dword_14    = 0x00007602,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x4AA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -18470,
            triggerZ            = 0,
            triggerY            = -5070,
            triggerRange        = 1500,
            actorX              = -18470,
            actorZ              = 1700,
            actorY              = -5070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4CE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_4E5',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_03_2380)

    def _loc_4E5(): pass

    label('loc_4E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_4F3',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_04_2E00)

    def _loc_4F3(): pass

    label('loc_4F3')

    Return()

# id: 0x0001 offset: 0x4F4
@scena.Code('func_01_4F4')
def func_01_4F4():
    OP_16(0x02, 4000, -140000, -140000, 196708)

    Return()

# id: 0x0002 offset: 0x507
@scena.Code('func_02_507')
def func_02_507():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 5, 0x615)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_237F',
    )

    EventBegin(0x00)
    ChrSetPos(0x0008, 14740, 0, -49400, 225)
    ChrSetPos(0x0009, 12040, 0, -49370, 90)
    ChrSetPos(0x000A, 12070, 0, -51990, 45)
    ChrSetPos(0x000B, 14800, 0, -52250, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    SetScenaFlags(ScenaFlag(0x00C2, 6, 0x616))

    ChrTalk(
        0x0008,
        (
            '#0100101363V……呀啊啊～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 0)
    ChrTurnDirection(0x0102, 0x0008, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F是女人的惨叫！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F在这里面，赶快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(13190, 0, -50600, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3070, 0)
    OP_6C(282000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 20850, 0, -44670, 0)
    ChrSetPos(0x0102, 19400, 0, -43210, 0)

    ChrTalk(
        0x0008,
        (
            '#0100101366V呀啊啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101367V救命啊！\n',
            '谁来帮忙啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0009, 2)

    @scena.Lambda('lambda_06C6')
    def lambda_06C6():
        OP_92(0x00FE, 0x0008, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_06C6)

    Sleep(50)

    ChrSetChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_06E5')
    def lambda_06E5():
        OP_92(0x00FE, 0x0008, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_06E5)

    Sleep(100)

    ChrSetChipByIndex(0x000B, 2)

    @scena.Lambda('lambda_0704')
    def lambda_0704():
        OP_92(0x00FE, 0x0008, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0704)

    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 5)

    @scena.Lambda('lambda_0723')
    def lambda_0723():
        ChrWalkTo(0x00FE, 15230, 0, -50290, 8500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0723)

    @scena.Lambda('lambda_073E')
    def lambda_073E():
        ChrWalkTo(0x00FE, 13790, 0, -48820, 8500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_073E)

    Sleep(600)

    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 11)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)

    @scena.Lambda('lambda_0772')
    def lambda_0772():
        OP_99(0x00FE, 0x00, 0x0B, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0772)

    @scena.Lambda('lambda_0782')
    def lambda_0782():
        OP_99(0x00FE, 0x00, 0x0B, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0782)

    WaitForThreadExit(0x0102, 0x0001)
    ChrSetChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_079C')
    def lambda_079C():
        ChrJumpToRelative(0x00FE, -2000, 0, 0, 1000, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_079C)

    ChrSetChipByIndex(0x000B, 1)

    @scena.Lambda('lambda_07BF')
    def lambda_07BF():
        ChrJumpToRelative(0x00FE, 0, 0, -2000, 1000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07BF)

    ChrTurnDirection(0x0101, 0x000B, 0)
    ChrTurnDirection(0x0102, 0x0009, 0)

    @scena.Lambda('lambda_07EB')
    def lambda_07EB():
        ChrMoveTo(0x00FE, 14510, 0, -50410, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07EB)

    @scena.Lambda('lambda_0806')
    def lambda_0806():
        ChrMoveTo(0x00FE, 13780, 0, -49680, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0806)

    Sleep(150)

    ChrSetChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_082B')
    def lambda_082B():
        ChrJumpToRelative(0x00FE, -700, 0, -700, 1000, 6000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_082B)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0100101368V哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F修女！\n',
            '已经没事了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F很危险，\n',
            '所以请退到后面去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08AA')
    def lambda_08AA():
        OP_92(0x00FE, 0x0008, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_08AA)

    @scena.Lambda('lambda_08BF')
    def lambda_08BF():
        OP_92(0x00FE, 0x0008, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_08BF)

    @scena.Lambda('lambda_08D4')
    def lambda_08D4():
        OP_92(0x00FE, 0x0008, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_08D4)

    Sleep(500)

    Battle(0x000003A3, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_901'),
        (-1, 'loc_904'),
    )

    def _loc_901(): pass

    label('loc_901')

    OP_B4(0x00)

    Return()

    def _loc_904(): pass

    label('loc_904')

    FormationAddMember(0x07, 0xFF)
    ChrSetPos(0x0108, 22520, 0, -37100, 0)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x0101, 14390, 0, -50980, 225)
    ChrSetPos(0x0102, 12920, 0, -49800, 225)
    ChrSetPos(0x0008, 14740, 0, -49400, 225)
    CameraMove(13730, 0, -50080, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3070, 0)
    OP_6C(282000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 5)
    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#000F呼……\n',
            '真是厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#000F修女，你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_09F8')
    def lambda_09F8():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_09F8)

    ChrTalk(
        0x0008,
        (
            '#0100101373V啊，是的……多亏了你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101374V嗯……你们到底是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101375V#010F我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101376V正在找人的途中，\n',
            '听到了你的惨叫，所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101377V是……这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101378V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F怎、怎么了？\n',
            '看起来好像很没精神的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101380V难道受伤了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101381V没有……\n',
            '多亏了你们，才平安无事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0101060002V我是王都大圣堂的修女，\n',
            '名叫艾伦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101383V真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈。\n',
            '不用谢啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过，\n',
            '作为圣职者的女性\n',
            '一个人来这种地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101386V你没有和其他人\n',
            '一起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0101060003V是的，不好意思，\n',
            '只有我一个人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101388V其实是因为大圣堂里\n',
            '调药用的草药没有了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101389V商店里也卖完了，\n',
            '所以才来这里采集的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这也太危险了。\n',
            '明明到处都是魔兽啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101391V不，以前这里\n',
            '没有这么多魔兽的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101392V好像是从最近\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 5)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    Sleep(500)

    @scena.Lambda('lambda_0DD1')
    def lambda_0DD1():
        ChrWalkTo(0x00FE, 15570, 0, -49480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DD1)

    Sleep(100)

    @scena.Lambda('lambda_0DF1')
    def lambda_0DF1():
        ChrWalkTo(0x00FE, 14280, 0, -48510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0DF1)

    ChrSetDirection(0x0008, 45, 400)

    ChrTalk(
        0x0008,
        (
            '#0100101393V啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0E42')
    def lambda_0E42():
        ChrMoveTo(0x00FE, 14210, 0, -50140, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0E42)

    ChrSetPos(0x0009, 19840, 0, -40400, 0)
    ChrSetPos(0x000A, 21100, 0, -41220, 0)
    ChrSetPos(0x000B, 21440, 0, -39410, 0)
    ChrSetPos(0x000C, 21420, 0, -38390, 0)
    ChrSetPos(0x000D, 23130, 0, -39910, 0)
    ChrSetPos(0x000E, 21460, 0, -36780, 0)
    ChrSetPos(0x000F, 23510, 0, -37150, 0)
    ChrSetPos(0x0010, 24560, 0, -39000, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    @scena.Lambda('lambda_0F0D')
    def lambda_0F0D():
        ChrWalkTo(0x00FE, 15280, 0, -45500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0F0D)

    @scena.Lambda('lambda_0F28')
    def lambda_0F28():
        ChrWalkTo(0x00FE, 17370, 0, -46170, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F28)

    @scena.Lambda('lambda_0F43')
    def lambda_0F43():
        ChrWalkTo(0x00FE, 16610, 0, -44960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0F43)

    @scena.Lambda('lambda_0F5E')
    def lambda_0F5E():
        ChrWalkTo(0x00FE, 16300, 0, -43340, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0F5E)

    @scena.Lambda('lambda_0F79')
    def lambda_0F79():
        ChrWalkTo(0x00FE, 18970, 0, -44750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0F79)

    @scena.Lambda('lambda_0F94')
    def lambda_0F94():
        ChrWalkTo(0x00FE, 17210, 0, -42380, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0F94)

    @scena.Lambda('lambda_0FAF')
    def lambda_0FAF():
        ChrWalkTo(0x00FE, 19190, 0, -42290, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0FAF)

    @scena.Lambda('lambda_0FCA')
    def lambda_0FCA():
        ChrWalkTo(0x00FE, 19060, 0, -43530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0FCA)

    Sleep(300)

    @scena.Lambda('lambda_0FEA')
    def lambda_0FEA():
        CameraMove(19250, 0, -43570, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FEA)

    @scena.Lambda('lambda_1002')
    def lambda_1002():
        OP_6C(0, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1002)

    Sleep(1500)

    @scena.Lambda('lambda_1017')
    def lambda_1017():
        CameraMove(17110, 0, -45970, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1017)

    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#000F怎么回事啊，这些家伙们……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好像是因为\n',
            '听到骚动而聚集过来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101396V有这么多，还真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，以防万一，\n',
            '至少先让修女逃出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0108, 0x0080)
    ChrWalkTo(0x0108, 21130, 0, -40520, 12000, 0x00)

    @scena.Lambda('lambda_10F8')
    def lambda_10F8():
        CameraMove(17970, 0, -45090, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10F8)

    ChrSetChipByIndex(0x0108, 8)
    ChrSetFlags(0x0108, 0x0020)
    ChrSetFlags(0x0108, 0x1000)

    @scena.Lambda('lambda_111F')
    def lambda_111F():
        OP_99(0x00FE, 0x00, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_111F)

    ChrWalkTo(0x0108, 19670, 0, -41930, 12000, 0x00)
    PlayEffect(0x08, 0xFF, 0x00FF, 19660, 0, -41900, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1178')
    def lambda_1178():
        ChrMoveTo(0x00FE, 17370, 0, -43990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1178)

    @scena.Lambda('lambda_1193')
    def lambda_1193():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1193)

    @scena.Lambda('lambda_11A5')
    def lambda_11A5():
        OP_99(0x00FE, 0x04, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_11A5)

    ChrJumpTo(0x0108, 20380, 0, -41250, 1000, 6000)

    ChrTalk(
        0x0108,
        (
            '#0081040001V哦，看起来你们遇到麻烦了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11F8')
    def lambda_11F8():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_11F8)

    @scena.Lambda('lambda_1206')
    def lambda_1206():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1206)

    @scena.Lambda('lambda_1214')
    def lambda_1214():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1214)

    @scena.Lambda('lambda_1222')
    def lambda_1222():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1222)

    @scena.Lambda('lambda_1230')
    def lambda_1230():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1230)

    ChrTalk(
        0x0101,
        (
            '#000F啊，金先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F太好了……\n',
            '终于发现了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101401V#070F嘿嘿，\n',
            '我还以为是谁，原来是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101402V总之，要说的话一会儿再说，\n',
            '赶快把这些家伙们收拾掉吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1318')
    def lambda_1318():
        OP_99(0x00FE, 0x00, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1318)

    @scena.Lambda('lambda_1328')
    def lambda_1328():
        ChrWalkTo(0x00FE, 16750, 0, -47000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1328)

    @scena.Lambda('lambda_1343')
    def lambda_1343():
        ChrWalkTo(0x00FE, 14860, 0, -46770, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1343)

    ChrWalkTo(0x0108, 18730, 0, -42670, 5000, 0x00)
    Battle(0x000003A4, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1385'),
        (-1, 'loc_1388'),
    )

    def _loc_1385(): pass

    label('loc_1385')

    OP_B4(0x00)

    Return()

    def _loc_1388(): pass

    label('loc_1388')

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetPos(0x0101, 16770, 0, -47500, 45)
    ChrSetPos(0x0102, 15050, 0, -45990, 45)
    ChrSetPos(0x0108, 17690, 0, -44440, 225)
    ChrSetPos(0x0008, 14650, 0, -48360, 45)
    CameraMove(15920, 0, -45970, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0108, 0x1000)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0108,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrClearFlags(0x0108, 0x0020)
    ChrClearFlags(0x0108, 0x1000)

    ChrTalk(
        0x0108,
        (
            '#070F哎呀哎呀……\n',
            '多亏了这些家伙们，让我好好地出了一次汗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，真没想到\n',
            '能在这里见到你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101407V你们不是在\n',
            '蔡斯地区工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈，确实从那时候起\n',
            '就一直没有像这样见面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F其实我们已经从蔡斯支部\n',
            '转属到格兰赛尔支部来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101410V#070F哦，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101411V也就是说，那个绑架事件，\n',
            '已经解决了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那个中毒的红发小哥\n',
            '现在还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101414V……请问…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哦，真是失礼了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '…………啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1691')
    def lambda_1691():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1691')

    DispatchAsync2(0x0108, 0x0001, lambda_1691)

    ChrMoveTo(0x0108, 15730, 0, -45650, 2000, 0x00)

    ChrTalk(
        0x0108,
        (
            '#070F喂喂……\n',
            '真是个美人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040002V是你们的同伴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#010F不是，\n',
            '我们也是刚认识的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#000F真是的，这么色迷迷的，\n',
            '也不知道害羞……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我去告诉雾香小姐吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0108, 0xFF)
    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#070F呜……\n',
            '我只是说陈述客观的事实罢了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '喂，\n',
            '为什么要提到那家伙的名字啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 15250, 0, -47500, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0100101424V那个……把我从危险的地方救出来，\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101425V你们都是我的救命恩人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_184D')
    def lambda_184D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_184D')

    DispatchAsync2(0x0108, 0x0001, lambda_184D)

    @scena.Lambda('lambda_185E')
    def lambda_185E():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_185E')

    DispatchAsync2(0x0102, 0x0001, lambda_185E)

    ChrMoveTo(0x0108, 15810, 0, -46820, 2000, 0x00)

    ChrTalk(
        0x0108,
        (
            '#070F没什么没什么，请别放在心上！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040003V作为男人，\n',
            '就应该贯彻武侠之道嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101428V哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F好像在装帅呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '金先生\n',
            '其实对女人没有办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哈哈……\n',
            '说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0011, 22440, 0, -38100, 0)
    ChrSetPos(0x0012, 21240, 0, -37930, 0)

    ChrTalk(
        0x0011,
        (
            '你们在干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_198B')
    def lambda_198B():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_198B')

    DispatchAsync2(0x0108, 0x0002, lambda_198B)

    @scena.Lambda('lambda_199C')
    def lambda_199C():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_199C')

    DispatchAsync2(0x0101, 0x0002, lambda_199C)

    @scena.Lambda('lambda_19AD')
    def lambda_19AD():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_19AD')

    DispatchAsync2(0x0102, 0x0002, lambda_19AD)

    @scena.Lambda('lambda_19BE')
    def lambda_19BE():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_19BE')

    DispatchAsync2(0x0008, 0x0002, lambda_19BE)

    @scena.Lambda('lambda_19CF')
    def lambda_19CF():
        ChrWalkTo(0x00FE, 18650, 0, -44020, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_19CF)

    @scena.Lambda('lambda_19EA')
    def lambda_19EA():
        ChrWalkTo(0x00FE, 17460, 0, -43540, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_19EA)

    CameraMove(17010, 0, -44670, 3000)

    ChrTalk(
        0x0101,
        (
            '#000F哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0011, 0x0001)

    ChrTalk(
        0x0011,
        (
            '#2620101435V在这种没人的地方密谈，\n',
            '真是可疑的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '难道……\n',
            '你们是恐怖分子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 16770, 0, -46090, 4000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#10A#000F谁、谁是恐怖分子啊！？\n',
            '我们是——呜。',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    ChrWalkTo(0x0102, 16170, 0, -46090, 4000, 0x00)

    @scena.Lambda('lambda_1B0E')
    def lambda_1B0E():
        ChrWalkTo(0x00FE, 17150, 0, -46640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B0E)

    ChrMoveTo(0x0102, 16770, 0, -46090, 2000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#010F……我们是游击士协会\n',
            '格兰赛尔支部所属的成员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101439V就在刚才，我们保护了\n',
            '这位修女免遭魔兽袭击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101440V什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '是游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 14980, 0, -46240, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0100101442V那个……\n',
            '他们说的都是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101443V我来这里采摘草药，\n',
            '结果被魔兽袭击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F顺便一说，我也是游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101445V我记得和你们的同伴\n',
            '在预选赛中曾经碰过面对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101446V卡尔瓦德的武术家……\n',
            '那个一个人参赛的家伙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '哼……\n',
            '身份好像可以确定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101448V这次就放过你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101449V不过，这里离艾尔贝离宫很近。\n',
            '没事不要在这边乱转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '还有，修女小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我们把你\n',
            '送回王都去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '不要借助\n',
            '什么游击士的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101453V哎，但、但是我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F可恶，等一下，你们！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101455V从刚才开始，\n',
            '就一直在说过分的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔……算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0011, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101457V#010F以后我们会注意的，\n',
            '这次能宽大处理，真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101458V哼，算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101459V你们到底只不过是普通市民。\n',
            '弄清楚自己的本分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '那么，修女小姐，我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101461V好、好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    ChrWalkTo(0x0008, 17000, 0, -44710, 3000, 0x00)
    ChrTurnDirection(0x0008, 0x0108, 400)

    ChrTalk(
        0x0008,
        (
            '那个，各位……\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1FAF')
    def lambda_1FAF():
        ChrWalkTo(0x00FE, 23730, 0, -36620, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1FAF)

    Sleep(100)

    @scena.Lambda('lambda_1FCF')
    def lambda_1FCF():
        ChrWalkTo(0x00FE, 23730, 0, -36620, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1FCF)

    Sleep(200)

    @scena.Lambda('lambda_1FEF')
    def lambda_1FEF():
        ChrWalkTo(0x00FE, 23730, 0, -36620, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1FEF)

    Sleep(2000)

    OP_62(0x0101, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    CameraMove(17150, 0, -46640, 1000)
    Sleep(100)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#000F什、什、什……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '什么啊！那些家伙们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040004V#070F是王国军情报部所属的\n',
            '『特务部队』的人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101466V虽然很厉害，\n',
            '不过是很阴险的家伙们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_20EA')
    def lambda_20EA():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_20EA)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#000F比起阴险来说，\n',
            '倒不如说是品行恶劣呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101469V为什么金先生\n',
            '你会知道他们的事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080101470V#070F啊，武术大会的预选赛，\n',
            '他们的队伍也出场了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101471V那时就是这样介绍的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（那些家伙也有出场……！？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101473V（平时进行隐秘活动那些家伙们\n',
            '这样堂堂正正地被人看到……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（大概是没有\n',
            '再隐藏自己存在的必要了吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F总之，在弄清楚原因之前，\n',
            '我们还是赶快回城去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……对了，\n',
            '你们为什么会在这里的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……都忘了重要的事情呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '其实，\n',
            '我们是来找金先生你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯？找我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F其实有件事情\n',
            '想拜托金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101481V是有关武术大会的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4130._SN', 100, 0, 0)
    IdleLoop()

    def _loc_237F(): pass

    label('loc_237F')

    Return()

# id: 0x0003 offset: 0x2380
@scena.Code('func_03_2380')
def func_03_2380():
    EventBegin(0x00)
    ChrSetPos(0x0101, 11690, 0, -52560, 225)
    ChrSetPos(0x0102, 11000, 0, -51680, 225)
    ChrSetPos(0x0108, 10930, 0, -50240, 196)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0013, 14410, 0, -53900, 257)
    ChrSetPos(0x0014, 14820, 0, -52280, 244)
    ChrSetPos(0x0015, 13050, 0, -51640, 207)
    ChrSetPos(0x0016, 13090, 0, -50260, 213)
    CameraMove(11570, 250, -53400, 0)
    OP_67(0, 7270, -10000, 0)
    CameraSetDistance(2710, 0)
    OP_6C(225000, 0)
    OP_6E(395, 0)
    FadeIn(3000, 0)

    @scena.Lambda('lambda_2459')
    def lambda_2459():
        OP_6C(249000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2459)

    OP_6E(309, 5000)

    ChrTalk(
        0x0101,
        (
            '#0010130532V#006F嗯……\n',
            '这里就是集合点吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130533V#010F在琥耀石的石碑旁的休息场所，\n',
            '和这里完全符合。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130534V#013F问题是，\n',
            '尤莉亚中尉他们还没来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x0017, 17080, 0, -45130, 225)
    ChrSetPos(0x0018, 17100, 0, -43830, 225)
    ChrSetPos(0x0019, 18380, 0, -45010, 225)
    ChrSetPos(0x001A, 17740, 0, -42700, 225)
    ChrSetPos(0x001B, 18600, 0, -43670, 225)
    ChrSetPos(0x001C, 19480, 0, -44620, 225)
    ChrSetPos(0x001D, 18580, 0, -41840, 225)
    ChrSetPos(0x001E, 19520, 0, -42690, 225)
    ChrSetPos(0x001F, 20400, 0, -43690, 225)

    @scena.Lambda('lambda_25E2')
    def lambda_25E2():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_25E2)

    @scena.Lambda('lambda_25FD')
    def lambda_25FD():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_25FD)

    @scena.Lambda('lambda_2618')
    def lambda_2618():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_2618)

    @scena.Lambda('lambda_2633')
    def lambda_2633():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_2633)

    @scena.Lambda('lambda_264E')
    def lambda_264E():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_264E)

    @scena.Lambda('lambda_2669')
    def lambda_2669():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_2669)

    @scena.Lambda('lambda_2684')
    def lambda_2684():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_2684)

    @scena.Lambda('lambda_269F')
    def lambda_269F():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_269F)

    @scena.Lambda('lambda_26BA')
    def lambda_26BA():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_26BA)

    ChrTalk(
        0x0017,
        (
            '#0100130535V#1P……请不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_272D')
    def lambda_272D():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_272D)

    @scena.Lambda('lambda_273B')
    def lambda_273B():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_273B)

    @scena.Lambda('lambda_2749')
    def lambda_2749():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2749)

    @scena.Lambda('lambda_2757')
    def lambda_2757():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_2757)

    @scena.Lambda('lambda_2765')
    def lambda_2765():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_2765)

    @scena.Lambda('lambda_2773')
    def lambda_2773():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_2773)

    @scena.Lambda('lambda_2781')
    def lambda_2781():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_2781)

    @scena.Lambda('lambda_278F')
    def lambda_278F():
        OP_6C(335000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_278F)

    @scena.Lambda('lambda_279F')
    def lambda_279F():
        OP_6E(332, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_279F)

    @scena.Lambda('lambda_27AF')
    def lambda_27AF():
        CameraMove(13880, 0, -49890, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_27AF)

    @scena.Lambda('lambda_27C7')
    def lambda_27C7():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_27C7)

    Sleep(100)

    @scena.Lambda('lambda_27E7')
    def lambda_27E7():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_27E7)

    @scena.Lambda('lambda_2802')
    def lambda_2802():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_2802)

    Sleep(100)

    @scena.Lambda('lambda_2822')
    def lambda_2822():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_2822)

    @scena.Lambda('lambda_283D')
    def lambda_283D():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_283D)

    @scena.Lambda('lambda_2858')
    def lambda_2858():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_2858)

    Sleep(100)

    @scena.Lambda('lambda_2878')
    def lambda_2878():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_2878)

    @scena.Lambda('lambda_2893')
    def lambda_2893():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_2893)

    @scena.Lambda('lambda_28AE')
    def lambda_28AE():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_28AE)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0017, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010130536V#004F哇，什么时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130537V#071F哈哈……\n',
            '原来有这么多人潜伏在王都啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0100130538V#176F市民中也有很多人支持我们。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130539V#170F我们这边已经准备好了，\n',
            '随时可以开始作战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0330130540V好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0016, 0x0101, 400)

    ChrTalk(
        0x0016,
        (
            '#0330130541V#5P艾丝蒂尔，\n',
            '请发号施令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_29F1')
    def lambda_29F1():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_29F1)

    @scena.Lambda('lambda_29FF')
    def lambda_29FF():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_29FF)

    @scena.Lambda('lambda_2A0D')
    def lambda_2A0D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_2A0D)

    @scena.Lambda('lambda_2A1B')
    def lambda_2A1B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_2A1B)

    @scena.Lambda('lambda_2A29')
    def lambda_2A29():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_2A29)

    @scena.Lambda('lambda_2A37')
    def lambda_2A37():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_2A37)

    ChrTalk(
        0x0101,
        (
            '#0010130542V#580F咦……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130543V我、我来！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0330130544V#5P因为是由你们\n',
            '接受女王委托的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0310130545V#5P是啊，\n',
            '由你来发号施令是理所当然的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130546V#506F可、可是……\n',
            '我还只是个新人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0320130547V#6P哈哈，没关系。\n',
            '由你来我们没有异议的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0120130548V#6P只要声音别叫得太大，\n',
            '就不会惊动到敌人的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0100130549V#171F我们是来协助你们作战的，\n',
            '所以绝对不会有半点异议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130550V#503F啊，哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130551V#010F#5P艾丝蒂尔，要有自信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130552V#071F#5P不用再细想了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130553V这可是老规矩了，老规矩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130554V#008F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130555V#006F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)

    @scena.Lambda('lambda_2CD2')
    def lambda_2CD2():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2CD2')

    DispatchAsync2(0x0102, 0x0001, lambda_2CD2)

    @scena.Lambda('lambda_2CE3')
    def lambda_2CE3():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2CE3')

    DispatchAsync2(0x0108, 0x0001, lambda_2CE3)

    @scena.Lambda('lambda_2CF4')
    def lambda_2CF4():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2CF4')

    DispatchAsync2(0x0013, 0x0001, lambda_2CF4)

    @scena.Lambda('lambda_2D05')
    def lambda_2D05():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2D05')

    DispatchAsync2(0x0014, 0x0001, lambda_2D05)

    @scena.Lambda('lambda_2D16')
    def lambda_2D16():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2D16')

    DispatchAsync2(0x0015, 0x0001, lambda_2D16)

    @scena.Lambda('lambda_2D27')
    def lambda_2D27():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2D27')

    DispatchAsync2(0x0016, 0x0001, lambda_2D27)

    @scena.Lambda('lambda_2D38')
    def lambda_2D38():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2D38)

    ChrWalkTo(0x0101, 10610, 480, -53440, 1500, 0x00)
    OP_20(0x000007D0)
    ChrSetDirection(0x0101, 45, 400)
    WaitForThreadExit(0x0101, 0x0003)
    OP_21()

    ChrTalk(
        0x0101,
        (
            '#0010130556V#006F#5P我向全体作战成员宣布……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010130557V#005F#5P艾尔贝离宫攻略战，\n',
            '暨人质解救作战现在开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4113._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x2E00
@scena.Code('func_04_2E00')
def func_04_2E00():
    EventBegin(0x00)
    CameraMove(-26280, 0, -4400, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(234, 0)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetChipByIndex(0x0018, 19)
    ChrSetChipByIndex(0x0019, 19)
    ChrSetChipByIndex(0x001A, 19)
    ChrSetChipByIndex(0x001B, 19)
    ChrSetSubChip(0x0018, 2)
    ChrSetSubChip(0x0019, 2)
    ChrSetSubChip(0x001A, 2)
    ChrSetSubChip(0x001B, 2)
    ChrSetPos(0x0018, -25890, 0, -4510, 180)
    ChrSetPos(0x0019, -27370, 0, -4510, 180)
    ChrSetPos(0x001A, -27240, 0, -2700, 180)
    ChrSetPos(0x001B, -25950, 0, -2920, 180)
    ChrSetPos(0x0108, -26570, 0, -6220, 0)
    ChrSetPos(0x0102, -28030, 0, -6250, 45)
    ChrSetPos(0x0101, -25360, 0, -6190, 315)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080130583V#072F好，伏击组开始行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#2690130584V#5P我们先行一步，\n',
            '去引开前庭的残存兵力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#2690130585V#5P趁此机会，\n',
            '请你们突入离宫内部！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130586V#006F嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130587V#012F愿女神保佑你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2FE2')
    def lambda_2FE2():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_2FE2')

    DispatchAsync2(0x0101, 0x0001, lambda_2FE2)

    @scena.Lambda('lambda_2FF3')
    def lambda_2FF3():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_2FF3')

    DispatchAsync2(0x0102, 0x0001, lambda_2FF3)

    @scena.Lambda('lambda_3004')
    def lambda_3004():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_3004')

    DispatchAsync2(0x0108, 0x0001, lambda_3004)

    ChrSetChipByIndex(0x001B, 18)

    @scena.Lambda('lambda_301A')
    def lambda_301A():
        ChrSetDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_301A)

    @scena.Lambda('lambda_3028')
    def lambda_3028():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_3028)

    Sleep(200)

    ChrSetChipByIndex(0x001A, 18)

    @scena.Lambda('lambda_304D')
    def lambda_304D():
        ChrSetDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_304D)

    @scena.Lambda('lambda_305B')
    def lambda_305B():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_305B)

    Sleep(200)

    ChrSetChipByIndex(0x0018, 18)

    @scena.Lambda('lambda_3080')
    def lambda_3080():
        ChrSetDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_3080)

    @scena.Lambda('lambda_308E')
    def lambda_308E():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_308E)

    Sleep(200)

    ChrSetChipByIndex(0x0019, 18)

    @scena.Lambda('lambda_30B3')
    def lambda_30B3():
        ChrSetDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_30B3)

    @scena.Lambda('lambda_30C1')
    def lambda_30C1():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_30C1)

    Sleep(2000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    SetScenaFlags(ScenaFlag(0x00CA, 1, 0x651))
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x3101
@scena.Code('func_05_3101')
def func_05_3101():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3279',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_317A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010130520V#002F……在突击的时刻是不能逃离的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130521V立刻赶去艾尔贝离宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_325E')

    def _loc_317A(): pass

    label('loc_317A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31E1',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130522V#012F要突击也只有趁现在了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130523V赶快去艾尔贝离宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_325E')

    def _loc_31E1(): pass

    label('loc_31E1')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_325E',
    )

    ChrTurnDirection(0x0108, 0x0001, 400)

    ChrTalk(
        0x0108,
        (
            '#0080130524V#072F如果现在不行动的话，\n',
            '就没有突入离宫的机会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130525V……赶快去艾尔贝离宫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_325E(): pass

    label('loc_325E')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3279(): pass

    label('loc_3279')

    Return()

# id: 0x0006 offset: 0x327A
@scena.Code('func_06_327A')
def func_06_327A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_33F2',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32F3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010130520V#002F……在突击的时刻是不能逃离的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130521V立刻赶去艾尔贝离宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33D7')

    def _loc_32F3(): pass

    label('loc_32F3')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_335A',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130522V#012F要突击也只有趁现在了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130523V赶快去艾尔贝离宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33D7')

    def _loc_335A(): pass

    label('loc_335A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33D7',
    )

    ChrTurnDirection(0x0108, 0x0001, 400)

    ChrTalk(
        0x0108,
        (
            '#0080130524V#072F如果现在不行动的话，\n',
            '就没有突入离宫的机会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130525V……赶快去艾尔贝离宫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33D7(): pass

    label('loc_33D7')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_33F2(): pass

    label('loc_33F2')

    Return()

# id: 0x0007 offset: 0x33F3
@scena.Code('func_07_33F3')
def func_07_33F3():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　艾尔贝离宫\n',
            '东　格鲁纳门　　２２４塞尔矩\n',
            '西　圣海姆门　　２５６塞尔矩',
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
