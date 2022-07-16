import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4111   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '修女艾伦'),
    TXT(0x02, '魔兽'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '魔兽'),
    TXT(0x06, '魔兽'),
    TXT(0x07, '魔兽'),
    TXT(0x08, '魔兽'),
    TXT(0x09, '魔兽'),
    TXT(0x0A, '特务兵'),
    TXT(0x0B, '特务兵'),
    TXT(0x0C, '卡露娜'),
    TXT(0x0D, '亚妮拉丝'),
    TXT(0x0E, '库拉茨'),
    TXT(0x0F, '克鲁茨'),
    TXT(0x10, '尤莉亚中尉'),
    TXT(0x11, '亲卫队员'),
    TXT(0x12, '亲卫队员'),
    TXT(0x13, '亲卫队员'),
    TXT(0x14, '亲卫队员'),
    TXT(0x15, '亲卫队员'),
    TXT(0x16, '亲卫队员'),
    TXT(0x17, '亲卫队员'),
    TXT(0x18, '亲卫队员'),
    TXT(0x19, ''),
]

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

# id: 0xFFFF offset: 0x328F
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
            word_3A         = 0,
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

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x44A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x44A
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

# id: 0x10005 offset: 0x4AA
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
@scena.Code('PreInit')
def PreInit():
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
    Event(0, 0x0003)

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
    Event(0, 0x0004)

    def _loc_4F3(): pass

    label('loc_4F3')

    Return()

# id: 0x0001 offset: 0x4F4
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -140000, -140000, 196708)

    Return()

