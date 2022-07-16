import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1215_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1215   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '亚鲁瓦教授'),
    TXT(0x02, '魔兽'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '宝箱魔兽'),
    TXT(0x05, '宝箱魔兽'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1215.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1196
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
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT09/CH10410._CH', 'ED6_DT09/CH10410P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT09/CH10411._CH', 'ED6_DT09/CH10411P._CP'),
        ('ED6_DT09/CH10440._CH', 'ED6_DT09/CH10440P._CP'),
        ('ED6_DT09/CH10441._CH', 'ED6_DT09/CH10441P._CP'),
        ('ED6_DT09/CH10410._CH', 'ED6_DT09/CH10410P._CP'),
        ('ED6_DT09/CH10411._CH', 'ED6_DT09/CH10411P._CP'),
        ('ED6_DT09/CH10420._CH', 'ED6_DT09/CH10420P._CP'),
        ('ED6_DT09/CH10421._CH', 'ED6_DT09/CH10421P._CP'),
        ('ED6_DT09/CH10430._CH', 'ED6_DT09/CH10430P._CP'),
        ('ED6_DT09/CH10431._CH', 'ED6_DT09/CH10431P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 380,
            y                   = 3530,
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
            x                   = -4280,
            z                   = 10000,
            y                   = 4280,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 4190,
            z                   = 10000,
            y                   = 3730,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C5,
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
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
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
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 20670,
            z           = 0,
            y           = -5460,
            word_0C     = 0x0097,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0094,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 19250,
            z           = 0,
            y           = 8320,
            word_0C     = 0x0149,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0097,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 8520,
            z           = 0,
            y           = 19510,
            word_0C     = 0x010F,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0091,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17540,
            z           = 0,
            y           = 12440,
            word_0C     = 0x00DF,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0096,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x22A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -3030,
            y           = -1000,
            z           = 14100,
            range       = 2970,
            dword_10    = 0x000007D0,
            dword_14    = 0x00003DAE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x24A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 11840,
            triggerZ            = 0,
            triggerY            = 40,
            triggerRange        = 1000,
            actorX              = 12620,
            actorZ              = 1500,
            actorY              = 60,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -11810,
            triggerZ            = 0,
            triggerY            = -40,
            triggerRange        = 1000,
            actorX              = -12660,
            actorZ              = 1500,
            actorY              = 90,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x292
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x293
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0070, 0, 0x380)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A5',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2AC')

    def _loc_2A5(): pass

    label('loc_2A5')

    OP_6F(0x0000, 60)

    def _loc_2AC(): pass

    label('loc_2AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0070, 1, 0x381)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BE',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2C5')

    def _loc_2BE(): pass

    label('loc_2BE')

    OP_6F(0x0001, 60)

    def _loc_2C5(): pass

    label('loc_2C5')

    Return()

# id: 0x0002 offset: 0x2C6
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2DB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2DB(): pass

    label('loc_2DB')

    Return()

# id: 0x0003 offset: 0x2DC
@scena.Code('func_03_2DC')
def func_03_2DC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            (Expr.Eval, "OP_29(0x000F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x000F, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CCF',
    )

    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010151096V#004F啊！那个人是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    Fade(1000)
    OP_6C(225000, 0)

    @scena.Lambda('lambda_0359')
    def lambda_0359():
        CameraMove(40, 380, 3090, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0359)

    OP_0D()
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrMoveToRelativeAsync(0x0008, 1000, 0, -600, 1000, 0x00)
    Sleep(200)

    OP_63(0x0008)
    ChrMoveToRelativeAsync(0x0008, -1000, 0, 600, 1000, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrMoveToRelativeAsync(0x0008, -500, 0, -300, 1000, 0x00)
    Sleep(200)

    WaitForThreadExit(0x0008, 0x0001)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x0009, 0x01, 0x00, 0x0004)
    CreateThread(0x000A, 0x01, 0x00, 0x0005)
    OP_63(0x0008)
    ChrMoveToRelativeAsync(0x0008, 500, 0, 300, 1000, 0x00)
    Sleep(400)

    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0008, 0, 0, 0, 800, 12000)
    SetChrDirection(0x0008, 315, 200)
    SetChrDirection(0x0008, 45, 200)
    SetChrDirection(0x0008, 0, 100)
    Sleep(400)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0150151097V#131F哎呀，哎呀呀！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150151098V救、救命啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_04DB')
    def lambda_04DB():
        ChrWalkTo(0x0009, -920, 0, 4660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_04DB)

    @scena.Lambda('lambda_04F6')
    def lambda_04F6():
        ChrWalkTo(0x000A, 1270, 0, 4710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_04F6)

    ChrMoveToRelativeAsync(0x0008, 0, 0, -200, 1000, 0x00)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)
    SetChrFlags(0x0103, 0x1000)
    SetChrChipByIndex(0x0101, 2)
    SetChrChipByIndex(0x0102, 3)
    SetChrChipByIndex(0x0103, 4)
    SetChrPos(0x0101, -60, 0, 11030, 182)
    SetChrPos(0x0102, 670, 0, 11700, 180)
    SetChrPos(0x0103, -810, 0, 12320, 180)

    @scena.Lambda('lambda_0576')
    def lambda_0576():
        ChrMoveToRelative(0x0101, 0, 0, -5000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0576)

    @scena.Lambda('lambda_0591')
    def lambda_0591():
        ChrMoveToRelative(0x0102, 0, 0, -5000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0591)

    @scena.Lambda('lambda_05AC')
    def lambda_05AC():
        ChrMoveToRelative(0x0103, 0, 0, -5000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_05AC)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000003EF, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_5EF'),
        (-1, 'loc_5F4'),
    )

    def _loc_5EF(): pass

    label('loc_5EF')

    OP_B4(0x00)

    Jump('loc_5F4')

    def _loc_5F4(): pass

    label('loc_5F4')

    EventBegin(0x00)
    FormationAddMember(0x0D, 0x03)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)
    ClearChrFlags(0x0103, 0x1000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrPos(0x0101, 0, 0, 5400, 180)
    SetChrPos(0x0102, -910, 0, 6810, 180)
    SetChrPos(0x0103, 800, 0, 6800, 180)
    SetChrPos(0x010E, 0, 380, 3420, 0)
    CameraMove(0, 0, 4440, 0)

    @scena.Lambda('lambda_0681')
    def lambda_0681():
        OP_6C(315000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0681)

    @scena.Lambda('lambda_0691')
    def lambda_0691():
        CameraMove(-720, 0, 5910, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0691)

    @scena.Lambda('lambda_06A9')
    def lambda_06A9():
        CameraSetDistance(2600, 3000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_06A9)

    OP_0D()
    WaitForThreadExit(0x0000, 0x0001)
    Sleep(400)

    ChrTalk(
        0x010E,
        (
            '#0150151099V#131F呼呼……\n',
            '得、得救了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151100V#006F#1P我以为是谁呢，\n',
            '这不是亚鲁瓦教授吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151101V真是的～我以为是空贼团，\n',
            '白紧张了一番呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150151102V#130F哈、哈哈哈，\n',
            '很久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151103V#023F你们认识吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151104V#000F#1P嗯，这位先生是\n',
            '是喜欢调查塔什么的考古学者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151105V我们在洛连特为记者做护卫的时候，\n',
            '曾经在翡翠之塔见过他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150151106V#130F哈哈哈，\n',
            '你们又救了我一次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 180, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151107V#022F我们刚才听到了说话的声音，\n',
            '还有其他人在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150151108V#130F哎呀，你们听到了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150151109V让你们见笑了，\n',
            '那是我在进行研究时的坏习惯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150151110V如果嘴里不说些什么，\n',
            '就无论如何也没办法进行思考。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151111V#506F#1P什么嘛，原来是自言自语。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151112V#020F是这样啊，我明白了。\n',
            '这个问题我们待会儿再讨论吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151113V在魔兽再次袭击我们之前，\n',
            '先从塔里出去比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150151114V#131F……啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150151115V现在就出去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151116V#023F有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150151117V#131F可、可是我的调查还没有完呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151118V#020F哦，这样啊。\n',
            '那就随你高兴，继续调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0103, 0, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151119V#026F艾丝蒂尔、约修亚，\n',
            '我们回去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151120V学者先生看来是想自己一个人回去。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150151121V#131F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B0D')
    def lambda_0B0D():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B0D)

    @scena.Lambda('lambda_0B1B')
    def lambda_0B1B():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B1B)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010151122V#509F#1P（哇啊，好可怕～～～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151123V#018F（……这根本就是胁迫嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x010E,
        (
            '#0150151124V#131F对、对不起！\n',
            '我决定现在就从塔里出去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0103, 180, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151125V#027F哼哼，乖乖听话的男人才是最棒的哦㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151126V好了，艾丝蒂尔、约修亚，\n',
            '快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151127V#007F#1P知道～了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151128V#017F……哎呀哎呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C77')
    def lambda_0C77():
        OP_92(0x0101, 0x0103, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C77)

    @scena.Lambda('lambda_0C8C')
    def lambda_0C8C():
        OP_92(0x0102, 0x0103, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0C8C)

    @scena.Lambda('lambda_0CA1')
    def lambda_0CA1():
        OP_92(0x010E, 0x0103, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_0CA1)

    OP_69(0x0103, 1400)
    WaitForThreadExit(0x010E, 0x0001)
    OP_28(0x000F, 0x04, 0x08)
    OP_28(0x000F, 0x01, 0x0004)
    OP_28(0x000F, 0x01, 0x0008)
    EventEnd(0x00)

    def _loc_CCF(): pass

    label('loc_CCF')

    Return()

