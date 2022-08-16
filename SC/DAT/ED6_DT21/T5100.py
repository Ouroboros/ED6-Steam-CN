import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T5100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T5100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'T5100.x'
    header.mapIndex       = 1
    header.bgm            = 25
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
        ('ED6_DT27/CH03090._CH', 'ED6_DT27/CH03090P._CP'),
        ('ED6_DT27/CH03900._CH', 'ED6_DT27/CH03900P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH04002._CH', 'ED6_DT27/CH04002P._CP'),
        ('ED6_DT27/CH04008._CH', 'ED6_DT27/CH04008P._CP'),
        ('ED6_DT27/CH04009._CH', 'ED6_DT27/CH04009P._CP'),
        ('ED6_DT27/CH0400B._CH', 'ED6_DT27/CH0400BP._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT07/CH00422._CH', 'ED6_DT07/CH00422P._CP'),
        ('ED6_DT07/CH00423._CH', 'ED6_DT07/CH00423P._CP'),
        ('ED6_DT07/CH00424._CH', 'ED6_DT07/CH00424P._CP'),
        ('ED6_DT07/CH00425._CH', 'ED6_DT07/CH00425P._CP'),
        ('ED6_DT07/CH00426._CH', 'ED6_DT07/CH00426P._CP'),
        ('ED6_DT27/CH04007._CH', 'ED6_DT27/CH04007P._CP'),
        ('ED6_DT27/CH0400A._CH', 'ED6_DT27/CH0400AP._CP'),
        ('ED6_DT27/CH0400C._CH', 'ED6_DT27/CH0400CP._CP'),
        ('ED6_DT27/CH03000._CH', 'ED6_DT27/CH03000P._CP'),
        ('ED6_DT27/CH03001._CH', 'ED6_DT27/CH03001P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
    ]

# id: 0x10001 offset: 0x15A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '亚妮拉丝',
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
            name                = '菲莉斯管理员',
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
            name                = '克鲁茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '艾丝蒂尔',
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
    )

# id: 0x10002 offset: 0x1DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1DA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -4320,
            y           = 0,
            z           = -36940,
            range       = 3430,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF7338,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
        ScenaEventData(
            x           = -6800,
            y           = -200,
            z           = -51800,
            range       = 700,
            dword_10    = 0x00001CE8,
            dword_14    = 0xFFFF52F4,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
    )

# id: 0x10004 offset: 0x21A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -3550,
            triggerZ            = 0,
            triggerY            = -3000,
            triggerRange        = 800,
            actorX              = -4250,
            actorZ              = 1000,
            actorY              = -3000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x23E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 6, 0x1006)),
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_260',
    )

    ChrSetPos(0x000A, -2780, 0, -30790, 0)
    ChrClearFlags(0x000A, 0x0080)

    def _loc_260(): pass

    label('loc_260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_275',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_04_601)

    def _loc_275(): pass

    label('loc_275')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 2, 0x1012)),
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 3, 0x101B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28E',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0F_3612)

    def _loc_28E(): pass

    label('loc_28E')

    Return()

# id: 0x0001 offset: 0x28F
@scena.Code('func_01_28F')
def func_01_28F():
    OP_16(0x02, 4000, -126000, -138000, 2293871)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Return,
        ),
        'loc_2B6',
    )

    ExecExpressionWithVar(
        0x3A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(451, 0x00, 0x64)

    def _loc_2B6(): pass

    label('loc_2B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_2C0',
    )

    OP_10(0x00, 0x00)

    def _loc_2C0(): pass

    label('loc_2C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 2, 0x1012)),
            Expr.Return,
        ),
        'loc_2D0',
    )

    OP_10(0x02, 0x00)
    OP_10(0x03, 0x01)

    Jump('loc_2D6')

    def _loc_2D0(): pass

    label('loc_2D0')

    OP_10(0x03, 0x00)
    OP_10(0x02, 0x01)

    def _loc_2D6(): pass

    label('loc_2D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 3, 0x101B)),
            Expr.Return,
        ),
        'loc_2EB',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2EB(): pass

    label('loc_2EB')

    Return()