# id: 0x0002 offset: 0x507
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 5, 0x615)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2267',
    )

    EventBegin(0x00)
    SetChrPos(0x0008, 14740, 0, -49400, 225)
    SetChrPos(0x0009, 12040, 0, -49370, 90)
    SetChrPos(0x000A, 12070, 0, -51990, 45)
    SetChrPos(0x000B, 14800, 0, -52250, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
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
    SetChrPos(0x0101, 20850, 0, -44670, 0)
    SetChrPos(0x0102, 19400, 0, -43210, 0)

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
    SetChrChipByIndex(0x0009, 2)

    @scena.Lambda('lambda_06B7')
    def lambda_06B7():
        OP_92(0x00FE, 0x0008, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_06B7)

    Sleep(50)

    SetChrChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_06D6')
    def lambda_06D6():
        OP_92(0x00FE, 0x0008, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_06D6)

    Sleep(100)

    SetChrChipByIndex(0x000B, 2)

    @scena.Lambda('lambda_06F5')
    def lambda_06F5():
        OP_92(0x00FE, 0x0008, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_06F5)

    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 5)

    @scena.Lambda('lambda_0714')
    def lambda_0714():
        ChrWalkTo(0x00FE, 15230, 0, -50290, 8500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0714)

    @scena.Lambda('lambda_072F')
    def lambda_072F():
        ChrWalkTo(0x00FE, 13790, 0, -48820, 8500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_072F)

    Sleep(600)

    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 11)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)

    @scena.Lambda('lambda_0763')
    def lambda_0763():
        OP_99(0x00FE, 0x00, 0x0B, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0763)

    @scena.Lambda('lambda_0773')
    def lambda_0773():
        OP_99(0x00FE, 0x00, 0x0B, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0773)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_078D')
    def lambda_078D():
        ChrJumpToRelative(0x00FE, -2000, 0, 0, 1000, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_078D)

    SetChrChipByIndex(0x000B, 1)

    @scena.Lambda('lambda_07B0')
    def lambda_07B0():
        ChrJumpToRelative(0x00FE, 0, 0, -2000, 1000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07B0)

    ChrTurnDirection(0x0101, 0x000B, 0)
    ChrTurnDirection(0x0102, 0x0009, 0)

    @scena.Lambda('lambda_07DC')
    def lambda_07DC():
        ChrMoveTo(0x00FE, 14510, 0, -50410, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07DC)

    @scena.Lambda('lambda_07F7')
    def lambda_07F7():
        ChrMoveTo(0x00FE, 13780, 0, -49680, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_07F7)

    Sleep(150)

    SetChrChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_081C')
    def lambda_081C():
        ChrJumpToRelative(0x00FE, -700, 0, -700, 1000, 6000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_081C)

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

    @scena.Lambda('lambda_0896')
    def lambda_0896():
        OP_92(0x00FE, 0x0008, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0896)

    @scena.Lambda('lambda_08AB')
    def lambda_08AB():
        OP_92(0x00FE, 0x0008, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_08AB)

    @scena.Lambda('lambda_08C0')
    def lambda_08C0():
        OP_92(0x00FE, 0x0008, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_08C0)

    Sleep(500)

    Battle(0x000003A3, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_8ED'),
        (-1, 'loc_8F0'),
    )

    def _loc_8ED(): pass

    label('loc_8ED')

    OP_B4(0x00)

    Return()

    def _loc_8F0(): pass

    label('loc_8F0')

    FormationAddMember(0x07, 0xFF)
    SetChrPos(0x0108, 22520, 0, -37100, 0)
    SetChrFlags(0x0108, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x0101, 14390, 0, -50980, 225)
    SetChrPos(0x0102, 12920, 0, -49800, 225)
    SetChrPos(0x0008, 14740, 0, -49400, 225)
    CameraMove(13730, 0, -50080, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3070, 0)
    OP_6C(282000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 5)
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
    SetChrChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#000F修女，你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_09E4')
    def lambda_09E4():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_09E4)

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
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 5)
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)
    Sleep(500)

    @scena.Lambda('lambda_0D6D')
    def lambda_0D6D():
        ChrWalkTo(0x00FE, 15570, 0, -49480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D6D)

    Sleep(100)

    @scena.Lambda('lambda_0D8D')
    def lambda_0D8D():
        ChrWalkTo(0x00FE, 14280, 0, -48510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0D8D)

    SetChrDirection(0x0008, 45, 400)

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

    @scena.Lambda('lambda_0DD9')
    def lambda_0DD9():
        ChrMoveTo(0x00FE, 14210, 0, -50140, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0DD9)

    SetChrPos(0x0009, 19840, 0, -40400, 0)
    SetChrPos(0x000A, 21100, 0, -41220, 0)
    SetChrPos(0x000B, 21440, 0, -39410, 0)
    SetChrPos(0x000C, 21420, 0, -38390, 0)
    SetChrPos(0x000D, 23130, 0, -39910, 0)
    SetChrPos(0x000E, 21460, 0, -36780, 0)
    SetChrPos(0x000F, 23510, 0, -37150, 0)
    SetChrPos(0x0010, 24560, 0, -39000, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)

    @scena.Lambda('lambda_0EA4')
    def lambda_0EA4():
        ChrWalkTo(0x00FE, 15280, 0, -45500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0EA4)

    @scena.Lambda('lambda_0EBF')
    def lambda_0EBF():
        ChrWalkTo(0x00FE, 17370, 0, -46170, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0EBF)

    @scena.Lambda('lambda_0EDA')
    def lambda_0EDA():
        ChrWalkTo(0x00FE, 16610, 0, -44960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0EDA)

    @scena.Lambda('lambda_0EF5')
    def lambda_0EF5():
        ChrWalkTo(0x00FE, 16300, 0, -43340, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0EF5)

    @scena.Lambda('lambda_0F10')
    def lambda_0F10():
        ChrWalkTo(0x00FE, 18970, 0, -44750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0F10)

    @scena.Lambda('lambda_0F2B')
    def lambda_0F2B():
        ChrWalkTo(0x00FE, 17210, 0, -42380, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0F2B)

    @scena.Lambda('lambda_0F46')
    def lambda_0F46():
        ChrWalkTo(0x00FE, 19190, 0, -42290, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0F46)

    @scena.Lambda('lambda_0F61')
    def lambda_0F61():
        ChrWalkTo(0x00FE, 19060, 0, -43530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0F61)

    Sleep(300)

    @scena.Lambda('lambda_0F81')
    def lambda_0F81():
        CameraMove(19250, 0, -43570, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F81)

    @scena.Lambda('lambda_0F99')
    def lambda_0F99():
        OP_6C(0, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F99)

    Sleep(1500)

    @scena.Lambda('lambda_0FAE')
    def lambda_0FAE():
        CameraMove(17110, 0, -45970, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FAE)

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
    ClearChrFlags(0x0108, 0x0080)
    ChrWalkTo(0x0108, 21130, 0, -40520, 12000, 0x00)

    @scena.Lambda('lambda_108A')
    def lambda_108A():
        CameraMove(17970, 0, -45090, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_108A)

    SetChrChipByIndex(0x0108, 8)
    SetChrFlags(0x0108, 0x0020)
    SetChrFlags(0x0108, 0x1000)

    @scena.Lambda('lambda_10B1')
    def lambda_10B1():
        OP_99(0x00FE, 0x00, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_10B1)

    ChrWalkTo(0x0108, 19670, 0, -41930, 12000, 0x00)
    PlayEffect(0x08, 0xFF, 0x00FF, 19660, 0, -41900, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_110A')
    def lambda_110A():
        ChrMoveTo(0x00FE, 17370, 0, -43990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_110A)

    @scena.Lambda('lambda_1125')
    def lambda_1125():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1125)

    @scena.Lambda('lambda_1137')
    def lambda_1137():
        OP_99(0x00FE, 0x04, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1137)

    ChrJumpTo(0x0108, 20380, 0, -41250, 1000, 6000)

    ChrTalk(
        0x0108,
        (
            '#0081040001V哦，看起来你们遇到麻烦了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1185')
    def lambda_1185():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1185)

    @scena.Lambda('lambda_1193')
    def lambda_1193():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1193)

    @scena.Lambda('lambda_11A1')
    def lambda_11A1():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_11A1)

    @scena.Lambda('lambda_11AF')
    def lambda_11AF():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_11AF)

    @scena.Lambda('lambda_11BD')
    def lambda_11BD():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_11BD)

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

    @scena.Lambda('lambda_129B')
    def lambda_129B():
        OP_99(0x00FE, 0x00, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_129B)

    @scena.Lambda('lambda_12AB')
    def lambda_12AB():
        ChrWalkTo(0x00FE, 16750, 0, -47000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_12AB)

    @scena.Lambda('lambda_12C6')
    def lambda_12C6():
        ChrWalkTo(0x00FE, 14860, 0, -46770, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_12C6)

    ChrWalkTo(0x0108, 18730, 0, -42670, 5000, 0x00)
    Battle(0x000003A4, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1308'),
        (-1, 'loc_130B'),
    )

    def _loc_1308(): pass

    label('loc_1308')

    OP_B4(0x00)

    Return()

    def _loc_130B(): pass

    label('loc_130B')

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
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrPos(0x0101, 16770, 0, -47500, 45)
    SetChrPos(0x0102, 15050, 0, -45990, 45)
    SetChrPos(0x0108, 17690, 0, -44440, 225)
    SetChrPos(0x0008, 14650, 0, -48360, 45)
    CameraMove(15920, 0, -45970, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0108, 0x1000)

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

    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    ClearChrFlags(0x0108, 0x0020)
    ClearChrFlags(0x0108, 0x1000)

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

    @scena.Lambda('lambda_1600')
    def lambda_1600():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1600')

    DispatchAsync2(0x0108, 0x0001, lambda_1600)

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

    @scena.Lambda('lambda_17AD')
    def lambda_17AD():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_17AD')

    DispatchAsync2(0x0108, 0x0001, lambda_17AD)

    @scena.Lambda('lambda_17BE')
    def lambda_17BE():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_17BE')

    DispatchAsync2(0x0102, 0x0001, lambda_17BE)

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
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0011, 22440, 0, -38100, 0)
    SetChrPos(0x0012, 21240, 0, -37930, 0)

    ChrTalk(
        0x0011,
        (
            '你们在干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18E1')
    def lambda_18E1():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_18E1')

    DispatchAsync2(0x0108, 0x0002, lambda_18E1)

    @scena.Lambda('lambda_18F2')
    def lambda_18F2():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_18F2')

    DispatchAsync2(0x0101, 0x0002, lambda_18F2)

    @scena.Lambda('lambda_1903')
    def lambda_1903():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_1903')

    DispatchAsync2(0x0102, 0x0002, lambda_1903)

    @scena.Lambda('lambda_1914')
    def lambda_1914():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_1914')

    DispatchAsync2(0x0008, 0x0002, lambda_1914)

    @scena.Lambda('lambda_1925')
    def lambda_1925():
        ChrWalkTo(0x00FE, 18650, 0, -44020, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1925)

    @scena.Lambda('lambda_1940')
    def lambda_1940():
        ChrWalkTo(0x00FE, 17460, 0, -43540, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1940)

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

    @scena.Lambda('lambda_1A5F')
    def lambda_1A5F():
        ChrWalkTo(0x00FE, 17150, 0, -46640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A5F)

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

    @scena.Lambda('lambda_1EBA')
    def lambda_1EBA():
        ChrWalkTo(0x00FE, 23730, 0, -36620, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1EBA)

    Sleep(100)

    @scena.Lambda('lambda_1EDA')
    def lambda_1EDA():
        ChrWalkTo(0x00FE, 23730, 0, -36620, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1EDA)

    Sleep(200)

    @scena.Lambda('lambda_1EFA')
    def lambda_1EFA():
        ChrWalkTo(0x00FE, 23730, 0, -36620, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1EFA)

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

    @scena.Lambda('lambda_1FEB')
    def lambda_1FEB():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1FEB)

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

    def _loc_2267(): pass

    label('loc_2267')

    Return()