# id: 0x0004 offset: 0xCD0
@scena.Code('func_04_CD0')
def func_04_CD0():
    PlaySE(189, 0x00, 0x64)
    ChrWalkTo(0x0009, -4280, 0, 4280, 18000, 0x00)
    PlaySE(530, 0x00, 0x64)
    ChrJumpTo(0x0009, -4430, 0, 4770, 2000, 2000)
    PlaySE(530, 0x00, 0x64)
    ChrJumpTo(0x0009, -2180, 0, 6510, 1400, 3000)
    SetChrChipByIndex(0x0009, 1)
    SetChrFlags(0x0009, 0x0001)
    ChrTurnDirection(0x00FE, 0x0008, 400)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0005 offset: 0xD3A
@scena.Code('func_05_D3A')
def func_05_D3A():
    Sleep(600)

    ChrWalkTo(0x000A, 4190, 0, 3730, 18000, 0x00)
    PlaySE(530, 0x00, 0x64)
    ChrJumpTo(0x000A, 3610, 0, 4780, 2500, 2500)
    PlaySE(530, 0x00, 0x64)
    ChrJumpTo(0x000A, 2360, 0, 6510, 1400, 3000)
    SetChrChipByIndex(0x000A, 1)
    SetChrFlags(0x000A, 0x0001)
    ChrTurnDirection(0x00FE, 0x0008, 400)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0006 offset: 0xDA4
