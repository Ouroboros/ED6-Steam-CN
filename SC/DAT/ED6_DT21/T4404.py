import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4404_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4404   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '杜南公爵'),
    TXT(0x02, '凯诺娜'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '特务兵'),
    TXT(0x05, '特务兵'),
    TXT(0x06, '特务兵'),
    TXT(0x07, '特务兵'),
    TXT(0x08, '特务兵'),
    TXT(0x09, '特务兵'),
    TXT(0x0A, '导力战车『奥尔杰尤』'),
    TXT(0x0B, '王都格兰赛尔·码头南'),
    TXT(0x0C, '侵蚀狼犬'),
    TXT(0x0D, '侵蚀狼犬'),
    TXT(0x0E, '侵蚀狼犬'),
    TXT(0x0F, '侵蚀狼犬'),
    TXT(0x10, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4404.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2A5C
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
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT27/CH03120._CH', 'ED6_DT27/CH03120P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
        ('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH00444._CH', 'ED6_DT07/CH00444P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
    ]

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
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
            direction           = 0,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0189,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -880,
            z                   = 0,
            y                   = -32689,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2AA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -670,
            z           = 0,
            y           = 15150,
            word_0C     = 0x0000,
            word_0E     = 0x0012,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -11530,
            z           = 0,
            y           = 35690,
            word_0C     = 0x0000,
            word_0E     = 0x0012,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13160,
            z           = 0,
            y           = 25810,
            word_0C     = 0x0000,
            word_0E     = 0x0012,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 14350,
            z           = 0,
            y           = 44170,
            word_0C     = 0x0000,
            word_0E     = 0x0012,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x31A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 21200,
            y           = -2000,
            z           = 47800,
            range       = 23000,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000F35C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x33A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x33A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_35A',
    )

    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)

    def _loc_35A(): pass

    label('loc_35A')

    Return()