# id: 0x0002 offset: 0x2EC
@scena.Code('func_02_2EC')
def func_02_2EC():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_31D'),
        (0x00000001, 'loc_329'),
        (0x00000002, 'loc_335'),
        (0x00000003, 'loc_341'),
        (0x00000004, 'loc_34D'),
        (0x00000005, 'loc_359'),
        (0x00000006, 'loc_365'),
        (-1, 'loc_371'),
    )

    def _loc_31D(): pass

    label('loc_31D')

    OP_99(0x00FE, 0x00, 0x07, 1450)

    Jump('loc_37D')

    def _loc_329(): pass

    label('loc_329')

    OP_99(0x00FE, 0x00, 0x07, 1550)

    Jump('loc_37D')

    def _loc_335(): pass

    label('loc_335')

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_37D')

    def _loc_341(): pass

    label('loc_341')

    OP_99(0x00FE, 0x00, 0x07, 1400)

    Jump('loc_37D')

    def _loc_34D(): pass

    label('loc_34D')

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_37D')

    def _loc_359(): pass

    label('loc_359')

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_37D')

    def _loc_365(): pass

    label('loc_365')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_37D')

    def _loc_371(): pass

    label('loc_371')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_37D')

    def _loc_37D(): pass

    label('loc_37D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_392',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_37D')

    def _loc_392(): pass

    label('loc_392')

    Return()

# id: 0x0003 offset: 0x393
@scena.Code('func_03_393')
def func_03_393():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 0, 0x1008)),
            Expr.Return,
        ),
        'loc_3A4',
    )

    Call(0, 0x000A)

    Jump('loc_5FD')

    def _loc_3A4(): pass

    label('loc_3A4')

    If(
        (
            (Expr.Eval, "OP_29(0x00C5, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_453',
    )

    ChrTalk(
        0x000A,
        (
            '#0330190780V#842F你们两个，食物准备得如何了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190781V长时间的作战行动中\n',
            '要是小看补给可会吃苦头的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190782V好好去向菲莉斯管理员\n',
            '请教一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

    def _loc_453(): pass

    label('loc_453')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 6, 0x1026)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_511',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0261, 0x00)"),
            (Expr.Eval, "OP_40(0x0258, 0x00)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x025E, 0x00)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x026D, 0x00)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x02C1, 0x00)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0273, 0x00)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x02C8, 0x00)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x026A, 0x00)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x02C1, 0x00)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_49A',
    )

    SetScenaFlags(ScenaFlag(0x0204, 6, 0x1026))

    Jump('loc_511')

    def _loc_49A(): pass

    label('loc_49A')

    ChrTalk(
        0x000A,
        (
            '#0330190783V#842F不合成新型\n',
            '结晶回路没问题吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190784V若不能使用回复系的魔法，\n',
            '参加演习是相当危险的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

    def _loc_511(): pass

    label('loc_511')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 0, 0x1008)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5FD',
    )

    If(
        (
            (Expr.Eval, "OP_B9(0x00, 0x006E)"),
            (Expr.Eval, "OP_B9(0x09, 0x006E)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_532',
    )

    SetScenaFlags(ScenaFlag(0x0201, 0, 0x1008))
    Call(0, 0x000B)

    Jump('loc_5FD')

    def _loc_532(): pass

    label('loc_532')

    ChrTalk(
        0x000A,
        (
            '#0330190785V#843F你们似乎合成了\n',
            '一些新型结晶回路啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190786V#842F但是，若不能使用回复系的魔法，\n',
            '参加演习是相当危险的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190787V用水之耀晶片合成结晶回路，\n',
            '然后镶嵌到导力器上就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

    def _loc_5FD(): pass

    label('loc_5FD')

    TalkEnd(0x000A)

    Return()

# id: 0x0004 offset: 0x601
@scena.Code('func_04_601')
def func_04_601():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_23(0x01C3)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    LoadEffect(0x00, 'Scraft\\sc000_00.eff')
    LoadEffect(0x01, 'Scraft\\sc000_10.eff')
    LoadEffect(0x02, 'Craft\\cr011_00.eff')
    LoadEffect(0x03, 'monster\\ms10005.eff')
    LoadEffect(0x04, 'map\\\\mp009_00.eff')
    CameraMove(7190, 0, 54070, 0)
    OP_67(0, 10560, -10000, 0)
    CameraSetDistance(5770, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetSubChip(0x000B, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 9)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '２个月后──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '塞姆里亚大陆中西部\n',
            '列曼自治州·峡谷地带──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '游击士协会\n',
            '卢·洛克尔训练场──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_DB()
    CreateThread(0x000A, 0x01, 0x00, func_06_21DF)

    @scena.Lambda('lambda_0772')
    def lambda_0772():
        CameraMove(4130, 0, 23930, 8000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_0772)

    OP_C8(0x0200, 0x0046, 'C_PLAC01._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)
    PlaySE(451, 0x00, 0x64)
    WaitForThreadExit(0x000A, 0x0001)
    PlayBGM(44)
    Fade(1000)
    CameraMove(4120, 0, 24030, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2960, 0)
    OP_6C(305000, 0)
    OP_6E(262, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrSetPos(0x000B, 510, 0, 22930, 90)
    ChrSetPos(0x0008, 7610, 0, 24760, 270)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x000B, 0x0020)

    @scena.Lambda('lambda_082B')
    def lambda_082B():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_082B)

    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_084D')
    def lambda_084D():
        CameraMove(200, 0, 23150, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_084D)

    @scena.Lambda('lambda_0865')
    def lambda_0865():
        CameraSetDistance(3200, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0865)

    @scena.Lambda('lambda_0875')
    def lambda_0875():
        OP_67(0, 6800, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0875)

    @scena.Lambda('lambda_088D')
    def lambda_088D():
        OP_6E(224, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_088D)

    ChrClearFlags(0x0008, 0x0020)
    ChrSetChipByIndex(0x0008, 10)

    @scena.Lambda('lambda_08A7')
    def lambda_08A7():
        ChrWalkTo(0x00FE, 2890, 0, 23700, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_08A7)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetChipByIndex(0x000B, 8)

    @scena.Lambda('lambda_08D6')
    def lambda_08D6():
        ChrMoveTo(0x00FE, 1970, 0, 23670, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_08D6)

    ChrSetSubChip(0x0008, 0)
    ChrSetSubChip(0x000B, 0)
    Sleep(100)

    ChrSetSubChip(0x0008, 1)
    ChrSetSubChip(0x000B, 1)
    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(200)

    ChrSetSubChip(0x0008, 0)
    Sleep(200)

    @scena.Lambda('lambda_0958')
    def lambda_0958():
        ChrMoveTo(0x00FE, 1460, 0, 23280, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0958)

    Sleep(50)

    @scena.Lambda('lambda_0978')
    def lambda_0978():
        ChrMoveTo(0x00FE, -270, 0, 22570, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0978)

    Sleep(50)

    ChrSetSubChip(0x0008, 1)
    ChrSetSubChip(0x000B, 0)
    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(200)

    ChrSetSubChip(0x0008, 0)
    Sleep(200)

    @scena.Lambda('lambda_09F0')
    def lambda_09F0():
        ChrMoveTo(0x00FE, 780, 0, 23090, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_09F0)

    @scena.Lambda('lambda_0A0B')
    def lambda_0A0B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0A0B')

    DispatchAsync2(0x000B, 0x0002, lambda_0A0B)

    @scena.Lambda('lambda_0A1C')
    def lambda_0A1C():
        ChrJumpTo(0x00FE, 2760, 0, 20500, 600, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A1C)

    @scena.Lambda('lambda_0A3A')
    def lambda_0A3A():
        CameraMove(4180, 0, 23500, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0A3A)

    @scena.Lambda('lambda_0A52')
    def lambda_0A52():
        OP_6C(206000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A52)

    ChrSetSubChip(0x0008, 0)
    Sleep(100)

    ChrSetSubChip(0x0008, 1)
    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0A80')
    def lambda_0A80():
        ChrJumpTo(0x00FE, 6330, 0, 23370, 600, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A80)

    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x64)
    TerminateThread(0x000B, 0x02)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_0AB1')
    def lambda_0AB1():
        CameraMove(1220, 0, 23560, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0AB1)

    ChrSetChipByIndex(0x000B, 5)
    ChrSetSubChip(0x000B, 5)

    @scena.Lambda('lambda_0AD3')
    def lambda_0AD3():
        ChrJumpTo(0x00FE, 2500, 0, 23260, 2200, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0AD3)

    @scena.Lambda('lambda_0AF1')
    def lambda_0AF1():
        OP_99(0x00FE, 0x05, 0x09, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0AF1)

    PlaySE(163, 0x00, 0x64)
    Sleep(200)

    ChrSetChipByIndex(0x0008, 9)

    @scena.Lambda('lambda_0B10')
    def lambda_0B10():
        ChrTurnDirection(0x00FE, 0x000B, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B10)

    WaitForThreadExit(0x000B, 0x0001)
    TerminateThread(0x000B, 0x02)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetSubChip(0x0008, 0)
    PlayEffect(0x04, 0xFF, 0x0008, 0, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_0B6B')
    def lambda_0B6B():
        ChrMoveTo(0x00FE, -1340, 0, 22880, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B6B)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_0B95')
    def lambda_0B95():
        CameraMove(2180, 0, 22700, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0B95)

    @scena.Lambda('lambda_0BAD')
    def lambda_0BAD():
        OP_6C(206000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BAD)

    @scena.Lambda('lambda_0BBD')
    def lambda_0BBD():
        OP_6E(250, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0BBD)

    ChrSetChipByIndex(0x000B, 8)
    ChrSetSubChip(0x000B, 0)

    @scena.Lambda('lambda_0BD7')
    def lambda_0BD7():
        ChrJumpTo(0x00FE, 6130, 0, 23700, 600, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0BD7)

    Sleep(200)

    ChrSetChipByIndex(0x0008, 9)
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(200)

    @scena.Lambda('lambda_0C1D')
    def lambda_0C1D():
        CameraMove(6330, 0, 23100, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0C1D)

    @scena.Lambda('lambda_0C35')
    def lambda_0C35():
        OP_67(0, 8100, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C35)

    ChrClearFlags(0x0008, 0x0020)
    ChrSetChipByIndex(0x0008, 10)

    @scena.Lambda('lambda_0C57')
    def lambda_0C57():
        ChrWalkTo(0x00FE, 3290, 0, 22900, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C57)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_0C7C')
    def lambda_0C7C():
        OP_6C(164000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C7C)

    @scena.Lambda('lambda_0C8C')
    def lambda_0C8C():
        ChrJumpTo(0x00FE, 6860, 0, 20650, 600, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C8C)

    @scena.Lambda('lambda_0CAA')
    def lambda_0CAA():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0CAA')

    DispatchAsync2(0x0008, 0x0002, lambda_0CAA)

    @scena.Lambda('lambda_0CBB')
    def lambda_0CBB():
        ChrSetDirection(0x00FE, 184, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0CBB)

    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x02)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0CDC')
    def lambda_0CDC():
        ChrJumpTo(0x00FE, 5320, 0, 26670, 2400, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CDC)

    ChrSetDirection(0x0008, 90, 800)
    ChrSetDirection(0x0008, 180, 800)
    ChrSetDirection(0x0008, 270, 800)
    ChrSetDirection(0x0008, 0, 800)
    ChrSetDirection(0x0008, 90, 800)
    ChrSetDirection(0x0008, 164, 800)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_0D33')
    def lambda_0D33():
        OP_6E(210, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D33)

    ChrSetChipByIndex(0x0008, 11)

    @scena.Lambda('lambda_0D48')
    def lambda_0D48():
        ChrMoveTo(0x00FE, 5980, 0, 24380, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D48)

    @scena.Lambda('lambda_0D63')
    def lambda_0D63():
        OP_99(0x00FE, 0x00, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0D63)

    ChrSetFlags(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 16)
    ChrSetSubChip(0x000B, 11)

    @scena.Lambda('lambda_0D82')
    def lambda_0D82():
        ChrMoveTo(0x00FE, 5580, 0, 22820, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0D82)

    @scena.Lambda('lambda_0D9D')
    def lambda_0D9D():
        OP_99(0x00FE, 0x0B, 0x0C, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0D9D)

    Sleep(100)

    PlaySE(132, 0x00, 0x64)
    Sleep(400)

    ChrSetFlags(0x000B, 0x0800)

    @scena.Lambda('lambda_0DC1')
    def lambda_0DC1():
        CameraMove(5340, 0, 24640, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0DC1)

    @scena.Lambda('lambda_0DD9')
    def lambda_0DD9():
        OP_67(0, 5980, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DD9)

    @scena.Lambda('lambda_0DF1')
    def lambda_0DF1():
        OP_6C(158000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DF1)

    @scena.Lambda('lambda_0E01')
    def lambda_0E01():
        OP_6E(258, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E01)

    ChrClearFlags(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 5)
    ChrTurnDirection(0x000B, 0x0008, 0)

    @scena.Lambda('lambda_0E22')
    def lambda_0E22():
        OP_99(0x00FE, 0x00, 0x09, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0E22)

    Sleep(200)

    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0008, 6)

    @scena.Lambda('lambda_0E41')
    def lambda_0E41():
        ChrJumpTo(0x00FE, 4310, 0, 27580, 600, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E41)

    @scena.Lambda('lambda_0E5F')
    def lambda_0E5F():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0E5F')

    DispatchAsync2(0x0008, 0x0002, lambda_0E5F)

    PlaySE(163, 0x00, 0x64)
    Sleep(100)

    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x02)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0008, 0)
    Sleep(500)

    ChrSetFlags(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 6)
    ChrSetSubChip(0x000B, 72)
    Sleep(100)

    @scena.Lambda('lambda_0EB0')
    def lambda_0EB0():
        CameraMove(4620, 0, 27120, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0EB0)

    @scena.Lambda('lambda_0EC8')
    def lambda_0EC8():
        OP_6C(182000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EC8)

    @scena.Lambda('lambda_0ED8')
    def lambda_0ED8():
        OP_6E(280, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0ED8)

    @scena.Lambda('lambda_0EE8')
    def lambda_0EE8():
        OP_67(0, 5340, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0EE8)

    ChrClearFlags(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetSubChip(0x000B, 2)

    @scena.Lambda('lambda_0F0F')
    def lambda_0F0F():
        ChrJumpTo(0x00FE, 4530, 0, 27410, 3000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0F0F)

    PlaySE(163, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_0F37')
    def lambda_0F37():
        OP_99(0x00FE, 0x02, 0x09, 2500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0F37)

    PlaySE(132, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0008, 6)
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_0F5B')
    def lambda_0F5B():
        ChrJumpTo(0x00FE, 4180, 2060, 32700, 2500, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F5B)

    PlaySE(163, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0F88')
    def lambda_0F88():
        ChrJumpTo(0x00FE, 7150, 0, 28330, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F88)

    @scena.Lambda('lambda_0FA6')
    def lambda_0FA6():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0FA6')

    DispatchAsync2(0x0008, 0x0002, lambda_0FA6)

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x02)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0FC5')
    def lambda_0FC5():
        CameraMove(4530, 0, 27250, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0FC5)

    @scena.Lambda('lambda_0FDD')
    def lambda_0FDD():
        OP_67(0, 6360, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FDD)

    @scena.Lambda('lambda_0FF5')
    def lambda_0FF5():
        OP_6E(256, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FF5)

    ChrSetChipByIndex(0x0008, 15)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_100F')
    def lambda_100F():
        ChrMoveTo(0x00FE, 5640, 0, 27930, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_100F)

    Sleep(100)

    ChrSetSubChip(0x0008, 1)
    PlaySE(132, 0x00, 0x64)
    ChrSetChipByIndex(0x000B, 8)
    ChrSetSubChip(0x000B, 0)
    ChrSetDirection(0x000B, 25, 0)

    @scena.Lambda('lambda_104A')
    def lambda_104A():
        ChrMoveTo(0x00FE, 3970, 0, 26820, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_104A)

    WaitForThreadExit(0x000B, 0x0001)
    Sleep(400)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_107E')
    def lambda_107E():
        CameraMove(3930, 0, 23850, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_107E)

    @scena.Lambda('lambda_1096')
    def lambda_1096():
        OP_6C(162000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1096)

    @scena.Lambda('lambda_10A6')
    def lambda_10A6():
        OP_67(0, 6360, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_10A6)

    @scena.Lambda('lambda_10BE')
    def lambda_10BE():
        OP_6E(280, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_10BE)

    @scena.Lambda('lambda_10CE')
    def lambda_10CE():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_10CE')

    DispatchAsync2(0x000B, 0x0002, lambda_10CE)

    @scena.Lambda('lambda_10DF')
    def lambda_10DF():
        ChrJumpTo(0x00FE, 920, 0, 25530, 400, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_10DF)

    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_110C')
    def lambda_110C():
        ChrJumpTo(0x00FE, 1720, 0, 22210, 400, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_110C)

    Sleep(100)

    ChrSetChipByIndex(0x0008, 9)

    @scena.Lambda('lambda_1134')
    def lambda_1134():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1134')

    DispatchAsync2(0x0008, 0x0002, lambda_1134)

    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x64)
    TerminateThread(0x000B, 0x02)
    TerminateThread(0x0008, 0x02)
    ChrSetChipByIndex(0x000B, 3)
    ChrClearFlags(0x000B, 0x0800)
    ChrSetChipByIndex(0x000B, 17)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x000B,
        (
            '#0010190422V#1006F要上了，亚妮拉丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000B, 0x00, 0x04, 1000)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0010190423V#1005F#4S烈破──无双击！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrClearFlags(0x000B, 0x0020)
    ChrSetChipByIndex(0x000B, 4)

    @scena.Lambda('lambda_11EA')
    def lambda_11EA():
        ChrWalkTo(0x00FE, 4180, 0, 25180, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_11EA)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_120A')
    def lambda_120A():
        CameraMove(5450, 0, 26870, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_120A)

    @scena.Lambda('lambda_1222')
    def lambda_1222():
        OP_6C(130000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1222)

    @scena.Lambda('lambda_1232')
    def lambda_1232():
        OP_6E(215, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1232)

    @scena.Lambda('lambda_1242')
    def lambda_1242():
        OP_67(0, 7460, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1242)

    ChrSetFlags(0x000B, 0x0020)
    ChrSetFlags(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 18)
    ChrSetSubChip(0x000B, 1)

    @scena.Lambda('lambda_126E')
    def lambda_126E():
        ChrMoveTo(0x00FE, 4770, 0, 26700, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_126E)

    WaitForThreadExit(0x000B, 0x0001)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetChipByIndex(0x000B, 7)
    ChrSetSubChip(0x000B, 0)

    @scena.Lambda('lambda_129D')
    def lambda_129D():
        OP_9E(0x00FE, 30, 0, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_129D)

    PlayEffect(0x00, 0x00, 0x000B, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x000B, 0x00, 0x03, 2000)
    PlayEffect(0x00, 0x00, 0x000B, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x000B, 0x00, 0x03, 2000)
    PlayEffect(0x00, 0x00, 0x000B, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x000B, 0x00, 0x03, 2000)
    PlayEffect(0x00, 0x00, 0x000B, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x000B, 0x00, 0x03, 2000)
    ChrClearFlags(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetSubChip(0x000B, 0)
    Sleep(100)

    @scena.Lambda('lambda_13C3')
    def lambda_13C3():
        OP_99(0x00FE, 0x00, 0x0C, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_13C3)

    Sleep(400)

    PlayEffect(0x01, 0x01, 0x000B, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_140D')
    def lambda_140D():
        CameraMove(6410, 0, 28130, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_140D)

    @scena.Lambda('lambda_1425')
    def lambda_1425():
        OP_6C(156000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1425)

    @scena.Lambda('lambda_1435')
    def lambda_1435():
        OP_6E(226, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1435)

    @scena.Lambda('lambda_1445')
    def lambda_1445():
        OP_67(0, 6540, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1445)

    @scena.Lambda('lambda_145D')
    def lambda_145D():
        ChrJumpTo(0x00FE, 6860, 0, 29720, 600, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_145D)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_1480')
    def lambda_1480():
        ChrJumpTo(0x00FE, 7500, 0, 30480, 400, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1480)

    WaitForThreadExit(0x0008, 0x0001)
    StopEffect(0x00, 0x00)
    StopEffect(0x01, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0120190424V#814F#6P哇哇，好猛烈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190425V#816F不过……\n',
            '这次轮到我了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetSubChip(0x0008, 0)
    ChrSetDirection(0x0008, 293, 1000)
    ChrSetDirection(0x0008, 23, 1000)
    ChrSetDirection(0x0008, 113, 1000)
    ChrSetDirection(0x0008, 203, 1000)

    @scena.Lambda('lambda_152B')
    def lambda_152B():
        ChrJumpTo(0x00FE, 3670, 0, 25710, 400, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_152B)

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0120190426V#815F#4S剑技──八叶灭杀！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0020)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x000B, 8)
    ChrSetSubChip(0x000B, 1)
    Sleep(100)

    Fade(500)
    CameraMove(6130, 0, 28370, 0)
    OP_6C(68000, 0)

    @scena.Lambda('lambda_15C8')
    def lambda_15C8():
        ChrWalkTo(0x00FE, 4660, 0, 26660, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_15C8)

    @scena.Lambda('lambda_15E3')
    def lambda_15E3():
        CameraMove(4730, 0, 26490, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_15E3)

    @scena.Lambda('lambda_15FB')
    def lambda_15FB():
        OP_6C(50000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15FB)

    WaitForThreadExit(0x0008, 0x0001)
    CreateThread(0x000A, 0x01, 0x00, func_07_2435)
    WaitForThreadExit(0x000A, 0x0001)
    StopEffect(0x03, 0x00)

    ChrTalk(
        0x000B,
        (
            '#0010190427V#1021F呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190428V#815F#6P还没结束呢～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_1671')
    def lambda_1671():
        ChrWalkTo(0x00FE, 3960, 0, 25900, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1671)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 11)
    ChrSetSubChip(0x0008, 0)
    CreateThread(0x000A, 0x01, 0x00, func_09_2A2B)

    ChrTalk(
        0x000B,
        (
            '#0010190429V#1003F（呜……\n',
            '这样下去会撑不住的……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190430V#1002F（那就……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    StopEffect(0x03, 0x00)
    PlaySE(214, 0x00, 0x64)
    ChrSetChipByIndex(0x000B, 17)
    ChrSetSubChip(0x000B, 7)
    ChrSetAfterImage(0x00, 0x000B, 0x0032, 0x01F4)

    @scena.Lambda('lambda_171A')
    def lambda_171A():
        ChrMoveTo(0x00FE, 5350, 0, 24530, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_171A)

    @scena.Lambda('lambda_1735')
    def lambda_1735():
        OP_99(0x00FE, 0x07, 0x0E, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1735)

    @scena.Lambda('lambda_1745')
    def lambda_1745():
        CameraMove(4400, 0, 26560, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1745)

    @scena.Lambda('lambda_175D')
    def lambda_175D():
        OP_6C(0, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_175D)

    @scena.Lambda('lambda_176D')
    def lambda_176D():
        OP_67(0, 6660, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_176D)

    WaitForThreadExit(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 8)
    ChrSetSubChip(0x000B, 1)
    ChrTurnDirection(0x000B, 0x0008, 0)
    ChrSetAfterImage(0x01, 0x000B, 0x0000, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0120190431V#814F#5P#10A咦，不会吧！？',
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    OP_56(0x00)

    ChrTalk(
        0x000B,
        (
            '#0010190432V#1005F#3S#10A得手了！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x00)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetSubChip(0x000B, 0)

    @scena.Lambda('lambda_180C')
    def lambda_180C():
        OP_99(0x00FE, 0x00, 0x0C, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_180C)

    Sleep(400)

    ChrTurnDirection(0x0008, 0x000B, 0)
    ChrSetChipByIndex(0x0008, 14)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_1832')
    def lambda_1832():
        ChrMoveTo(0x00FE, 3100, 0, 26670, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1832)

    @scena.Lambda('lambda_184D')
    def lambda_184D():
        OP_9E(0x00FE, 20, 0, 0, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_184D)

    PlayEffect(0x01, 0x01, 0x0008, 500, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0xFF, 0x0008, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    OP_20(0x000005DC)

    ChrTalk(
        0x0008,
        (
            '#0120190433V#1312F#5P#10A呀～！',
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    OP_56(0x00)
    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x02)
    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 0)
    OP_99(0x0008, 0x00, 0x03, 1000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0120190434V#1312F#5P好痛～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrClearFlags(0x000B, 0x0020)
    ChrSetChipByIndex(0x000B, 19)
    ChrSetSubChip(0x000B, 0)
    OP_0D()
    Sleep(500)

    ChrSetChipByIndex(0x000B, 20)
    ChrSetSubChip(0x000B, 0)

    @scena.Lambda('lambda_1975')
    def lambda_1975():
        CameraMove(3820, 0, 27610, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1975)

    OP_92(0x000B, 0x0008, 1500, 4000, 0x00)
    OP_62(0x000B, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetChipByIndex(0x000B, 21)
    ChrSetSubChip(0x000B, 0)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0010190435V#1004F没、没事吧，亚妮拉丝？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    PlayBGM(25)
    Sleep(600)

    ChrTalk(
        0x0008,
        (
            '#0120190436V#819F#5P啊哈哈，没事啦。\n',
            '总算来得及防御。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Fade(500)
    ChrSetChipByIndex(0x000B, 19)
    ChrSetSubChip(0x000B, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0120190437V#1316F#5P唉～不过真是败给你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190438V#1314F还是被艾丝蒂尔\n',
            '挡回了那招～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010190439V#1016F嘿嘿，是歪打正着啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190440V#1006F之前老被你压得死死的，\n',
            '也要稍微讨回一点颜面才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190441V#816F#5P呵呵。\n',
            '真有干劲啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190442V#1310F那么，就顺便\n',
            '再来一回合试试怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010190443V#1006F嗯，正合我意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, 3820, 0, 12520, 0)
    ChrClearFlags(0x0009, 0x0080)

    NpcTalk(
        0x0009,
        '女性的声音',
        (
            '#2750190444V#5P哎呀哎呀，你们俩可真有精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    Fade(500)
    CameraMove(4150, 0, 23370, 0)
    OP_67(0, 7660, -10000, 0)
    CameraSetDistance(3090, 0)
    OP_6C(122000, 0)
    OP_6E(270, 0)

    @scena.Lambda('lambda_1C7A')
    def lambda_1C7A():
        ChrWalkTo(0x0009, 3820, 0, 22130, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1C7A)

    Sleep(100)

    ChrTurnDirection(0x000B, 0x0009, 400)
    Sleep(100)

    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(200)

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0120190445V#811F#6P啊，管理员。\n',
            '早上好～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010190446V#1018F#5P管理员，早上好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#2750190447V#2P你们早啊。\n',
            '艾丝蒂尔，亚妮拉丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2750190448V早餐已经做好了，\n',
            '我过来招呼你们用餐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2750190449V嗯～该不会打扰你们了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010190450V#1004F#5P啊，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0008, 400)
    Sleep(300)

    ChrTalk(
        0x000B,
        (
            '#0010190451V#1015F#5P亚妮拉丝你觉得呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000B, 400)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0120190452V#817F#6P嗯～是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190453V#810F饭菜冷掉就可惜了，\n',
            '今天早上就到此为止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E73')
    def lambda_1E73():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1E73)

    Sleep(50)

    @scena.Lambda('lambda_1E86')
    def lambda_1E86():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1E86)

    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0120190454V#1310F#6P管理员。\n',
            '克鲁茨前辈现在在干吗呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2750190455V#2P克鲁茨先生\n',
            '说要去准备演习，\n',
            '已经先吃完早餐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2750190456V听说今天的演习\n',
            '相当严峻呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010190457V#1019F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190458V#1317F#6P前、前辈是\n',
            '那么说的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2750190459V嗯，他要我转告说，\n',
            '请你们早餐要好好吃饱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2750190460V你们两人都多吃点，\n',
            '好储备足够的体力哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_23(0x01C3)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T5110._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x2019
@scena.Code('func_05_2019')
def func_05_2019():
    ChrSetPos(0x000B, 510, 0, 22930, 90)
    ChrSetPos(0x0008, 7610, 0, 24760, 270)

    @scena.Lambda('lambda_2041')
    def lambda_2041():
        ChrWalkTo(0x00FE, 4170, 0, 23740, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2041)

    Sleep(300)

    @scena.Lambda('lambda_2061')
    def lambda_2061():
        ChrWalkTo(0x00FE, 5580, 0, 23680, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2061)

    Sleep(300)

    WaitForThreadExit(0x000B, 0x0001)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetSubChip(0x000B, 5)

    @scena.Lambda('lambda_2090')
    def lambda_2090():
        OP_99(0x00FE, 0x05, 0x0C, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_2090)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_20A5')
    def lambda_20A5():
        ChrJumpTo(0x00FE, 5050, 0, 21290, 800, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_20A5)

    Sleep(200)

    @scena.Lambda('lambda_20C8')
    def lambda_20C8():
        ChrTurnDirection(0x0008, 0x000B, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_20C8)

    Sleep(200)

    TerminateThread(0x000B, 0x00)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetSubChip(0x000B, 0)
    ChrTurnDirection(0x0008, 0x000B, 1000)

    @scena.Lambda('lambda_20F0')
    def lambda_20F0():
        ChrWalkTo(0x00FE, 4350, 0, 23210, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_20F0)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_211A')
    def lambda_211A():
        ChrJumpTo(0x00FE, 4280, 0, 25860, 300, 6000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_211A)

    ChrSetSubChip(0x0008, 1)
    WaitForThreadExit(0x000B, 0x0000)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_214C')
    def lambda_214C():
        ChrMoveTo(0x00FE, 4180, 0, 24340, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_214C)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_216C')
    def lambda_216C():
        ChrMoveTo(0x00FE, 3960, 0, 27750, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_216C)

    ChrTurnDirection(0x0008, 0x000B, 1000)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetSubChip(0x0008, 1)
    Sleep(200)

    ChrSetChipByIndex(0x0008, 9)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_21A7')
    def lambda_21A7():
        ChrMoveTo(0x00FE, 4140, 0, 23950, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_21A7)

    ChrSetPos(0x000B, 3960, 0, 27750, 180)
    ChrSetPos(0x0008, 4140, 0, 23950, 0)

    Return()

# id: 0x0006 offset: 0x21DF
@scena.Code('func_06_21DF')
def func_06_21DF():
    ChrSetPos(0x000B, 3900, 0, 23500, 180)
    ChrSetPos(0x0008, 3900, 0, 20400, 0)
    Sleep(200)

    PlaySE(214, 0x00, 0x14)
    Sleep(300)

    PlaySE(214, 0x00, 0x14)
    Sleep(1000)

    PlaySE(132, 0x00, 0x28)
    Sleep(300)

    PlaySE(132, 0x00, 0x28)
    Sleep(300)

    PlaySE(214, 0x00, 0x28)
    ChrSetChipByIndex(0x000B, 8)
    ChrSetSubChip(0x000B, 0)
    ChrSetFlags(0x000B, 0x0020)

    @scena.Lambda('lambda_2248')
    def lambda_2248():
        ChrMoveTo(0x00FE, 3900, 0, 26960, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2248)

    WaitForThreadExit(0x000B, 0x0001)
    Sleep(200)

    ChrClearFlags(0x000B, 0x0020)
    ChrSetChipByIndex(0x000B, 4)
    ChrSetSubChip(0x000B, 0)

    @scena.Lambda('lambda_227C')
    def lambda_227C():
        ChrWalkTo(0x00FE, 3900, 0, 23180, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_227C)

    Sleep(200)

    @scena.Lambda('lambda_229C')
    def lambda_229C():
        ChrJumpTo(0x00FE, 3900, 0, 24890, 2000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_229C)

    PlaySE(163, 0x00, 0x3C)
    WaitForThreadExit(0x000B, 0x0001)
    ChrSetFlags(0x000B, 0x0020)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetSubChip(0x000B, 5)

    @scena.Lambda('lambda_22D3')
    def lambda_22D3():
        ChrMoveTo(0x00FE, 3900, 0, 21840, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_22D3)

    @scena.Lambda('lambda_22EE')
    def lambda_22EE():
        OP_99(0x00FE, 0x05, 0x09, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_22EE)

    PlaySE(132, 0x00, 0x3C)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x3C)

    @scena.Lambda('lambda_230D')
    def lambda_230D():
        ChrJumpTo(0x00FE, 3900, 0, 26960, 400, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_230D)

    @scena.Lambda('lambda_232B')
    def lambda_232B():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_232B)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x3C)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetSubChip(0x000B, 0)
    PlaySE(163, 0x00, 0x3C)

    @scena.Lambda('lambda_2352')
    def lambda_2352():
        ChrJumpTo(0x00FE, 3900, 0, 25350, 2000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2352)

    @scena.Lambda('lambda_2370')
    def lambda_2370():
        OP_99(0x00FE, 0x00, 0x09, 2500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2370)

    @scena.Lambda('lambda_2380')
    def lambda_2380():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_2380)

    Sleep(300)

    @scena.Lambda('lambda_2393')
    def lambda_2393():
        ChrJumpTo(0x00FE, 7610, 0, 24760, 400, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2393)

    @scena.Lambda('lambda_23B1')
    def lambda_23B1():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_23B1')

    DispatchAsync2(0x0008, 0x0002, lambda_23B1)

    Sleep(100)

    PlaySE(132, 0x00, 0x50)
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x50)
    Sleep(400)

    ChrSetChipByIndex(0x000B, 8)
    ChrSetSubChip(0x000B, 0)

    @scena.Lambda('lambda_23E5')
    def lambda_23E5():
        ChrJumpTo(0x00FE, 510, 0, 22930, 400, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_23E5)

    @scena.Lambda('lambda_2403')
    def lambda_2403():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2403')

    DispatchAsync2(0x000B, 0x0002, lambda_2403)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x50)
    TerminateThread(0x0008, 0x02)
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x50)
    TerminateThread(0x000B, 0x02)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetSubChip(0x000B, 0)

    Return()

# id: 0x0007 offset: 0x2435
@scena.Code('func_07_2435')
def func_07_2435():
    ChrSetChipByIndex(0x0008, 11)
    ChrSetSubChip(0x0008, 0)
    OP_99(0x0008, 0x00, 0x07, 4000)
    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_2488')
    def lambda_2488():
        OP_9E(0x00FE, 30, 0, 2000, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_2488)

    PlayEffect(0x03, 0x00, 0x0008, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_24D7')
    def lambda_24D7():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_24D7)

    @scena.Lambda('lambda_24F2')
    def lambda_24F2():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_24F2)

    OP_99(0x0008, 0x00, 0x07, 4000)
    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0x00, 0x0008, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_2585')
    def lambda_2585():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2585)

    @scena.Lambda('lambda_25A0')
    def lambda_25A0():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_25A0)

    OP_99(0x0008, 0x00, 0x07, 4000)
    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0x00, 0x0008, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_2633')
    def lambda_2633():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2633)

    @scena.Lambda('lambda_264E')
    def lambda_264E():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_264E)

    OP_99(0x0008, 0x00, 0x07, 4000)
    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0x00, 0x0008, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_26E1')
    def lambda_26E1():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_26E1)

    @scena.Lambda('lambda_26FC')
    def lambda_26FC():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_26FC)

    OP_99(0x0008, 0x00, 0x07, 4000)
    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0x00, 0x0008, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_278F')
    def lambda_278F():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_278F)

    @scena.Lambda('lambda_27AA')
    def lambda_27AA():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_27AA)

    OP_99(0x0008, 0x00, 0x07, 4000)
    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0x00, 0x0008, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_283D')
    def lambda_283D():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_283D)

    @scena.Lambda('lambda_2858')
    def lambda_2858():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2858)

    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2878')
    def lambda_2878():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 3000, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2878)

    Sleep(500)

    @scena.Lambda('lambda_289B')
    def lambda_289B():
        OP_99(0x0008, 0x00, 0x05, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_289B)

    @scena.Lambda('lambda_28AB')
    def lambda_28AB():
        ChrMoveToRelativeAsync(0x00FE, -100, 0, -130, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_28AB)

    Sleep(300)

    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    OP_7C(0, 500, 300, 100)
    WaitForThreadExit(0x0008, 0x0000)
    PlayEffect(0x03, 0x00, 0x0008, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_2950')
    def lambda_2950():
        ChrJumpTo(0x00FE, 6440, 0, 28520, 2500, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2950)

    CreateThread(0x000A, 0x02, 0x00, func_08_2990)
    WaitForThreadExit(0x000A, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)
    PlaySE(164, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x000B, 1000)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetSubChip(0x0008, 0)

    Return()

# id: 0x0008 offset: 0x2990
@scena.Code('func_08_2990')
def func_08_2990():
    ChrSetDirection(0x0008, 0, 2000)
    ChrSetDirection(0x0008, 45, 2000)
    ChrSetDirection(0x0008, 90, 2000)
    ChrSetDirection(0x0008, 135, 2000)
    ChrSetDirection(0x0008, 180, 2000)
    ChrSetDirection(0x0008, 225, 2000)
    ChrSetDirection(0x0008, 270, 2000)
    ChrSetDirection(0x0008, 315, 2000)
    ChrSetDirection(0x0008, 0, 2000)
    ChrSetDirection(0x0008, 45, 2000)
    ChrSetDirection(0x0008, 90, 2000)
    ChrSetDirection(0x0008, 135, 2000)
    ChrSetDirection(0x0008, 180, 2000)
    ChrSetDirection(0x0008, 225, 2000)
    ChrSetDirection(0x0008, 270, 2000)
    ChrSetDirection(0x0008, 315, 2000)
    ChrSetDirection(0x0008, 0, 2000)
    ChrSetDirection(0x0008, 45, 2000)
    ChrSetDirection(0x0008, 90, 2000)
    ChrSetDirection(0x0008, 135, 2000)
    ChrSetDirection(0x0008, 180, 2000)
    ChrSetDirection(0x0008, 203, 2000)

    Return()

# id: 0x0009 offset: 0x2A2B
@scena.Code('func_09_2A2B')
def func_09_2A2B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2AD3',
    )

    PlayEffect(0x03, 0x00, 0x0008, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x0008, 0x00, 0x07, 4000)
    PlayEffect(0x04, 0xFF, 0x000B, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_2AB2')
    def lambda_2AB2():
        OP_9E(0x000B, 30, 0, 300, 4000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2AB2)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2AD0',
    )

    Jump('loc_2AD3')

    def _loc_2AD0(): pass

    label('loc_2AD0')

    Jump('func_09_2A2B')

    def _loc_2AD3(): pass

    label('loc_2AD3')

    Return()

# id: 0x000A offset: 0x2AD4
@scena.Code('func_0A_2AD4')
def func_0A_2AD4():
    EventBegin(0x00)
    Fade(1000)
    ChrSetDirection(0x000A, 0, 0)
    ChrSetSubChip(0x000A, 0)
    ChrSetPos(0x0101, -3720, 0, -28700, 180)
    ChrSetPos(0x010A, -2700, 0, -28850, 180)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0xA, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0xA, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0xA, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0330190795V#840F#6P两人都准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000C)

    Return()

# id: 0x000B offset: 0x2B74
@scena.Code('func_0B_2B74')
def func_0B_2B74():
    EventBegin(0x00)
    Fade(1000)
    ChrSetDirection(0x000A, 0, 0)
    ChrSetSubChip(0x000A, 0)
    ChrSetPos(0x0101, -3720, 0, -28700, 180)
    ChrSetPos(0x010A, -2700, 0, -28850, 180)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0xA, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0xA, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0xA, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0330190788V#840F#6P制造了新的结晶回路，\n',
            '也准备好回复系魔法了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190789V这样一来总算可以出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190790V#1007F#5P哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190791V#818F嗯，记得是西边的\n',
            '中世纪地下水道吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0330190792V#843F#6P嗯嗯，是『巴斯塔尔水道』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190793V#842F话先说在前头，水道里\n',
            '徘徊着危险的魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190794V你们两人都准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C5, 0x01, 0x0040)
    OP_28(0x00C5, 0x04, 0x10)
    OP_28(0x00C5, 0x04, 0x20)
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x2D57
@scena.Code('func_0C_2D57')
def func_0C_2D57():
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
            TXT(0x00, '【向目的地出发】\n'),
            TXT(0x01, '【还要准备准备】\n'),
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
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DF2',
    )

    ChrTalk(
        0x000A,
        (
            '#0330190796V#840F#6P明白了。\n',
            '准备充足一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_2DF2(): pass

    label('loc_2DF2')

    ChrTalk(
        0x000A,
        (
            '#0330190797V#840F#6P明白了。\n',
            '那么出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190798V你们两个都跟我来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190799V#1018F#5P明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190800V#1310F明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x0040)
    ChrSetDirection(0x000A, 180, 500)

    @scena.Lambda('lambda_2E94')
    def lambda_2E94():
        ChrWalkTo(0x000A, -2940, 0, -41020, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2E94)

    Sleep(300)

    @scena.Lambda('lambda_2EB4')
    def lambda_2EB4():
        ChrWalkTo(0x010A, -2940, 0, -41020, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2EB4)

    Sleep(500)

    @scena.Lambda('lambda_2ED4')
    def lambda_2ED4():
        ChrWalkTo(0x0101, -2940, 0, -41020, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2ED4)

    Sleep(3000)

    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    ChrClearFlags(0x0101, 0x0040)
    Call(0, 0x000D)
    NewScene('ED6_DT21/C5503._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x2F11
@scena.Code('func_0D_2F11')
def func_0D_2F11():
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS137._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 500, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2F72(): pass

    label('loc_2F72')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30BE',
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
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2FD3'),
        (0x00000001, 'loc_3039'),
        (-1, 'loc_30BB'),
    )

    def _loc_2FD3(): pass

    label('loc_2FD3')

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('克鲁茨')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0330190801V#840F目的地是西边的\n',
            '【巴斯塔尔水道】。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190802V选那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_30BB')

    def _loc_3039(): pass

    label('loc_3039')

    TalkSetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【巴斯塔尔水道】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_30A8'),
        (0x00000001, 'loc_30B5'),
        (-1, 'loc_30B8'),
    )

    def _loc_30A8(): pass

    label('loc_30A8')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_30B8')

    def _loc_30B5(): pass

    label('loc_30B5')

    Jump('loc_30B8')

    def _loc_30B8(): pass

    label('loc_30B8')

    Jump('loc_30BB')

    def _loc_30BB(): pass

    label('loc_30BB')

    Jump('loc_2F72')

    def _loc_30BE(): pass

    label('loc_30BE')

    OP_C6(0x00, 0x00, -358000, -37000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    Return()

# id: 0x000E offset: 0x3108
@scena.Code('func_0E_3108')
def func_0E_3108():
    MapClearFlags(0x02000000)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_312B',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_313C')

    def _loc_312B(): pass

    label('loc_312B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 2, 0x1012)),
            Expr.Return,
        ),
        'loc_313C',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_313C(): pass

    label('loc_313C')

    MapSetFlags(0x00000080)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS137._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 500, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_31AD(): pass

    label('loc_31AD')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34CA',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_31D8'),
        (0x00000001, 'loc_3204'),
        (0x00000002, 'loc_3241'),
        (-1, 'loc_3293'),
    )

    def _loc_31D8(): pass

    label('loc_31D8')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
        ),
    )

    Jump('loc_3293')

    def _loc_3204(): pass

    label('loc_3204')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
            TXT(0x02, '【圣科洛瓦森林】\n'),
        ),
    )

    Jump('loc_3293')

    def _loc_3241(): pass

    label('loc_3241')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
            TXT(0x02, '【圣科洛瓦森林】\n'),
            TXT(0x03, '【格林姆瑟尔小要塞】\n'),
        ),
    )

    Jump('loc_3293')

    def _loc_3293(): pass

    label('loc_3293')

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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_32BD'),
        (0x00000001, 'loc_333D'),
        (0x00000002, 'loc_33BF'),
        (0x00000003, 'loc_3441'),
        (-1, 'loc_34C7'),
    )

    def _loc_32BD(): pass

    label('loc_32BD')

    TalkSetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【训练场宿舍】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_332A'),
        (0x00000001, 'loc_3337'),
        (-1, 'loc_333A'),
    )

    def _loc_332A(): pass

    label('loc_332A')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_333A')

    def _loc_3337(): pass

    label('loc_3337')

    Jump('loc_333A')

    def _loc_333A(): pass

    label('loc_333A')

    Jump('loc_34C7')

    def _loc_333D(): pass

    label('loc_333D')

    TalkSetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【巴斯塔尔水道】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_33AC'),
        (0x00000001, 'loc_33B9'),
        (-1, 'loc_33BC'),
    )

    def _loc_33AC(): pass

    label('loc_33AC')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_33BC')

    def _loc_33B9(): pass

    label('loc_33B9')

    Jump('loc_33BC')

    def _loc_33BC(): pass

    label('loc_33BC')

    Jump('loc_34C7')

    def _loc_33BF(): pass

    label('loc_33BF')

    TalkSetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【圣科洛瓦森林】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_342E'),
        (0x00000001, 'loc_343B'),
        (-1, 'loc_343E'),
    )

    def _loc_342E(): pass

    label('loc_342E')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_343E')

    def _loc_343B(): pass

    label('loc_343B')

    Jump('loc_343E')

    def _loc_343E(): pass

    label('loc_343E')

    Jump('loc_34C7')

    def _loc_3441(): pass

    label('loc_3441')

    TalkSetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【格林姆瑟尔小要塞】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_34B4'),
        (0x00000001, 'loc_34C1'),
        (-1, 'loc_34C4'),
    )

    def _loc_34B4(): pass

    label('loc_34B4')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34C4')

    def _loc_34C1(): pass

    label('loc_34C1')

    Jump('loc_34C4')

    def _loc_34C4(): pass

    label('loc_34C4')

    Jump('loc_34C7')

    def _loc_34C7(): pass

    label('loc_34C7')

    Jump('loc_31AD')

    def _loc_34CA(): pass

    label('loc_34CA')

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_34E3'),
        (0x00000001, 'loc_3517'),
        (0x00000002, 'loc_354B'),
        (0x00000003, 'loc_357F'),
        (-1, 'loc_35B3'),
    )

    def _loc_34E3(): pass

    label('loc_34E3')

    OP_C6(0x00, 0x00, -640000, 0, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_35B3')

    def _loc_3517(): pass

    label('loc_3517')

    OP_C6(0x00, 0x00, -358000, -37000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_35B3')

    def _loc_354B(): pass

    label('loc_354B')

    OP_C6(0x00, 0x00, -362000, -266000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_35B3')

    def _loc_357F(): pass

    label('loc_357F')

    OP_C6(0x00, 0x00, -64000, -340000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_35B3')

    def _loc_35B3(): pass

    label('loc_35B3')

    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_35D5'),
        (0x00000001, 'loc_35ED'),
        (0x00000002, 'loc_35F9'),
        (0x00000003, 'loc_3605'),
        (-1, 'loc_3611'),
    )

    def _loc_35D5(): pass

    label('loc_35D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 3, 0x101B)),
            Expr.Return,
        ),
        'loc_35E1',
    )

    MapSetFlags(0x02000000)

    def _loc_35E1(): pass

    label('loc_35E1')

    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3611')

    def _loc_35ED(): pass

    label('loc_35ED')

    NewScene('ED6_DT21/C5503._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3611')

    def _loc_35F9(): pass

    label('loc_35F9')

    NewScene('ED6_DT21/C5507._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_3611')

    def _loc_3605(): pass

    label('loc_3605')

    NewScene('ED6_DT21/C5508._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_3611')

    def _loc_3611(): pass

    label('loc_3611')

    Return()

# id: 0x000F offset: 0x3612
@scena.Code('func_0F_3612')
def func_0F_3612():
    EventBegin(0x00)
    ChrSetPos(0x0101, -4030, 0, -16260, 4)
    ChrSetPos(0x010A, -3010, 0, -16920, 0)
    CameraMove(-4570, 0, 10280, 0)
    OP_67(0, 7680, -10000, 0)
    CameraSetDistance(4880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_3682')
    def lambda_3682():
        CameraMove(-3880, 0, -13000, 5000)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_3682)

    WaitForThreadExit(0x010A, 0x0000)
    Fade(1000)
    CameraMove(-4570, 0, -16000, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3020, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191321V#5P#1002F从这里看上去\n',
            '好像没有人的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191322V#6P#812F嗯……\n',
            '进去也没关系吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191323V但是，也有可能设了陷阱，\n',
            '所以必须要谨慎地行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191324V#5P#1002F明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0203, 3, 0x101B))
    OP_28(0x0080, 0x01, 0x0001)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0010 offset: 0x37BD
@scena.Code('func_10_37BD')
def func_10_37BD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 6, 0x1006)),
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_385C',
    )

    EventBegin(0x01)
    OP_4A(0x000A, 255)
    ChrTurnDirection(0x000A, 0x0000, 400)

    ChrTalk(
        0x000A,
        (
            '#0330190803V#843F你们两人都准备好了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190804V#840F要出发的时候\n',
            '就跟我说一声吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    ChrSetDirection(0x000A, 0, 0)
    OP_4B(0x000A, 255)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_3967')

    def _loc_385C(): pass

    label('loc_385C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38E1',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010190805V#1015F……不知不觉中\n',
            '演习就要开始了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190806V得回房间整理装备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_3967')

    def _loc_38E1(): pass

    label('loc_38E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 6, 0x1006)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3967',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010190807V#1015F……让克鲁茨前辈他们\n',
            '等太久可就不好了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190808V必须赶快到大门去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3967(): pass

    label('loc_3967')

    Return()

# id: 0x0011 offset: 0x3968
@scena.Code('func_11_3968')
def func_11_3968():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　 游击士协会\n',
            '【卢·洛克尔训练场】',
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