@scena.Code('func_06_DA4')
def func_06_DA4():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0070, 0, 0x380)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F4E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0070, 2, 0x382)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E80',
    )

    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    SetChrPos(0x000B, 12620, 3000, 60, 320)
    ChrTurnDirection(0x000B, 0x0000, 0)

    @scena.Lambda('lambda_0DF3')
    def lambda_0DF3():
        ChrMoveTo(0x00FE, 12620, 1500, 60, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0DF3)

    @scena.Lambda('lambda_0E0E')
    def lambda_0E0E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0E0E)

    ClearChrFlags(0x000B, 0x0080)

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
    Battle(0x000000A0, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x000B, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_E5B'),
        (0x00000002, 'loc_E6D'),
        (0x00000001, 'loc_E7D'),
        (-1, 'loc_E80'),
    )

    def _loc_E5B(): pass

    label('loc_E5B')

    SetScenaFlags(ScenaFlag(0x0070, 2, 0x382))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_E80')

    def _loc_E6D(): pass

    label('loc_E6D')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_E7D(): pass

    label('loc_E7D')

    OP_B4(0x00)

    Return()

    def _loc_E80(): pass

    label('loc_E80')

    If(
        (
            (Expr.Eval, "AddItem(0x00F8, 1)"),
            Expr.Return,
        ),
        'loc_ED6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '锁片薄衣',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0070, 0, 0x380))

    Jump('loc_F4B')

    def _loc_ED6(): pass

    label('loc_ED6')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '锁片薄衣',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '锁片薄衣',
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

    def _loc_F4B(): pass

    label('loc_F4B')

    Jump('loc_F84')

    def _loc_F4E(): pass

    label('loc_F4E')

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
    WaitEffect(0x0F, 0x0D)
    def _loc_F84(): pass

    label('loc_F84')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xF92
@scena.Code('func_07_F92')
def func_07_F92():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0070, 1, 0x381)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1142',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0070, 3, 0x383)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_106E',
    )

    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 0)
    SetChrPos(0x000C, -12660, 3000, 90, 320)
    ChrTurnDirection(0x000C, 0x0000, 0)

    @scena.Lambda('lambda_0FE1')
    def lambda_0FE1():
        ChrMoveTo(0x00FE, -12660, 1500, 90, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0FE1)

    @scena.Lambda('lambda_0FFC')
    def lambda_0FFC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0FFC)

    ClearChrFlags(0x000C, 0x0080)

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
    Battle(0x0000009F, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x000C, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1049'),
        (0x00000002, 'loc_105B'),
        (0x00000001, 'loc_106B'),
        (-1, 'loc_106E'),
    )

    def _loc_1049(): pass

    label('loc_1049')

    SetScenaFlags(ScenaFlag(0x0070, 3, 0x383))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_106E')

    def _loc_105B(): pass

    label('loc_105B')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_106B(): pass

    label('loc_106B')

    OP_B4(0x00)

    Return()

    def _loc_106E(): pass

    label('loc_106E')

    If(
        (
            (Expr.Eval, "AddItem(0x0144, 1)"),
            Expr.Return,
        ),
        'loc_10C6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '翠耀石护符',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0070, 1, 0x381))

    Jump('loc_113F')

    def _loc_10C6(): pass

    label('loc_10C6')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '翠耀石护符',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '翠耀石护符',
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

    def _loc_113F(): pass

    label('loc_113F')

    Jump('loc_1178')

    def _loc_1142(): pass

    label('loc_1142')

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
    WaitEffect(0x0F, 0x0E)
    def _loc_1178(): pass

    label('loc_1178')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
