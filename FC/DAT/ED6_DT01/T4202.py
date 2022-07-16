import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4202_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4202   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '艾莉茜雅女王'),
    TXT(0x02, '尤莉亚中尉'),
    TXT(0x03, '约修亚'),
    TXT(0x04, '奥利维尔'),
    TXT(0x05, '金'),
    TXT(0x06, '洛伦斯少尉'),
    TXT(0x07, '洛伦斯残像'),
    TXT(0x08, '洛伦斯残像'),
    TXT(0x09, '洛伦斯残像'),
    TXT(0x0A, '洛伦斯残像'),
    TXT(0x0B, '头盔'),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4202.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3501
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
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00480._CH', 'ED6_DT07/CH00480P._CP'),
        ('ED6_DT07/CH00482._CH', 'ED6_DT07/CH00482P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH00484._CH', 'ED6_DT07/CH00484P._CP'),
        ('ED6_DT07/CH00104._CH', 'ED6_DT07/CH00104P._CP'),
        ('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP'),
        ('ED6_DT07/CH00144._CH', 'ED6_DT07/CH00144P._CP'),
        ('ED6_DT06/CH20035._CH', 'ED6_DT06/CH20035P._CP'),
        ('ED6_DT06/CH20036._CH', 'ED6_DT06/CH20036P._CP'),
        ('ED6_DT06/CH20037._CH', 'ED6_DT06/CH20037P._CP'),
        ('ED6_DT06/CH20044._CH', 'ED6_DT06/CH20044P._CP'),
        ('ED6_DT07/CH00481._CH', 'ED6_DT07/CH00481P._CP'),
        ('ED6_DT07/CH00011._CH', 'ED6_DT07/CH00011P._CP'),
        ('ED6_DT07/CH00031._CH', 'ED6_DT07/CH00031P._CP'),
        ('ED6_DT07/CH00071._CH', 'ED6_DT07/CH00071P._CP'),
        ('ED6_DT06/CH20114._CH', 'ED6_DT06/CH20114P._CP'),
        ('ED6_DT06/CH20115._CH', 'ED6_DT06/CH20115P._CP'),
    ]

# id: 0x10002 offset: 0x18A
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
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 6,
            chipIndex           = 6,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2EA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2EA
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2F6'),
        (-1, 'loc_311'),
    )

    def _loc_2F6(): pass

    label('loc_2F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 6, 0x666)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 5, 0x665)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_30E',
    )

    PlaySE(451, 0x01, 0x64)
    SetScenaFlags(ScenaFlag(0x00CC, 6, 0x666))
    Event(0, 0x0002)

    def _loc_30E(): pass

    label('loc_30E')

    Jump('loc_311')

    def _loc_311(): pass

    label('loc_311')

    Return()

# id: 0x0001 offset: 0x312
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x39A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32F',
    )

    PlaySE(451, 0x01, 0x64)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_35C')

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_347',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_35C')

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_35C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_35C(): pass

    label('loc_35C')

    Return()