# id: 0x0003 offset: 0x2268
@scena.Code('func_03_2268')
def func_03_2268():
    EventBegin(0x00)
    SetChrPos(0x0101, 11690, 0, -52560, 225)
    SetChrPos(0x0102, 11000, 0, -51680, 225)
    SetChrPos(0x0108, 10930, 0, -50240, 196)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0013, 14410, 0, -53900, 257)
    SetChrPos(0x0014, 14820, 0, -52280, 244)
    SetChrPos(0x0015, 13050, 0, -51640, 207)
    SetChrPos(0x0016, 13090, 0, -50260, 213)
    CameraMove(11570, 250, -53400, 0)
    OP_67(0, 7270, -10000, 0)
    CameraSetDistance(2710, 0)
    OP_6C(225000, 0)
    OP_6E(395, 0)
    FadeIn(3000, 0)

    @scena.Lambda('lambda_2341')
    def lambda_2341():
        OP_6C(249000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2341)

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
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x0017, 17080, 0, -45130, 225)
    SetChrPos(0x0018, 17100, 0, -43830, 225)
    SetChrPos(0x0019, 18380, 0, -45010, 225)
    SetChrPos(0x001A, 17740, 0, -42700, 225)
    SetChrPos(0x001B, 18600, 0, -43670, 225)
    SetChrPos(0x001C, 19480, 0, -44620, 225)
    SetChrPos(0x001D, 18580, 0, -41840, 225)
    SetChrPos(0x001E, 19520, 0, -42690, 225)
    SetChrPos(0x001F, 20400, 0, -43690, 225)

    @scena.Lambda('lambda_24BB')
    def lambda_24BB():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_24BB)

    @scena.Lambda('lambda_24D6')
    def lambda_24D6():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_24D6)

    @scena.Lambda('lambda_24F1')
    def lambda_24F1():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_24F1)

    @scena.Lambda('lambda_250C')
    def lambda_250C():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_250C)

    @scena.Lambda('lambda_2527')
    def lambda_2527():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_2527)

    @scena.Lambda('lambda_2542')
    def lambda_2542():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_2542)

    @scena.Lambda('lambda_255D')
    def lambda_255D():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_255D)

    @scena.Lambda('lambda_2578')
    def lambda_2578():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_2578)

    @scena.Lambda('lambda_2593')
    def lambda_2593():
        ChrMoveToRelative(0x00FE, 2000, 0, 4000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_2593)

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

    @scena.Lambda('lambda_2601')
    def lambda_2601():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2601)

    @scena.Lambda('lambda_260F')
    def lambda_260F():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_260F)

    @scena.Lambda('lambda_261D')
    def lambda_261D():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_261D)

    @scena.Lambda('lambda_262B')
    def lambda_262B():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_262B)

    @scena.Lambda('lambda_2639')
    def lambda_2639():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_2639)

    @scena.Lambda('lambda_2647')
    def lambda_2647():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_2647)

    @scena.Lambda('lambda_2655')
    def lambda_2655():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_2655)

    @scena.Lambda('lambda_2663')
    def lambda_2663():
        OP_6C(335000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2663)

    @scena.Lambda('lambda_2673')
    def lambda_2673():
        OP_6E(332, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2673)

    @scena.Lambda('lambda_2683')
    def lambda_2683():
        CameraMove(13880, 0, -49890, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2683)

    @scena.Lambda('lambda_269B')
    def lambda_269B():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_269B)

    Sleep(100)

    @scena.Lambda('lambda_26BB')
    def lambda_26BB():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_26BB)

    @scena.Lambda('lambda_26D6')
    def lambda_26D6():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_26D6)

    Sleep(100)

    @scena.Lambda('lambda_26F6')
    def lambda_26F6():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_26F6)

    @scena.Lambda('lambda_2711')
    def lambda_2711():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_2711)

    @scena.Lambda('lambda_272C')
    def lambda_272C():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_272C)

    Sleep(100)

    @scena.Lambda('lambda_274C')
    def lambda_274C():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_274C)

    @scena.Lambda('lambda_2767')
    def lambda_2767():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_2767)

    @scena.Lambda('lambda_2782')
    def lambda_2782():
        ChrMoveToRelative(0x00FE, -4000, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_2782)

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

    @scena.Lambda('lambda_28A7')
    def lambda_28A7():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_28A7)

    @scena.Lambda('lambda_28B5')
    def lambda_28B5():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_28B5)

    @scena.Lambda('lambda_28C3')
    def lambda_28C3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_28C3)

    @scena.Lambda('lambda_28D1')
    def lambda_28D1():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_28D1)

    @scena.Lambda('lambda_28DF')
    def lambda_28DF():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_28DF)

    @scena.Lambda('lambda_28ED')
    def lambda_28ED():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_28ED)

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
    SetChrDirection(0x0101, 225, 400)

    @scena.Lambda('lambda_2B42')
    def lambda_2B42():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2B42')

    DispatchAsync2(0x0102, 0x0001, lambda_2B42)

    @scena.Lambda('lambda_2B53')
    def lambda_2B53():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2B53')

    DispatchAsync2(0x0108, 0x0001, lambda_2B53)

    @scena.Lambda('lambda_2B64')
    def lambda_2B64():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2B64')

    DispatchAsync2(0x0013, 0x0001, lambda_2B64)

    @scena.Lambda('lambda_2B75')
    def lambda_2B75():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2B75')

    DispatchAsync2(0x0014, 0x0001, lambda_2B75)

    @scena.Lambda('lambda_2B86')
    def lambda_2B86():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2B86')

    DispatchAsync2(0x0015, 0x0001, lambda_2B86)

    @scena.Lambda('lambda_2B97')
    def lambda_2B97():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2B97')

    DispatchAsync2(0x0016, 0x0001, lambda_2B97)

    @scena.Lambda('lambda_2BA8')
    def lambda_2BA8():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2BA8)

    ChrWalkTo(0x0101, 10610, 480, -53440, 1500, 0x00)
    OP_20(0x000007D0)
    SetChrDirection(0x0101, 45, 400)
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
    SetMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4113._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x2C66