# id: 0x0001 offset: 0x35B
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE2370, 0xFFFEE2D8, 0x0023006E)
    OP_22(0x01C5, 0x00, 0x64)

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x45D),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_387',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_387(): pass

    label('loc_387')

    OP_72(0x0007, 0x0010)
    OP_72(0x000A, 0x0010)
    OP_72(0x000B, 0x0010)
    OP_72(0x0007, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_72(0x000B, 0x0004)
    OP_72(0x0001, 0x0010)
    OP_72(0x0002, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_72(0x0008, 0x0010)
    OP_72(0x0001, 0x0004)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_72(0x0005, 0x0010)
    OP_72(0x0004, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0005, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0006, 0x0004)
    OP_71(0x000C, 0x0004)

    Return()

# id: 0x0002 offset: 0x3F1
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_406',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_406(): pass

    label('loc_406')

    Return()

# id: 0x0003 offset: 0x407
@scena.Code('func_03_407')
def func_03_407():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_423',
    )

    Call(0, 0x0014)
    FadeIn(0, 0)

    def _loc_423(): pass

    label('loc_423')

    Fade(1000)
    OP_6D(22590, 0, 54310, 0)
    OP_67(0, 12420, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(138000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 22670, 0, 55450, 90)
    SetChrPos(0x00F7, 22590, 0, 54260, 90)
    SetChrPos(0x0109, 21470, 0, 54830, 90)
    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 45)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0008, 37560, 0, 53580, 270)
    SetChrPos(0x0009, 35110, 0, 55020, 270)
    SetChrPos(0x000A, 38350, 0, 53580, 270)
    SetChrPos(0x000B, 35840, 0, 55950, 270)
    SetChrPos(0x000C, 35880, 0, 54180, 270)
    SetChrPos(0x000D, 36530, 0, 56690, 270)
    SetChrPos(0x000E, 36530, 0, 53240, 270)
    SetChrPos(0x000F, 38030, 0, 55680, 270)
    SetChrPos(0x0010, 37130, 0, 54760, 270)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    OP_0D()
    OP_20(0x000007D0)

    NpcTalk(
        0x0009,
        '女人的声音',
        (
            '#0610270434V#4P哼，果然来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0613')
    def lambda_0613():
        OP_6D(33260, 0, 54610, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0613)

    @scena.Lambda('lambda_062B')
    def lambda_062B():
        OP_67(0, 6790, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_062B)

    @scena.Lambda('lambda_0643')
    def lambda_0643():
        OP_6B(2920, 3000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0643)

    @scena.Lambda('lambda_0653')
    def lambda_0653():
        OP_6C(135000, 3000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_0653)

    @scena.Lambda('lambda_0663')
    def lambda_0663():
        OP_6E(316, 3000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_0663)

    @scena.Lambda('lambda_0673')
    def lambda_0673():
        OP_8E(0x00FE, 29000, 0, 55740, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0673)

    Sleep(100)

    @scena.Lambda('lambda_0693')
    def lambda_0693():
        OP_8E(0x00FE, 29000, 0, 54590, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_0693)

    Sleep(200)

    @scena.Lambda('lambda_06B3')
    def lambda_06B3():
        OP_8E(0x00FE, 27980, 0, 55320, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_06B3)

    Sleep(1000)

    OP_1D(0x56)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010270435V#1005F#6P凯诺娜上尉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610270436V#1182F#5P哼，是原上尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270437V军犬们那么吵闹，\n',
            '我就知道有问题，才出来看看……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270438V不愧是游击士，\n',
            '嗅觉相当灵敏呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270439V#1005F#6P别小看我们！\n',
            '竟然做出那种事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270440V连无辜的孩子都……\n',
            '绝对不能原谅！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610270441V#1181F#5P你在说什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270442V我们只是协助公爵阁下\n',
            '继承王位而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270443V无关的外人请让开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270444V#1020F#6P啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270445V公爵！？\n',
            '你又在做什么愚蠢的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0640270446V#226F#6P谁、谁会支持\n',
            '这样无谋的计划！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640270447V这、这些家伙只是\n',
            '打算利用我而已！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270448V#1060F嗯～好像是真的\n',
            '很不情愿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9E3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270449V#057F#2P这母狐狸……\n',
            '还不说实话吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270450V你真正的目的\n',
            '是解放理查德吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A51')

    def _loc_9E3(): pass

    label('loc_9E3')

    ChrTalk(
        0x0103,
        (
            '#0030270451V#022F#2P原上尉大人，差不多\n',
            '该说实话了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270452V你真正的目的\n',
            '是为了解放理查德上校吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A51(): pass

    label('loc_A51')

    ChrTalk(
        0x0101,
        (
            '#0010270453V#1004F#6P#3S咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610270454V#1183F#5P哈哈哈，连这\n',
            '都知道就好说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270455V#1186F──现在\n',
            '开始『再启动作战』！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270456V你们！\n',
            '努力撑个两分钟吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName('特务兵们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#2660270457V#3S是·长官！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    @scena.Lambda('lambda_0B62')
    def lambda_0B62():
        OP_6D(37020, 0, 54410, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0B62)

    @scena.Lambda('lambda_0B7A')
    def lambda_0B7A():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0B7A)

    CreateThread(0x000D, 0x00, 0x00, 0x0004)
    Sleep(100)

    CreateThread(0x000F, 0x00, 0x00, 0x0005)
    Sleep(100)

    CreateThread(0x0010, 0x00, 0x00, 0x0006)
    SetChrFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_0BAC')
    def lambda_0BAC():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0BAC)

    Sleep(50)

    @scena.Lambda('lambda_0BBF')
    def lambda_0BBF():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BBF)

    Sleep(50)

    @scena.Lambda('lambda_0BD2')
    def lambda_0BD2():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0BD2)

    @scena.Lambda('lambda_0BE0')
    def lambda_0BE0():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0BE0)

    Sleep(500)

    @scena.Lambda('lambda_0BF3')
    def lambda_0BF3():
        OP_8E(0x00FE, 47700, 1000, 54910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0BF3)

    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_0C34')
    def lambda_0C34():
        OP_8E(0x00FE, 46700, 1000, 54140, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C34)

    SetChrChipByIndex(0x0008, 0)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_0C5B')
    def lambda_0C5B():
        OP_8F(0x00FE, 46700, 1000, 54140, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C5B)

    @scena.Lambda('lambda_0C76')
    def lambda_0C76():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x000001F4, 0x00000BB8)
        Yield()

        Jump('lambda_0C76')

    DispatchAsync2(0x0008, 0x0002, lambda_0C76)

    Sleep(200)

    SetChrChipByIndex(0x000B, 15)

    @scena.Lambda('lambda_0C9D')
    def lambda_0C9D():
        OP_8E(0x00FE, 45700, 1000, 55950, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C9D)

    SetChrChipByIndex(0x000C, 12)

    @scena.Lambda('lambda_0CBD')
    def lambda_0CBD():
        OP_8E(0x00FE, 45700, 1000, 54180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0CBD)

    @scena.Lambda('lambda_0CD8')
    def lambda_0CD8():
        OP_6D(33260, 0, 54610, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0CD8)

    CreateThread(0x0009, 0x02, 0x00, 0x0007)
    WaitForThreadExit(0x0009, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010270458V#1005F#6P喂，等一下啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270459V公爵也就算了，\n',
            '至少先把玲还给我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x00, 0x0008)
    CreateThread(0x000E, 0x01, 0x00, 0x0009)
    CreateThread(0x000F, 0x01, 0x00, 0x000A)
    CreateThread(0x0010, 0x01, 0x00, 0x000B)

    @scena.Lambda('lambda_0D74')
    def lambda_0D74():
        OP_90(0x00FE, 2000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D74)

    Sleep(100)

    @scena.Lambda('lambda_0D94')
    def lambda_0D94():
        OP_90(0x00FE, 2000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0D94)

    Sleep(100)

    @scena.Lambda('lambda_0DB4')
    def lambda_0DB4():
        OP_90(0x00FE, 2000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_0DB4)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x000F, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#2660270460V#5P上尉殿下的决意和觉悟，\n',
            '绝不能让你们阻挠！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2670270461V#2P来吧，协会的走狗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270462V#1005F#6P可、可恶～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(400)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 3)
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EA4',
    )

    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0106, 7)

    Jump('loc_EAE')

    def _loc_EA4(): pass

    label('loc_EA4')

    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0103, 5)

    def _loc_EAE(): pass

    label('loc_EAE')

    Sleep(200)

    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0109, 9)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F0D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270463V#054F#2P真有种……\n',
            '那就把你们统统打垮！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F4C')

    def _loc_F0D(): pass

    label('loc_F0D')

    ChrTalk(
        0x0103,
        (
            '#0030270464V#024F#2P真有胆量……\n',
            '让我好好疼爱疼爱你们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F4C(): pass

    label('loc_F4C')

    Sleep(100)

    SetChrChipByIndex(0x000D, 12)
    SetChrChipByIndex(0x000E, 12)
    SetChrChipByIndex(0x000F, 15)
    SetChrChipByIndex(0x0010, 15)

    @scena.Lambda('lambda_0F6B')
    def lambda_0F6B():
        OP_90(0x00FE, 1500, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F6B)

    @scena.Lambda('lambda_0F86')
    def lambda_0F86():
        OP_90(0x00FE, 1500, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0F86)

    @scena.Lambda('lambda_0FA1')
    def lambda_0FA1():
        OP_90(0x00FE, 1500, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_0FA1)

    @scena.Lambda('lambda_0FBC')
    def lambda_0FBC():
        OP_90(0x00FE, -2000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0FBC)

    @scena.Lambda('lambda_0FD7')
    def lambda_0FD7():
        OP_90(0x00FE, -2000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0FD7)

    @scena.Lambda('lambda_0FF2')
    def lambda_0FF2():
        OP_90(0x00FE, -2000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0FF2)

    @scena.Lambda('lambda_100D')
    def lambda_100D():
        OP_90(0x00FE, -2000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_100D)

    @scena.Lambda('lambda_1028')
    def lambda_1028():
        OP_6B(2510, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1028)

    Sleep(200)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x00F7, 0xFF)
    TerminateThread(0x0109, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    Battle(0x0000045D, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_106C'),
        (-1, 'loc_1071'),
    )

    def _loc_106C(): pass

    label('loc_106C')

    OP_B4(0x00)

    Jump('loc_1071')

    def _loc_1071(): pass

    label('loc_1071')

    Call(0, 0x000C)

    Return()

# id: 0x0004 offset: 0x1076
@scena.Code('func_04_1076')
def func_04_1076():
    SetChrChipByIndex(0x00FE, 12)
    OP_8C(0x00FE, 180, 400)
    OP_8F(0x00FE, 36630, 0, 57940, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 11)

    Return()

# id: 0x0005 offset: 0x109C
@scena.Code('func_05_109C')
def func_05_109C():
    SetChrChipByIndex(0x00FE, 15)
    OP_8C(0x00FE, 180, 400)
    OP_8F(0x00FE, 37930, 0, 56900, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 14)

    Return()

# id: 0x0006 offset: 0x10C2
@scena.Code('func_06_10C2')
def func_06_10C2():
    SetChrChipByIndex(0x00FE, 15)
    OP_8C(0x00FE, 180, 400)
    OP_8F(0x00FE, 36830, 0, 56890, 3000, 0x00)
    SetChrChipByIndex(0x00FE, 14)

    Return()

# id: 0x0007 offset: 0x10E8
@scena.Code('func_07_10E8')
def func_07_10E8():
    WaitForThreadExit(0x0009, 0x0001)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    TerminateThread(0x0008, 0x02)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 45)
    OP_70(0x0000, 0x0000001F)
    OP_22(0x00D3, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(400)

    OP_22(0x0073, 0x00, 0x64)

    Return()

# id: 0x0008 offset: 0x112F
@scena.Code('func_08_112F')
def func_08_112F():
    SetChrChipByIndex(0x00FE, 12)
    OP_8E(0x00FE, 35760, 0, 55730, 4000, 0x00)
    SetChrChipByIndex(0x00FE, 11)
    OP_8C(0x00FE, 270, 600)

    Return()

# id: 0x0009 offset: 0x1155
@scena.Code('func_09_1155')
def func_09_1155():
    SetChrChipByIndex(0x00FE, 12)
    OP_8E(0x00FE, 35650, 0, 54100, 4000, 0x00)
    SetChrChipByIndex(0x00FE, 11)
    OP_8C(0x00FE, 270, 600)

    Return()

# id: 0x000A offset: 0x117B
@scena.Code('func_0A_117B')
def func_0A_117B():
    Sleep(100)

    SetChrChipByIndex(0x00FE, 15)
    OP_8E(0x00FE, 37340, 0, 55700, 4000, 0x00)
    SetChrChipByIndex(0x00FE, 14)
    OP_8C(0x00FE, 270, 600)

    Return()

# id: 0x000B offset: 0x11A6
@scena.Code('func_0B_11A6')
def func_0B_11A6():
    SetChrChipByIndex(0x00FE, 15)
    OP_8E(0x00FE, 37040, 0, 53730, 4000, 0x00)
    SetChrChipByIndex(0x00FE, 14)
    OP_8C(0x00FE, 270, 600)

    Return()

# id: 0x000C offset: 0x11CC
@scena.Code('func_0C_11CC')
def func_0C_11CC():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Sleep(500)

    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0010, 0x01)
    SetChrPos(0x0101, 33440, 0, 55730, 90)
    SetChrPos(0x00F7, 33440, 0, 54390, 90)
    SetChrPos(0x0109, 32000, 0, 55000, 90)
    SetChrPos(0x000D, 37250, 0, 55300, 270)
    SetChrPos(0x000E, 37250, 0, 54000, 270)
    SetChrPos(0x000F, 38260, 0, 55760, 270)
    SetChrPos(0x0010, 38260, 0, 53780, 270)
    SetChrChipByIndex(0x0101, 3)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_127F',
    )

    SetChrChipByIndex(0x0106, 7)

    Jump('loc_1284')

    def _loc_127F(): pass

    label('loc_127F')

    SetChrChipByIndex(0x0103, 5)

    def _loc_1284(): pass

    label('loc_1284')

    SetChrChipByIndex(0x0109, 9)
    SetChrChipByIndex(0x000D, 13)
    SetChrChipByIndex(0x000E, 13)
    SetChrChipByIndex(0x000F, 17)
    SetChrChipByIndex(0x0010, 17)
    SetChrSubChip(0x000D, 3)
    SetChrSubChip(0x000E, 3)
    SetChrSubChip(0x000F, 3)
    SetChrSubChip(0x0010, 3)
    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x0010, 0x00)
    OP_6D(35640, 0, 54600, 0)
    OP_67(0, 7090, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(133000, 0)
    OP_6E(316, 0)
    LoadEffect(0x00, 'monster\\ms30600d.eff')
    LoadEffect(0x01, 'monster\\ms30602a.eff')
    LoadEffect(0x02, 'monster\\ms30602b.eff')
    LoadEffect(0x03, 'monster\\ms30600b.eff')
    LoadEffect(0x04, 'monster\\ms30600a.eff')
    OP_6F(0x0000, 31)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#4300270465V可、可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#4310270466V#2P这些家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270467V#1005F#6P趁早死心吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270468V喂！\n',
            '赶快让开……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x000C, 0x0004)
    OP_A1(0x0011, 0x000C)
    SetChrFlags(0x0011, 0x0040)
    SetChrFlags(0x0011, 0x0004)
    SetChrPos(0x0011, 47700, 1000, 54940, 270)
    PlayEffect(0x01, 0xFF, 0x0011, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0x00FF, 0, 0, 0, 0)
    OP_20(0x00000000)
    PlayEffect(0x01, 0xFF, 0x0011, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01FE, 0x00, 0x64)
    OP_7C(0x00000000, 0x00000CE4, 0x00000BB8, 0x00000064)
    PlayEffect(0x02, 0xFF, 0x00FF, 40310, 1500, 54930, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0000, 2)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010270469V#1020F#6P哇哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270470V#1069F什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6D(38840, 40, 54260, 1000)
    PlayEffect(0x01, 0xFF, 0x0011, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01FE, 0x00, 0x64)
    OP_7C(0x00000000, 0x00000CE4, 0x00000BB8, 0x00000064)
    PlayEffect(0x02, 0xFF, 0x00FF, 40310, 1500, 54930, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 2)
    OP_70(0x0000, 0x00000004)
    OP_22(0x010F, 0x00, 0x64)
    Sleep(1000)

    OP_1D(0x71)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_164F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270471V#054F#2P可恶……\n',
            '这就是设计图上的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1688')

    def _loc_164F(): pass

    label('loc_164F')

    ChrTalk(
        0x0103,
        (
            '#0030270472V#024F#2P难不成……\n',
            '这就是设计图上的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1688(): pass

    label('loc_1688')

    ChrTalk(
        0x000F,
        (
            '#4300270473V#5P哈哈哈……\n',
            '看来赶上了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#4310270474V情、情报部荣光永存！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayEffect(0x01, 0xFF, 0x0011, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01FE, 0x00, 0x64)
    OP_7C(0x00000000, 0x00000CE4, 0x00000BB8, 0x00000064)
    PlayEffect(0x02, 0xFF, 0x00FF, 40310, 1500, 54930, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0000, 4)
    OP_70(0x0000, 0x0000001D)
    Sleep(500)

    OP_6F(0x0007, 1)
    OP_70(0x0007, 0x0000001E)
    OP_6F(0x000A, 1)
    OP_70(0x000A, 0x0000001E)
    OP_6F(0x000B, 1)
    OP_70(0x000B, 0x0000001E)

    @scena.Lambda('lambda_179F')
    def lambda_179F():
        OP_96(0x00FE, 0x00008110, 0x00000000, 0x0000D9B2, 0x000001F4, 0x00001388)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_179F)

    @scena.Lambda('lambda_17BD')
    def lambda_17BD():
        OP_96(0x00FE, 0x00008110, 0x00000000, 0x0000D476, 0x000001F4, 0x00001388)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_17BD)

    @scena.Lambda('lambda_17DB')
    def lambda_17DB():
        OP_96(0x00FE, 0x00007B70, 0x00000000, 0x0000D6D8, 0x000001F4, 0x00001388)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_17DB)

    Sleep(500)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x0109, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010270475V#1014F呀啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270476V#1070F这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayEffect(0x03, 0x03, 0x0011, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x04, 0x0011, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_18BB')
    def lambda_18BB():
        OP_6D(40070, 1000, 54760, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18BB)

    @scena.Lambda('lambda_18D3')
    def lambda_18D3():
        OP_67(0, 2600, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_18D3)

    @scena.Lambda('lambda_18EB')
    def lambda_18EB():
        OP_6B(4190, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_18EB)

    @scena.Lambda('lambda_18FB')
    def lambda_18FB():
        OP_6C(90000, 5000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_18FB)

    @scena.Lambda('lambda_190B')
    def lambda_190B():
        OP_6E(243, 5000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_190B)

    CreateThread(0x000D, 0x01, 0x00, 0x000D)
    CreateThread(0x000E, 0x01, 0x00, 0x000E)
    CreateThread(0x000F, 0x01, 0x00, 0x000F)
    CreateThread(0x0010, 0x01, 0x00, 0x0010)
    OP_24(0x0075, 0x64)

    @scena.Lambda('lambda_193B')
    def lambda_193B():
        OP_7C(0x00000064, 0x00000064, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_193B')

    DispatchAsync2(0x0011, 0x0003, lambda_193B)

    PlayEffect(0x00, 0x01, 0x0011, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x0011, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_71(0x000C, 0x0020)
    OP_B0(0x000C, 0x0F)
    OP_6F(0x000C, 21)
    OP_70(0x000C, 0x00000028)
    Sleep(300)

    @scena.Lambda('lambda_19DC')
    def lambda_19DC():
        OP_8E(0x0011, 41000, 1000, 54940, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_19DC)

    OP_22(0x0110, 0x00, 0x64)
    Sleep(1000)

    PlayEffect(0x04, 0x05, 0x0011, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x06, 0x0011, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0011, 0x0001)
    OP_23(0x0110)
    TerminateThread(0x0011, 0x03)
    OP_82(0x01, 0x02)
    OP_82(0x02, 0x02)
    OP_6F(0x000C, 1)
    OP_70(0x000C, 0x00000014)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010270477V#1020F#5P战、战车……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AF6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270478V#057F#2P这就是『奥尔杰尤』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B26')

    def _loc_1AF6(): pass

    label('loc_1AF6')

    ChrTalk(
        0x0103,
        (
            '#0030270479V#022F#2P这就是『奥尔杰尤』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B26(): pass

    label('loc_1B26')

    OP_B0(0x000C, 0x0F)
    OP_6F(0x000C, 21)
    OP_70(0x000C, 0x00000028)

    @scena.Lambda('lambda_1B3E')
    def lambda_1B3E():
        OP_7C(0x00000064, 0x00000064, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_1B3E')

    DispatchAsync2(0x0011, 0x0003, lambda_1B3E)

    PlayEffect(0x00, 0x01, 0x0011, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x0011, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    @scena.Lambda('lambda_1BC8')
    def lambda_1BC8():
        OP_8E(0x0011, 35140, 0, 54740, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1BC8)

    OP_22(0x0110, 0x00, 0x64)
    Sleep(300)

    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_1BF2')
    def lambda_1BF2():
        OP_96(0x00FE, 0x00005DAC, 0x00000000, 0x0000D6EC, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1BF2)

    Sleep(50)

    @scena.Lambda('lambda_1C15')
    def lambda_1C15():
        OP_96(0x00FE, 0x000061BC, 0x00000000, 0x0000D412, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1C15)

    Sleep(50)

    @scena.Lambda('lambda_1C38')
    def lambda_1C38():
        OP_96(0x00FE, 0x000061C6, 0x00000000, 0x0000D926, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C38)

    Sleep(50)

    WaitForThreadExit(0x0109, 0x0001)
    WaitForThreadExit(0x0109, 0x0002)
    WaitForThreadExit(0x0011, 0x0001)
    OP_23(0x0110)
    TerminateThread(0x0011, 0x03)
    OP_82(0x01, 0x02)
    OP_82(0x02, 0x02)
    OP_6F(0x000C, 1)
    OP_70(0x000C, 0x00000014)
    Fade(1000)
    OP_6D(31230, 0, 53830, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(135000, 0)
    OP_6E(538, 0)
    OP_0D()
    OP_72(0x000C, 0x0020)
    OP_22(0x006A, 0x00, 0x64)
    OP_6F(0x000C, 371)
    OP_70(0x000C, 0x00000186)
    OP_73(0x000C)
    OP_73(0x000C)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0001)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x0009, 0x0020)
    SetChrPos(0x0009, 35050, 2000, 56100, 270)

    @scena.Lambda('lambda_1D1B')
    def lambda_1D1B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1D1B)

    OP_8F(0x0009, 35050, 2600, 56100, 2000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0610270480V#1181F#6P如何呢……\n',
            '这个『奥尔杰尤』？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270481V有情报部独自开发，\n',
            '最新型的高机动导力战车哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270482V火力是帝国制战车的２倍──\n',
            '几乎能与警备飞艇相匹敌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270483V#1068F#2P又搞出这么离谱的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270484V#1009F#5P乱、乱七八糟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610270485V#1181F#6P由于没找到启动这个\n',
            '的高输出引擎，\n',
            '在差一步就完成的时候，引擎被王室收回了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270486V真没想到能够获得要用在『埃尔赛尤』\n',
            '上的新型引擎啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270487V哈哈哈，空之女神\n',
            '好像对我微笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270488V#1005F#2P慢、慢着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270489V你用这种东西\n',
            '想干什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0610270490V#1181F#6P我说过了吧。\n',
            '为了帮助公爵阁下即位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270491V为此必须获得\n',
            '女王陛下的认可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270492V#1020F#2P难、难道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_204C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270493V#054F#2P目标是城堡里的女王吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2080')

    def _loc_204C(): pass

    label('loc_204C')

    ChrTalk(
        0x0103,
        (
            '#0030270494V#024F#2P目标是城堡里的女王陛下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2080(): pass

    label('loc_2080')

    ChrTalk(
        0x0009,
        (
            '#0610270495V#1188F#6P哈哈哈！\n',
            '你们现在明白也晚了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270496V奥尔杰尤号\n',
            '可以轻易粉碎城门！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270497V全城的部队也不是对手！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270498V你们就咬着手指\n',
            '乖乖在一边看着吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_213C')
    def lambda_213C():
        OP_69(0x0011, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_213C)

    OP_8F(0x0009, 35050, 2000, 56100, 2000, 0x00)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x000000C8)
    SetChrFlags(0x0009, 0x0080)
    OP_22(0x00E6, 0x00, 0x64)
    OP_6F(0x000C, 391)
    OP_70(0x000C, 0x0000019A)
    OP_73(0x000C)

    @scena.Lambda('lambda_2184')
    def lambda_2184():
        OP_69(0x0011, 0x00000000)
        Yield()

        Jump('lambda_2184')

    DispatchAsync2(0x0011, 0x0001, lambda_2184)

    OP_B0(0x000C, 0x0F)
    OP_71(0x000C, 0x0020)
    OP_6F(0x000C, 21)
    OP_70(0x000C, 0x00000028)

    @scena.Lambda('lambda_21AC')
    def lambda_21AC():
        OP_7C(0x00000064, 0x00000064, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_21AC')

    DispatchAsync2(0x0011, 0x0003, lambda_21AC)

    PlayEffect(0x00, 0x01, 0x0011, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x0011, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_8E(0x0011, 32270, 0, 54740, 2000, 0x00)

    @scena.Lambda('lambda_224A')
    def lambda_224A():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_224A)

    @scena.Lambda('lambda_225A')
    def lambda_225A():
        OP_8E(0x00FE, 21450, 0, 54740, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_225A)

    OP_22(0x0110, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x00F7, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0109, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_22B5')
    def lambda_22B5():
        OP_96(0x00FE, 0x00006482, 0x00000000, 0x0000E7F4, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22B5)

    Sleep(50)

    @scena.Lambda('lambda_22D8')
    def lambda_22D8():
        OP_96(0x00FE, 0x00006446, 0x00000000, 0x0000C576, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_22D8)

    Sleep(50)

    @scena.Lambda('lambda_22FB')
    def lambda_22FB():
        OP_96(0x00FE, 0x00005D70, 0x00000000, 0x0000E772, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_22FB)

    @scena.Lambda('lambda_2319')
    def lambda_2319():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2319')

    DispatchAsync2(0x0101, 0x0003, lambda_2319)

    @scena.Lambda('lambda_232A')
    def lambda_232A():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_232A')

    DispatchAsync2(0x00F7, 0x0002, lambda_232A)

    @scena.Lambda('lambda_233B')
    def lambda_233B():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_233B')

    DispatchAsync2(0x0109, 0x0002, lambda_233B)

    WaitForThreadExit(0x0011, 0x0002)
    CreateThread(0x0011, 0x02, 0x00, 0x0011)

    @scena.Lambda('lambda_2358')
    def lambda_2358():
        OP_8C(0x00FE, 180, 50)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2358)

    OP_6F(0x000C, 61)
    OP_70(0x000C, 0x00000050)
    OP_22(0x01FE, 0x00, 0x64)
    Sleep(100)

    OP_6F(0x0001, 1)
    OP_70(0x0001, 0x0000001E)
    OP_6F(0x0008, 1)
    OP_70(0x0008, 0x0000001E)
    Sleep(10)

    OP_6F(0x0002, 1)
    OP_70(0x0002, 0x0000001E)
    OP_6F(0x0003, 1)
    OP_70(0x0003, 0x0000001E)
    TerminateThread(0x0011, 0x01)

    @scena.Lambda('lambda_23BF')
    def lambda_23BF():
        OP_7C(0x00000032, 0x00000032, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_23BF')

    DispatchAsync2(0x0011, 0x0000, lambda_23BF)

    Sleep(4000)

    OP_24(0x010F, 0x5A)
    OP_24(0x0110, 0x5A)
    Sleep(100)

    OP_24(0x010F, 0x50)
    OP_24(0x0110, 0x50)
    Sleep(100)

    OP_24(0x010F, 0x46)
    OP_24(0x0110, 0x46)
    Sleep(100)

    OP_24(0x010F, 0x3C)
    OP_24(0x0110, 0x3C)
    Sleep(100)

    OP_24(0x010F, 0x32)
    OP_24(0x0110, 0x32)
    Sleep(100)

    OP_24(0x010F, 0x28)
    OP_24(0x0110, 0x28)
    Sleep(100)

    OP_24(0x010F, 0x1E)
    OP_24(0x0110, 0x1E)
    Sleep(100)

    OP_24(0x010F, 0x14)
    OP_24(0x0110, 0x14)
    Sleep(100)

    OP_24(0x010F, 0x0A)
    OP_24(0x0110, 0x0A)
    Sleep(100)

    OP_23(0x010F)
    OP_23(0x0110)
    WaitForThreadExit(0x0011, 0x0002)
    Fade(1000)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x0109, 0x02)
    OP_6D(23950, 0, 55930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0011, 0x00)
    OP_8C(0x0109, 225, 0)
    OP_0D()
    OP_82(0x01, 0x00)
    OP_82(0x02, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010270499V#1020F#6P糟、糟了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2513',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270500V#054F#5P快追！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2533')

    def _loc_2513(): pass

    label('loc_2513')

    ChrTalk(
        0x0103,
        (
            '#0030270501V#024F#5P快追！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2533(): pass

    label('loc_2533')

    @scena.Lambda('lambda_2539')
    def lambda_2539():
        OP_8E(0x00FE, 17550, 0, 51690, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2539)

    Sleep(100)

    @scena.Lambda('lambda_2559')
    def lambda_2559():
        OP_8E(0x00FE, 15390, 0, 50150, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_2559)

    Sleep(100)

    @scena.Lambda('lambda_2579')
    def lambda_2579():
        OP_8E(0x00FE, 16260, 0, 50270, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2579)

    Sleep(1000)

    WaitForThreadExit(0x00F7, 0x0001)

    @scena.Lambda('lambda_259E')
    def lambda_259E():
        OP_8E(0x00FE, 15450, 0, 49150, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_259E)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x00F7, 0x0080)
    SetChrFlags(0x0109, 0x0080)
    OP_DB()

    @scena.Lambda('lambda_25D4')
    def lambda_25D4():
        OP_7C(0x00000032, 0x00000032, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_25D4')

    DispatchAsync2(0x0011, 0x0000, lambda_25D4)

    SetChrPos(0x0011, 13560, 0, 45760, 180)
    PlayEffect(0x00, 0x01, 0x0011, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x0011, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6D(13560, 0, 45760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_26A7')
    def lambda_26A7():
        OP_69(0x0011, 0x00000000)
        Yield()

        Jump('lambda_26A7')

    DispatchAsync2(0x0011, 0x0002, lambda_26A7)

    OP_22(0x010F, 0x00, 0x64)
    OP_22(0x0110, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_8E(0x0011, 13560, 0, 34080, 4500, 0x00)
    CreateThread(0x0011, 0x01, 0x00, 0x0012)

    @scena.Lambda('lambda_26E6')
    def lambda_26E6():
        OP_8C(0x00FE, 270, 52)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_26E6)

    OP_22(0x01FE, 0x00, 0x64)
    Sleep(200)

    OP_6F(0x0004, 1)
    OP_70(0x0004, 0x0000001E)
    Sleep(10)

    OP_6F(0x0005, 1)
    OP_70(0x0005, 0x0000001E)
    OP_6F(0x0006, 1)
    OP_70(0x0006, 0x0000001E)
    WaitForThreadExit(0x0011, 0x0001)
    CreateThread(0x0011, 0x01, 0x00, 0x0013)
    OP_8C(0x0011, 180, 60)
    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_24(0x0075, 0x5A)
    Sleep(100)

    OP_24(0x0075, 0x50)
    Sleep(100)

    OP_24(0x0075, 0x46)
    Sleep(100)

    OP_24(0x0075, 0x3C)
    Sleep(100)

    OP_24(0x0075, 0x32)
    Sleep(100)

    OP_24(0x0075, 0x28)
    Sleep(100)

    OP_24(0x0075, 0x1E)
    Sleep(100)

    OP_24(0x0075, 0x14)
    Sleep(100)

    OP_24(0x0075, 0x0A)
    Sleep(100)

    OP_23(0x0075)
    WaitForThreadExit(0x0011, 0x0001)
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)

    OP_CE(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CE(
        0x03,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    NewScene('ED6_DT21/T4403._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x27D1
@scena.Code('func_0D_27D1')
def func_0D_27D1():
    Sleep(100)

    OP_99(0x00FE, 0x03, 0x00, 0x000005DC)
    SetChrChipByIndex(0x00FE, 12)
    OP_8E(0x00FE, 37120, 0, 59380, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 13)
    OP_99(0x00FE, 0x00, 0x03, 0x000005DC)
    SetChrSubChip(0x00FE, 3)

    Return()

# id: 0x000E offset: 0x2813
@scena.Code('func_0E_2813')
def func_0E_2813():
    Sleep(150)

    OP_99(0x00FE, 0x03, 0x00, 0x000005DC)
    SetChrChipByIndex(0x00FE, 12)
    OP_8E(0x00FE, 37210, 0, 50280, 2000, 0x00)
    OP_8E(0x00FE, 37250, 0, 50350, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 13)
    OP_99(0x00FE, 0x00, 0x03, 0x000005DC)
    SetChrSubChip(0x00FE, 3)

    Return()

# id: 0x000F offset: 0x2869
@scena.Code('func_0F_2869')
def func_0F_2869():
    OP_99(0x00FE, 0x03, 0x00, 0x000005DC)
    SetChrChipByIndex(0x00FE, 16)
    OP_8E(0x00FE, 37960, 0, 60040, 2000, 0x00)
    OP_8E(0x00FE, 38590, 0, 59990, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 17)
    OP_99(0x00FE, 0x00, 0x03, 0x000005DC)
    SetChrSubChip(0x00FE, 3)

    Return()

# id: 0x0010 offset: 0x28BA
@scena.Code('func_10_28BA')
def func_10_28BA():
    Sleep(50)

    OP_99(0x00FE, 0x03, 0x00, 0x000005DC)
    SetChrChipByIndex(0x00FE, 16)
    OP_8E(0x00FE, 37800, 0, 50240, 2000, 0x00)
    OP_8E(0x00FE, 38620, 0, 50370, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 17)
    OP_99(0x00FE, 0x00, 0x03, 0x000005DC)
    SetChrSubChip(0x00FE, 3)

    Return()

# id: 0x0011 offset: 0x2910
@scena.Code('func_11_2910')
def func_11_2910():
    OP_8F(0x00FE, 15560, 0, 48830, 4500, 0x00)
    OP_6F(0x000C, 21)
    OP_70(0x000C, 0x00000028)
    OP_8F(0x00FE, 14560, 0, 35000, 4500, 0x00)

    Return()

# id: 0x0012 offset: 0x2947
@scena.Code('func_12_2947')
def func_12_2947():
    OP_8F(0x00FE, 8580, 0, 26890, 4500, 0x00)
    OP_8F(0x00FE, 2380, 0, 25890, 4500, 0x00)

    Return()

# id: 0x0013 offset: 0x2970
@scena.Code('func_13_2970')
def func_13_2970():
    OP_8F(0x00FE, -970, 0, 19560, 4500, 0x00)
    OP_8F(0x00FE, -630, 0, -8770, 4500, 0x00)

    Return()

# id: 0x0014 offset: 0x2999
@scena.Code('func_14_2999')
def func_14_2999():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_2A13'),
        (0x00000001, 'loc_2A19'),
        (-1, 'loc_2A1F'),
    )

    def _loc_2A13(): pass

    label('loc_2A13')

    OP_A2(0x1200)

    Jump('loc_2A1F')

    def _loc_2A19(): pass

    label('loc_2A19')

    OP_A2(0x1201)

    Jump('loc_2A1F')

    def _loc_2A1F(): pass

    label('loc_2A1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2A2D',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    Jump('loc_2A31')

    def _loc_2A2D(): pass

    label('loc_2A2D')

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    def _loc_2A31(): pass

    label('loc_2A31')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