# id: 0x0002 offset: 0x35D
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    OP_28(0x004E, 0x01, 0x0008)
    CameraMove(2050, 12000, 54240, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(2400, 0)
    OP_6C(54000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0008, 2170, 12000, 62700, 0)
    SetChrPos(0x000D, 4110, 12000, 65390, 180)
    SetChrPos(0x0101, 1870, 12000, 45230, 0)
    SetChrPos(0x0105, 1870, 12000, 45230, 0)
    SetChrPos(0x0103, 1870, 12000, 45230, 0)
    SetChrChipByIndex(0x0101, 7)
    SetChrChipByIndex(0x0103, 9)
    SetChrChipByIndex(0x0105, 11)
    ChrSetRGBAMask(0x0105, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0103, 255, 255, 255, 0, 0)
    ClearMapFlags(0x00000800)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0445')
    def lambda_0445():
        CameraMove(1870, 12000, 56440, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0445)

    @scena.Lambda('lambda_045D')
    def lambda_045D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_045D)

    @scena.Lambda('lambda_046F')
    def lambda_046F():
        ChrWalkTo(0x00FE, 1840, 12000, 54630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_046F)

    Sleep(500)

    @scena.Lambda('lambda_048F')
    def lambda_048F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_048F)

    @scena.Lambda('lambda_04A1')
    def lambda_04A1():
        ChrWalkTo(0x00FE, 3020, 12000, 53420, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04A1)

    Sleep(500)

    @scena.Lambda('lambda_04C1')
    def lambda_04C1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_04C1)

    @scena.Lambda('lambda_04D3')
    def lambda_04D3():
        ChrWalkTo(0x00FE, 620, 12000, 53660, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_04D3)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_20(0x00000BB8)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0105,
        (
            '#0060131283V#043F祖母大人，您没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131284V#508F我们来救您了，女王陛下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 400)

    ChrTalk(
        0x0008,
        (
            '#0630131285V#093F科洛蒂娅……还有艾丝蒂尔……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '男人的声音',
        (
            '#0140131286V#4P总算来了啊……\n',
            '我已经等得有些不耐烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(81)

    @scena.Lambda('lambda_0617')
    def lambda_0617():
        ChrWalkTo(0x000D, 2770, 12000, 62440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0617)

    @scena.Lambda('lambda_0632')
    def lambda_0632():
        ChrTurnDirection(0x000D, 0x0105, 0)
        Yield()

        Jump('lambda_0632')

    DispatchAsync2(0x000D, 0x0001, lambda_0632)

    @scena.Lambda('lambda_0643')
    def lambda_0643():
        CameraMove(2100, 13150, 60270, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0643)

    @scena.Lambda('lambda_065B')
    def lambda_065B():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_065B)

    @scena.Lambda('lambda_066B')
    def lambda_066B():
        OP_6E(359, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_066B)

    @scena.Lambda('lambda_067B')
    def lambda_067B():
        OP_67(0, 6640, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_067B)

    @scena.Lambda('lambda_0693')
    def lambda_0693():
        CameraSetDistance(2300, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_0693)

    Sleep(800)

    @scena.Lambda('lambda_06A8')
    def lambda_06A8():
        ChrMoveTo(0x00FE, 2190, 12000, 63300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_06A8)

    Sleep(200)

    @scena.Lambda('lambda_06C8')
    def lambda_06C8():
        ChrWalkTo(0x00FE, 2110, 12000, 56770, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_06C8)

    Sleep(110)

    @scena.Lambda('lambda_06E8')
    def lambda_06E8():
        ChrWalkTo(0x00FE, 3360, 12000, 57270, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06E8)

    Sleep(100)

    @scena.Lambda('lambda_0708')
    def lambda_0708():
        ChrWalkTo(0x00FE, 640, 12000, 57460, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0708)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010131287V#580F洛、洛伦斯少尉！\n',
            '你为什么会在这种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000D, 0xFF)

    ChrTalk(
        0x000D,
        (
            '#0140131288V#280F#5P呵呵……\n',
            '我的任务是保护女王陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131289V出现在这里也没什么不可思议的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131290V#005F别开玩笑了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131291V不管你的实力有多强，\n',
            '我们这边可是有三个人哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131292V#023F怎么会，这个男人……\n',
            '身上散发出如此强烈的压迫感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131173V他究竟是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131294V#005F这个人就是情报部特务部队队长\n',
            '洛伦斯·博格少尉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131295V过去是猎兵团的一员，\n',
            '后来被理查德上校招入麾下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131296V#280F#5P哦，竟然调查到如此程度了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131297V不愧是Ｓ级游击士\n',
            '卡西乌斯·布莱特的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131298V#580F#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131299V#022F居然连从未向外界公布过的\n',
            '老师的级别也知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131300V这个男人，不是等闲之辈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131301V#280F#5P呵呵……\n',
            '你的事情我也很清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131302V级别Ｃ、外号『银闪』的\n',
            '雪拉扎德·哈维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131303V近日似乎就要升格为级别Ｂ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131304V#022F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131305V#043F对、对不起……\n',
            '请把祖母大人还给我好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131306V如果你只是被上校所雇佣的话，\n',
            '现在已经没有必要再战斗下去了啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131307V#280F#5P驱动着这个世界的，\n',
            '并非只有眼睛能够看到的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131308V就像只观察结晶回路的轮盘\n',
            '是无法知晓齿轮的运动一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131309V#044F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131310V#281F#5P听好了，科洛蒂娅公主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131311V所谓国家，\n',
            '就如同巨大而复杂的导力器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131312V人们如同身处其中、蕴含力量的结晶回路，\n',
            '组织、制度则是调动力量的齿轮……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131313V而将其包裹在一起的国土就是导力器的框架。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131314V对于这些知识，如果不能掌握，\n',
            '那你就没有资格成为一国之主的女王。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131315V#043F！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131316V#094F的确是相当形象的比喻啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131317V#090F而且……\n',
            '也许就像你所说的那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131318V真没有想到在这样的地方\n',
            '竟然能听到如此独到的国家论……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131319V#280F#5P呵呵……刚才献丑了。\n',
            '这些话对于陛下您来说似乎没有必要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131320V#007F虽然不太明白是怎么一回事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131321V#002F不过看起来，\n',
            '你没有打算要释放女王陛下的意思吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131322V#280F#5P就算如此……你们又能怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131323V#005F那还用说……\n',
            '拼尽全力也要救回女王陛下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131324V#024F没错……\n',
            '既然到了这里，就没有退缩的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131325V#049F虽然从你身上感觉不到什么敌意……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131326V#042F但是，为了将祖母大人救回来，\n',
            '我会毫不犹豫向你出剑的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131327V#280F#5P呵呵，不错啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131328V既然这样的话，\n',
            '我也要拿出一些真正的实力来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131329V#004F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    SetChrFlags(0x000D, 0x0020)
    SetChrFlags(0x000D, 0x0002)
    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000D, 18)

    @scena.Lambda('lambda_0FCB')
    def lambda_0FCB():
        OP_99(0x00FE, 0x00, 0x01, 1000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0FCB)

    Sleep(500)

    SetChrFlags(0x0012, 0x0020)
    SetChrFlags(0x0012, 0x0002)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0012, 0x0040)
    SetChrSubChip(0x0012, 0)
    SetChrPos(0x0012, 3300, 12300, 62320, 0)
    OP_99(0x000D, 0x01, 0x04, 1300)
    ClearChrFlags(0x0012, 0x0080)

    @scena.Lambda('lambda_1018')
    def lambda_1018():
        OP_99(0x00FE, 0x05, 0x07, 1300)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1018)

    ChrWalkTo(0x0012, 3500, 12000, 62220, 5000, 0x00)
    PlaySE(177, 0x00, 0x64)

    @scena.Lambda('lambda_1041')
    def lambda_1041():
        OP_99(0x00FE, 0x00, 0x07, 1200)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1041)

    ChrJumpTo(0x0012, 5120, 12000, 61840, 700, 1500)
    ChrJumpTo(0x0012, 5840, 12000, 61520, 400, 1500)

    @scena.Lambda('lambda_107F')
    def lambda_107F():
        OP_99(0x00FE, 0x00, 0x07, 1300)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_107F)

    ChrWalkTo(0x0012, 6500, 12000, 61300, 700, 0x00)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0140131330V#284F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131331V#580F……银发……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131332V#022F不对………………\n',
            '……是苍金色……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131333V这个男人……\n',
            '看起来应该是北方出生的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131334V#285F#5P呵呵……\n',
            '没错，的确是北方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131335V不过离这里也不算非常的远。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131336V#043F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(43)

    @scena.Lambda('lambda_11C0')
    def lambda_11C0():
        CameraSetDistance(2000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11C0)

    Sleep(500)

    Fade(500)
    ClearChrFlags(0x000D, 0x0002)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000D, 6)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0140131337V#286F#5P虽然你们是女性，\n',
            '但我也没打算要手下留情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131338V#283F……接招。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000D, 0x0020)
    SetChrChipByIndex(0x000D, 22)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1262')
    def lambda_1262():
        OP_92(0x00FE, 0x0105, 1000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1262)

    @scena.Lambda('lambda_1277')
    def lambda_1277():
        CameraMove(2100, 13150, 57270, 500)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1277)

    Sleep(400)

    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0105, 0xFF)
    SetChrFlags(0x000D, 0x0020)
    Battle(0x0000039A, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrPos(0x0101, 3360, 12000, 57270, 0)
    SetChrPos(0x0105, 2110, 12000, 56770, 0)
    SetChrPos(0x0103, 640, 12000, 57460, 0)
    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000D, 5)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_12FB'),
        (-1, 'loc_179D'),
    )

    def _loc_12FB(): pass

    label('loc_12FB')

    WaitEffect(0x16, 0x00)
    LoadEffect(0x00, 'monster\\\\msc0280.eff')
    OP_28(0x004E, 0x01, 0x0010)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000D, 14)
    SetChrPos(0x000D, 2220, 12000, 61180, 180)
    OP_2B(0x004D, 0x0003)
    CameraSetDistance(2300, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0140131339V#286F#5P真令人吃惊啊……\n',
            '没想到你们可以达到如此程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131340V#582F呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131341V#005F你、你这家伙！\n',
            '当初决赛的时候没有尽全力吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131342V和那时相比，简直强悍得判若两人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131343V#522F竟、竟然可以打败这样的怪物……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131344V#049F的、的确难以置信啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131345V#284F#5P艾丝蒂尔·布莱特……\n',
            '刚才对你太过轻视，在下深表歉意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131346V你如果能继续这么走下去……\n',
            '达到你父亲那种境界也未尝不可。　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131347V#004F什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131348V#285F#5P不过……现在还有一定差距。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_154E')
    def lambda_154E():
        CameraMove(2400, 12000, 57540, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_154E)

    OP_99(0x000D, 0x03, 0x00, 2000)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000D, 6)
    ChrSetRGBAMask(0x000E, 255, 255, 255, 200, 0)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 150, 0)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 100, 0)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 50, 0)
    SetChrPos(0x000E, 2220, 12000, 61180, 180)
    SetChrPos(0x000F, 2220, 12000, 61180, 180)
    SetChrPos(0x0010, 2220, 12000, 61180, 180)
    SetChrPos(0x0011, 2220, 12000, 61180, 180)
    CreateThread(0x000D, 0x01, 0x00, 0x0005)
    Sleep(90)

    CreateThread(0x000E, 0x01, 0x00, 0x0004)
    Sleep(90)

    CreateThread(0x000F, 0x01, 0x00, 0x0004)
    Sleep(90)

    CreateThread(0x0010, 0x01, 0x00, 0x0004)
    Sleep(90)

    CreateThread(0x0011, 0x01, 0x00, 0x0004)
    OP_A6(0x0000)

    @scena.Lambda('lambda_1629')
    def lambda_1629():
        OP_67(0, 7820, -10000, 700)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1629)

    @scena.Lambda('lambda_1641')
    def lambda_1641():
        OP_6C(24000, 700)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1641)

    OP_A6(0x0001)
    Sleep(130)

    PlayEffect(0x00, 0xFF, 0x00FF, 2360, 12050, 57260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_A6(0x0002)

    ExecExpressionWithValue(
        0x0105,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0105, 17)
    ChrTurnDirection(0x0105, 0x000D, 0)

    @scena.Lambda('lambda_16A8')
    def lambda_16A8():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_16A8)

    @scena.Lambda('lambda_16BE')
    def lambda_16BE():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_16BE)

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0103, 16)
    ChrTurnDirection(0x0103, 0x000D, 0)

    @scena.Lambda('lambda_16E5')
    def lambda_16E5():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_16E5)

    @scena.Lambda('lambda_16FB')
    def lambda_16FB():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_16FB)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0101, 15)
    ChrTurnDirection(0x0101, 0x000D, 0)

    @scena.Lambda('lambda_1722')
    def lambda_1722():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1722)

    @scena.Lambda('lambda_1738')
    def lambda_1738():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1738)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#504F#2P#8A啊啊！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0103,
        (
            '#523F#8A呜……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0105,
        (
            '#0060131351V#541F#8A呀啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(2500)

    Jump('loc_1985')

    def _loc_179D(): pass

    label('loc_179D')

    OP_28(0x004E, 0x01, 0x0020)
    OP_6C(24000, 0)
    OP_67(0, 7820, -10000, 0)
    CameraMove(2400, 12000, 57540, 0)
    CameraSetDistance(2300, 0)
    SetChrChipByIndex(0x0105, 17)
    SetChrChipByIndex(0x0103, 16)
    SetChrChipByIndex(0x0101, 15)
    SetChrSubChip(0x0105, 2)
    SetChrSubChip(0x0103, 2)
    SetChrSubChip(0x0101, 2)
    SetChrPos(0x000D, 1970, 12000, 58030, 182)
    SetChrPos(0x0105, 1500, 12000, 55600, 359)
    SetChrPos(0x0103, -500, 12000, 57130, 49)
    SetChrPos(0x0101, 4000, 12000, 56700, 290)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0140131352V#284F#5P……真让人失望。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131353V原本还以为能有场势均力敌的战斗……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131354V#581F#4P为、为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131355V和当初的决赛相比简直判若两人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131356V#522F……可能那时候\n',
            '他根本还没有出尽全力吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131357V如此强大的力量……\n',
            '或许已经可以和老师匹敌了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131358V#049F祖母大人……\n',
            '……对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1985')

    def _loc_1985(): pass

    label('loc_1985')

    ChrTalk(
        0x0008,
        (
            '#0630131359V#095F#6P科洛蒂娅！艾丝蒂尔！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_19B7')
    def lambda_19B7():
        ChrWalkTo(0x00FE, 1780, 12000, 61930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_19B7)

    Sleep(200)

    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)

    @scena.Lambda('lambda_19EB')
    def lambda_19EB():
        CameraMove(2150, 12000, 59650, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19EB)

    SetChrDirection(0x000D, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000D,
        (
            '#0140131360V#284F#4P陛下，请少安毋躁。\n',
            '我只是让她们暂时不能动而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131361V并没有生命危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131362V#093F#5P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131363V那双眼眸……\n',
            '为何会有那么深邃的颜色呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131364V明明还如此年轻……\n',
            '可却好像经历过巨大的苦难一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131365V#283F#4P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131366V#286F女王啊，\n',
            '您并没有怜悯我的资格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131367V对于『哈梅尔』这个名字，\n',
            '我想您应该不会感到陌生吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0630131368V#097F#5P#3S！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0105, 400)

    @scena.Lambda('lambda_1BD2')
    def lambda_1BD2():
        ChrTurnDirection(0x00FE, 0x0105, 0)
        Yield()

        Jump('lambda_1BD2')

    DispatchAsync2(0x000D, 0x0001, lambda_1BD2)

    @scena.Lambda('lambda_1BE3')
    def lambda_1BE3():
        CameraMove(2150, 12000, 61000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1BE3)

    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x000D, 2830, 12000, 61950, 500, 5000)
    ChrTurnDirection(0x0008, 0x000D, 400)
    ChrTurnDirection(0x0105, 0x000D, 0)

    @scena.Lambda('lambda_1C25')
    def lambda_1C25():
        OP_99(0x0105, 0x03, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1C25)

    Sleep(100)

    ChrTurnDirection(0x0101, 0x000D, 0)

    @scena.Lambda('lambda_1C41')
    def lambda_1C41():
        OP_99(0x0101, 0x03, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C41)

    Sleep(100)

    ChrTurnDirection(0x0103, 0x000D, 0)

    @scena.Lambda('lambda_1C5D')
    def lambda_1C5D():
        OP_99(0x0103, 0x03, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1C5D)

    WaitForThreadExit(0x0105, 0x0001)
    SetChrChipByIndex(0x0105, 11)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrChipByIndex(0x0101, 7)
    WaitForThreadExit(0x0103, 0x0001)
    SetChrChipByIndex(0x0103, 9)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000D,
        (
            '#0140131369V#285F好了，差不多是时候了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131370V如大家所愿，\n',
            '我将女王完好奉还给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000D, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010131371V#580F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131372V#286F如果还想阻止上校的话，\n',
            '劝你们赶快前往地下去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131373V虽然可能已经来不及了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131374V不过也许还能减少无谓的伤亡。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131375V#092F#3P地下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131376V难道是说从那个地方降落到地下？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0140131377V#285F呵呵……现在的您对其中的含义，\n',
            '应该是清楚得不能再清楚了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131378V为他们指引前进的道路吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131379V#286F……那么，再会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\evsepith.eff')

    @scena.Lambda('lambda_1E79')
    def lambda_1E79():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_1E79')

    DispatchAsync2(0x0008, 0x0001, lambda_1E79)

    ClearChrFlags(0x000D, 0x0020)
    SetChrFlags(0x000D, 0x0004)

    @scena.Lambda('lambda_1E94')
    def lambda_1E94():
        CameraMove(1740, 12000, 71200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1E94)

    @scena.Lambda('lambda_1EAC')
    def lambda_1EAC():
        OP_6E(359, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EAC)

    @scena.Lambda('lambda_1EBC')
    def lambda_1EBC():
        OP_67(0, 6450, -10000, 2500)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_1EBC)

    @scena.Lambda('lambda_1ED4')
    def lambda_1ED4():
        OP_6C(90000, 2500)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1ED4)

    OP_20(0x000005DC)
    SetChrFlags(0x000D, 0x0020)
    SetChrDirection(0x000D, 0, 600)
    ClearChrFlags(0x000D, 0x0020)
    ChrSetRGBAMask(0x000E, 255, 255, 255, 120, 0)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 100, 0)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 80, 0)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 60, 0)
    SetChrPos(0x000E, 2830, 12000, 61950, 0)
    SetChrPos(0x000F, 2830, 12000, 61950, 0)
    SetChrPos(0x0010, 2830, 12000, 61950, 0)
    SetChrPos(0x0011, 2830, 12000, 61950, 0)
    CreateThread(0x000D, 0x00, 0x00, 0x0007)
    Sleep(150)

    CreateThread(0x000E, 0x00, 0x00, 0x0006)
    Sleep(150)

    CreateThread(0x000F, 0x00, 0x00, 0x0006)
    Sleep(150)

    CreateThread(0x0010, 0x00, 0x00, 0x0006)
    Sleep(150)

    CreateThread(0x0011, 0x00, 0x00, 0x0006)

    @scena.Lambda('lambda_1FA1')
    def lambda_1FA1():
        OP_6C(110000, 2500)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1FA1)

    Sleep(1100)

    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x0010, 0x00)
    TerminateThread(0x0011, 0x00)
    SetChrPos(0x0101, 4270, 12000, 59160, 0)
    SetChrPos(0x0105, 1920, 12000, 58210, 0)
    SetChrPos(0x0103, 10, 12000, 59190, 0)
    Sleep(3000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_200B')
    def lambda_200B():
        CameraMove(2090, 12000, 65720, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_200B)

    @scena.Lambda('lambda_2023')
    def lambda_2023():
        CameraSetDistance(2840, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2023)

    @scena.Lambda('lambda_2033')
    def lambda_2033():
        OP_6C(129000, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2033)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010131380V#005F#3P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_2075')
    def lambda_2075():
        ChrWalkTo(0x00FE, 3820, 12000, 67150, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2075)

    ChrTalk(
        0x0103,
        (
            '#0030131381V#024F#3P来、来真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0103, 65535)

    @scena.Lambda('lambda_20C8')
    def lambda_20C8():
        ChrWalkTo(0x00FE, 750, 12000, 67290, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_20C8)

    Sleep(500)

    ExecExpressionWithValue(
        0x0105,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0105, 65535)

    @scena.Lambda('lambda_20F8')
    def lambda_20F8():
        ChrWalkTo(0x00FE, 1770, 12000, 60750, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_20F8)

    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_2118')
    def lambda_2118():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2118)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010131382V#580F不、不见了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131383V跳到湖里去了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0103, 0x0001)

    ChrTalk(
        0x0103,
        (
            '#0030131384V#022F尽管真的跳了下去……\n',
            '但是，湖面并没有任何波痕啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131385V那个男人，究竟是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131386V#043F祖母大人……\n',
            '您没有受伤吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131387V#090F#6P我很好，科洛蒂娅。\n',
            '他由始至终都没有伤害过我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131388V#094F而且……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrPos(0x000B, 1870, 12000, 45230, 0)
    SetChrPos(0x000A, 1870, 12000, 45230, 0)
    SetChrPos(0x000C, 1870, 12000, 45230, 0)
    SetChrPos(0x0009, 1870, 12000, 45230, 0)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)

    NpcTalk(
        0x000A,
        '少年的声音',
        (
            '#0020131389V#3P艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(17)

    @scena.Lambda('lambda_2313')
    def lambda_2313():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2313)

    @scena.Lambda('lambda_2321')
    def lambda_2321():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2321)

    @scena.Lambda('lambda_232F')
    def lambda_232F():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_232F)

    @scena.Lambda('lambda_233D')
    def lambda_233D():
        CameraMove(2540, 12000, 61390, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_233D)

    @scena.Lambda('lambda_2355')
    def lambda_2355():
        OP_67(0, 9350, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2355)

    @scena.Lambda('lambda_236D')
    def lambda_236D():
        CameraSetDistance(2500, 4000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_236D)

    CreateThread(0x000D, 0x01, 0x00, 0x0003)
    SetChrChipByIndex(0x000A, 23)

    @scena.Lambda('lambda_2389')
    def lambda_2389():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2389)

    @scena.Lambda('lambda_239B')
    def lambda_239B():
        ChrWalkTo(0x00FE, 3370, 12000, 58260, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_239B)

    Sleep(500)

    SetChrChipByIndex(0x0009, 26)

    @scena.Lambda('lambda_23C0')
    def lambda_23C0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_23C0)

    @scena.Lambda('lambda_23D2')
    def lambda_23D2():
        ChrWalkTo(0x00FE, 2000, 12000, 59510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_23D2)

    Sleep(500)

    SetChrChipByIndex(0x000B, 24)

    @scena.Lambda('lambda_23F7')
    def lambda_23F7():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_23F7')

    DispatchAsync2(0x000B, 0x0001, lambda_23F7)

    @scena.Lambda('lambda_2408')
    def lambda_2408():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2408)

    @scena.Lambda('lambda_241A')
    def lambda_241A():
        ChrWalkTo(0x00FE, 2070, 12000, 57860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_241A)

    Sleep(500)

    SetChrChipByIndex(0x000C, 25)

    @scena.Lambda('lambda_243F')
    def lambda_243F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_243F')

    DispatchAsync2(0x000C, 0x0001, lambda_243F)

    @scena.Lambda('lambda_2450')
    def lambda_2450():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2450)

    @scena.Lambda('lambda_2462')
    def lambda_2462():
        ChrWalkTo(0x00FE, 710, 12000, 58440, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_2462)

    @scena.Lambda('lambda_247D')
    def lambda_247D():
        ChrWalkTo(0x00FE, 3570, 12000, 59430, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_247D)

    Sleep(500)

    @scena.Lambda('lambda_249D')
    def lambda_249D():
        ChrWalkTo(0x00FE, 150, 12000, 60340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_249D)

    @scena.Lambda('lambda_24B8')
    def lambda_24B8():
        CameraMove(2140, 12000, 59300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_24B8)

    @scena.Lambda('lambda_24D0')
    def lambda_24D0():
        OP_6E(307, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_24D0)

    SetChrFlags(0x0105, 0x0040)
    ChrWalkTo(0x0105, 2850, 12000, 61440, 2000, 0x00)
    ChrTurnDirection(0x0105, 0x0009, 400)
    WaitForThreadExit(0x0103, 0x0001)

    @scena.Lambda('lambda_2505')
    def lambda_2505():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2505)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010131390V#004F约修亚！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131391V#001F太好了，你平安无事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131392V#010F#2P艾丝蒂尔你这边也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131393V因为上校和少尉都没有在城内，\n',
            '所以我很担心你们这里的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131394V#505F那个戴红色头盔的洛伦斯少尉\n',
            '倒是刚才还在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131395V#014F#2P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131396V#522F那个男人从栏杆那里一跃而下，\n',
            '已经逃得无影无踪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131397V#025F简直是个超乎常人的怪物啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131398V#013F#2P哦，原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131399V#015F总之，大家能平安无事……\n',
            '这已经是最好的结局了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111389V#008F约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0009, 1)
    ChrWalkTo(0x0009, 1840, 12000, 60370, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0100131401V#171F#2P陛下……幸好您没事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131402V#091F尤莉亚中尉……\n',
            '能再见到你我真的很高兴呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131403V#090F而且，各位朋友……\n',
            '我对你们的感激也是一言难尽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_27D2')
    def lambda_27D2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27D2)

    @scena.Lambda('lambda_27E0')
    def lambda_27E0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_27E0)

    @scena.Lambda('lambda_27EE')
    def lambda_27EE():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_27EE)

    @scena.Lambda('lambda_27FC')
    def lambda_27FC():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_27FC)

    @scena.Lambda('lambda_280A')
    def lambda_280A():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_280A)

    @scena.Lambda('lambda_2818')
    def lambda_2818():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2818)

    ChrTalk(
        0x000B,
        (
            '#0040131404V#031F#2P呵呵，女王陛下。\n',
            '非常荣幸能得到您的赞美之词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080131405V#070F#2P能够为您效劳，我已深感荣幸了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131406V#074F不过现在还没有到结束的时候。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100131407V#175F#2P虽然我们已经镇压了城内的特务兵，\n',
            '但是，又传来了不利的消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131408V各地的正规军部队正朝着王都方向攻来……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131409V他们很可能是被情报部给操控了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131410V#093F是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100131411V#178F#2P虽然很抱歉，不过已经没时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131412V陛下，请您乘坐飞艇从这里离开吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131413V#094F不行……我办不到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131414V#092F因为更为严重的是……\n',
            '一场可怕的灾难可能就要发生了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131415V所以，当务之急……\n',
            '无论如何也要阻止理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100131416V#173F#2P怎、怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_20(0x000003E8)
    Fade(1000)
    CameraMove(2200, 12000, 60780, 0)
    OP_67(0, 6870, -10000, 0)
    CameraSetDistance(2650, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0105, 3190, 12000, 60950, 270)
    OP_21()
    OP_0D()
    PlayBGM(33)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0630131417V#093F昨夜，我和上校长谈了一番，\n',
            '终于明白他发动政变的真正目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131418V他好像企图把『辉之环』据为己有。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131419V#004F『辉之环』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131420V好、好像在哪听说过这个东西……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131421V#015F#2P那是空之女神赐予古代人的\n',
            '『七至宝』之一……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131422V#012F可以支配世间一切的传说中的古代遗物。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131423V#505F哦，是亚鲁瓦教授说过的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131424V可那只是教会流传下来的故事啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131425V#094F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130273V#580F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040131427V#032F嗯，应该存在吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131428V在这个利贝尔王国的某处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131429V#093F王室中也有这么一个古老的传说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131430V#094F『辉之环，总有一天会带来灾难，\n',
            '　将人类之子的灵魂与炼狱相接。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131431V『吾等，为了作为人而存在，\n',
            '　将其封印在昏暗的狭间……』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080131432V#074F『将人类之子的灵魂与炼狱相接』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131433V#072F实在是……令人感到可怕的说法啊。　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131434V#092F这些箴言……\n',
            '作为戒律由代代的国王相传至今。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131435V那个被称作『辉之环』的物品\n',
            '恐怕具有相当的危险性，\n',
            '因此，王家的先祖们将其封印了起来。  ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131436V而且，以前在王都的地下\n',
            '还检测出了巨大的导力反应……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131437V如果把这两者结合起来考虑的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131438V#012F#2P那么就可以推断出……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131439V王都的地下封印着『辉之环』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131440V#093F是啊……\n',
            '上校肯定也是这么推断的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131441V『辉之环』究竟是什么样的东西，\n',
            '这一点并没有被传承下来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131442V一旦该物品被人唤醒，\n',
            '说不定会发生十分可怕的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131443V也许，甚至能和过去所发生的\n',
            '传说中的『大崩坏』匹敌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131444V#043F怎、怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131445V#522F没有想到，竟然会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131446V#002F女王陛下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131447V那个洛伦斯少尉刚才说过\n',
            '『前往地下去吧』之类的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131448V那是代表什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131449V#094F在这个格兰赛尔城里有\n',
            '一间奇怪的房间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131450V是一个什么东西也不保管，\n',
            '而且从很久以前就禁止入内的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131451V#044F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100131452V#172F是宝物库吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_28(0x004E, 0x01, 0x0040)
    OP_28(0x004E, 0x01, 0x0080)
    OP_28(0x004E, 0x01, 0x0100)
    OP_28(0x004E, 0x01, 0x0200)
    OP_28(0x004E, 0x01, 0x0400)
    OP_28(0x004F, 0x04, 0x02)
    OP_28(0x004F, 0x04, 0x04)
    SetMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4240._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x3241
@scena.Code('func_03_3241')
def func_03_3241():
    WaitForThreadExit(0x000A, 0x0001)
    SetChrChipByIndex(0x000A, 2)
    WaitForThreadExit(0x0009, 0x0001)
    SetChrSubChip(0x0009, 1)
    SetChrChipByIndex(0x0009, 27)
    WaitForThreadExit(0x000B, 0x0003)
    SetChrChipByIndex(0x000B, 3)
    WaitForThreadExit(0x000C, 0x0003)
    SetChrChipByIndex(0x000C, 4)

    Return()

# id: 0x0004 offset: 0x326F
@scena.Code('func_04_326F')
def func_04_326F():
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    ChrJumpTo(0x00FE, 2110, 12000, 60200, 400, 6000)
    SetChrChipByIndex(0x00FE, 6)

    @scena.Lambda('lambda_32A5')
    def lambda_32A5():
        OP_99(0x00FE, 0x00, 0x01, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_32A5)

    ChrJumpTo(0x00FE, 1950, 15000, 59050, 3000, 8000)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearChrFlags(0x00FE, 0x0400)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    @scena.Lambda('lambda_32DC')
    def lambda_32DC():
        OP_99(0x00FE, 0x02, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_32DC)

    ChrJumpTo(0x00FE, 1860, 12000, 57860, 0, 15000)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    Sleep(2000)

    @scena.Lambda('lambda_330B')
    def lambda_330B():
        OP_99(0x00FE, 0x03, 0x0B, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_330B)

    Return()

# id: 0x0005 offset: 0x3316
@scena.Code('func_05_3316')
def func_05_3316():
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    ChrJumpTo(0x00FE, 2110, 12000, 60200, 400, 6000)
    SetChrChipByIndex(0x00FE, 6)

    @scena.Lambda('lambda_334C')
    def lambda_334C():
        OP_99(0x00FE, 0x00, 0x01, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_334C)

    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x00FE, 1950, 15000, 59050, 3000, 8000)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearChrFlags(0x00FE, 0x0400)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    @scena.Lambda('lambda_3388')
    def lambda_3388():
        OP_99(0x00FE, 0x02, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3388)

    ChrJumpTo(0x00FE, 1860, 12000, 57860, 0, 15000)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    Sleep(2000)

    @scena.Lambda('lambda_33B7')
    def lambda_33B7():
        OP_99(0x00FE, 0x03, 0x0B, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_33B7)

    Return()

# id: 0x0006 offset: 0x33C2
@scena.Code('func_06_33C2')
def func_06_33C2():
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 19)
    ChrWalkTo(0x00FE, 2450, 12000, 63010, 6000, 0x00)
    ChrWalkTo(0x00FE, 1890, 12000, 65120, 6000, 0x00)
    ChrJumpTo(0x00FE, 2040, 12390, 67720, 800, 3500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x00FE, 20)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_342E')
    def lambda_342E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_342E)

    ChrJumpTo(0x00FE, 1850, 4500, 78500, 1000, 4000)

    Return()

# id: 0x0007 offset: 0x3452
@scena.Code('func_07_3452')
def func_07_3452():
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 19)
    ChrWalkTo(0x00FE, 2450, 12000, 63010, 6000, 0x00)
    ChrWalkTo(0x00FE, 1890, 12000, 65120, 6000, 0x00)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x00FE, 2040, 12390, 67720, 800, 3500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x00FE, 20)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_34C3')
    def lambda_34C3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_34C3)

    PlaySE(163, 0x00, 0x64)
    PlaySE(153, 0x00, 0x64)
    ChrJumpTo(0x00FE, 1850, 4500, 78500, 1000, 4000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