@scena.Code('func_04_2C66')
def func_04_2C66():
    EventBegin(0x00)
    CameraMove(-26280, 0, -4400, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(234, 0)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    SetChrChipByIndex(0x0018, 19)
    SetChrChipByIndex(0x0019, 19)
    SetChrChipByIndex(0x001A, 19)
    SetChrChipByIndex(0x001B, 19)
    SetChrSubChip(0x0018, 2)
    SetChrSubChip(0x0019, 2)
    SetChrSubChip(0x001A, 2)
    SetChrSubChip(0x001B, 2)
    SetChrPos(0x0018, -25890, 0, -4510, 180)
    SetChrPos(0x0019, -27370, 0, -4510, 180)
    SetChrPos(0x001A, -27240, 0, -2700, 180)
    SetChrPos(0x001B, -25950, 0, -2920, 180)
    SetChrPos(0x0108, -26570, 0, -6220, 0)
    SetChrPos(0x0102, -28030, 0, -6250, 45)
    SetChrPos(0x0101, -25360, 0, -6190, 315)
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

    @scena.Lambda('lambda_2E2F')
    def lambda_2E2F():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_2E2F')

    DispatchAsync2(0x0101, 0x0001, lambda_2E2F)

    @scena.Lambda('lambda_2E40')
    def lambda_2E40():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_2E40')

    DispatchAsync2(0x0102, 0x0001, lambda_2E40)

    @scena.Lambda('lambda_2E51')
    def lambda_2E51():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_2E51')

    DispatchAsync2(0x0108, 0x0001, lambda_2E51)

    SetChrChipByIndex(0x001B, 18)

    @scena.Lambda('lambda_2E67')
    def lambda_2E67():
        SetChrDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_2E67)

    @scena.Lambda('lambda_2E75')
    def lambda_2E75():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_2E75)

    Sleep(200)

    SetChrChipByIndex(0x001A, 18)

    @scena.Lambda('lambda_2E9A')
    def lambda_2E9A():
        SetChrDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_2E9A)

    @scena.Lambda('lambda_2EA8')
    def lambda_2EA8():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_2EA8)

    Sleep(200)

    SetChrChipByIndex(0x0018, 18)

    @scena.Lambda('lambda_2ECD')
    def lambda_2ECD():
        SetChrDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_2ECD)

    @scena.Lambda('lambda_2EDB')
    def lambda_2EDB():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_2EDB)

    Sleep(200)

    SetChrChipByIndex(0x0019, 18)

    @scena.Lambda('lambda_2F00')
    def lambda_2F00():
        SetChrDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_2F00)

    @scena.Lambda('lambda_2F0E')
    def lambda_2F0E():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_2F0E)

    Sleep(2000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetScenaFlags(ScenaFlag(0x00CA, 1, 0x651))
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x2F4E
@scena.Code('func_05_2F4E')
def func_05_2F4E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_30A8',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FBD',
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

    Jump('loc_308D')

    def _loc_2FBD(): pass

    label('loc_2FBD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_301A',
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

    Jump('loc_308D')

    def _loc_301A(): pass

    label('loc_301A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_308D',
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

    def _loc_308D(): pass

    label('loc_308D')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_30A8(): pass

    label('loc_30A8')

    Return()

# id: 0x0006 offset: 0x30A9
@scena.Code('func_06_30A9')
def func_06_30A9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3203',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3118',
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

    Jump('loc_31E8')

    def _loc_3118(): pass

    label('loc_3118')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3175',
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

    Jump('loc_31E8')

    def _loc_3175(): pass

    label('loc_3175')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31E8',
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

    def _loc_31E8(): pass

    label('loc_31E8')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3203(): pass

    label('loc_3203')

    Return()

# id: 0x0007 offset: 0x3204
@scena.Code('func_07_3204')
def func_07_3204():
    FadeOut(300, 0, 100)
    SetChrName('')
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
