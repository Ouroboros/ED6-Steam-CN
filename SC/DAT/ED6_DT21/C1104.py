import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1104_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1104   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '小丑肯帕雷拉'),
    TXT(0x02, '凯文神父'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '特务兵'),
    TXT(0x05, '特务兵'),
    TXT(0x06, '特务兵'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1104.x'
    header.mapIndex       = 49
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5001
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
        ('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT27/CH03095._CH', 'ED6_DT27/CH03095P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT07/CH00424._CH', 'ED6_DT07/CH00424P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT26/CH20299._CH', 'ED6_DT26/CH20299P._CP'),
        ('ED6_DT26/CH20300._CH', 'ED6_DT26/CH20300P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00153._CH', 'ED6_DT07/CH00153P._CP'),
        ('ED6_DT07/CH00423._CH', 'ED6_DT07/CH00423P._CP'),
        ('ED6_DT07/CH00055._CH', 'ED6_DT07/CH00055P._CP'),
        ('ED6_DT07/CH00025._CH', 'ED6_DT07/CH00025P._CP'),
        ('ED6_DT26/CH20298._CH', 'ED6_DT26/CH20298P._CP'),
        ('ED6_DT26/CH20305._CH', 'ED6_DT26/CH20305P._CP'),
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
            dword_10            = 18,
            chipIndex           = 18,
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
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x24A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x24A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x24A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x24A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_25D',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0003)

    def _loc_25D(): pass

    label('loc_25D')

    Return()

# id: 0x0001 offset: 0x25E
@scena.Code('Init')
def Init():
    OP_22(0x010E, 0x01, 0x5A)

    Return()

# id: 0x0002 offset: 0x264
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_279',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_279(): pass

    label('loc_279')

    Return()

# id: 0x0003 offset: 0x27A
@scena.Code('func_03_27A')
def func_03_27A():
    EventBegin(0x00)
    OP_DB()
    OP_E8(0xDC, 0x05, 0x00, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_291',
    )

    FormationReset()
    FormationAddMember(ChrTable['阿加特'], 0xF6, 0xFF)

    Jump('loc_296')

    def _loc_291(): pass

    label('loc_291')

    FormationReset()
    FormationAddMember(ChrTable['雪拉扎德'], 0xF6, 0xFF)

    def _loc_296(): pass

    label('loc_296')

    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    OP_6D(-330, 0, 3610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(45000, 0)
    OP_6E(547, 0)
    SetChrPos(0x00F6, 4590, 0, -23390, 333)
    SetChrPos(0x010A, 3790, 50, -24060, 333)
    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_0309')
    def lambda_0309():
        OP_6D(3640, 130, -22260, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0309)

    @scena.Lambda('lambda_0321')
    def lambda_0321():
        OP_67(0, 10920, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0321)

    @scena.Lambda('lambda_0339')
    def lambda_0339():
        OP_6B(2240, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0339)

    @scena.Lambda('lambda_0349')
    def lambda_0349():
        OP_6E(262, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0349)

    OP_6C(3000, 8000)
    Sleep(500)

    OP_DC()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_47A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260025V#552F#2P真奇怪啊……\n',
            '明明是预想中的基地……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260026V但感觉不到有人的气息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260027V#1317F是、是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260028V刚才的士兵们\n',
            '去了哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260029V#053F#2P哼，搞不好\n',
            '被察觉了也说不定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260030V#050F不管了，赶快调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_59B')

    def _loc_47A(): pass

    label('loc_47A')

    ChrTalk(
        0x0103,
        (
            '#0030260031V#022F#2P真是奇怪呢……\n',
            '似乎如预料一般是座大本营……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260032V但感觉不到有人存在的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260027V#1317F是、是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260028V刚才的士兵们\n',
            '去了哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260035V#026F#2P那么……\n',
            '是被察觉了，还是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260036V#027F算了。\n',
            '总之还是慎重进行调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_59B(): pass

    label('loc_59B')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetChrPos(0x00F6, 1180, 0, -470, 90)
    SetChrPos(0x010A, -6500, 0, 5600, 180)
    OP_6D(-2610, 0, -760, 0)
    OP_67(0, 9420, -10000, 0)
    OP_6B(1730, 0)
    OP_6C(45000, 0)
    OP_6E(449, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0619')
    def lambda_0619():
        OP_6B(1400, 4000)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0619)

    @scena.Lambda('lambda_0629')
    def lambda_0629():
        OP_8F(0x00FE, -3360, 0, -1060, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_0629)

    Sleep(1500)

    OP_8C(0x00F6, 270, 400)

    @scena.Lambda('lambda_0650')
    def lambda_0650():
        OP_8E(0x00FE, -1840, 0, -1210, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F6, 0x0000, lambda_0650)

    WaitForThreadExit(0x010A, 0x0000)
    OP_8C(0x010A, 90, 400)
    WaitForThreadExit(0x00F6, 0x0000)
    WaitForThreadExit(0x010A, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_124D',
    )

    ChrTalk(
        0x010A,
        (
            '#0120260037V#1316F#6P不行啊。\n',
            '感觉像是人去楼空的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260038V#818F前辈那边怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260039V#555F这边也是一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260040V是出去了呢，还是\n',
            '刚转移据点了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260041V哪怕能发现一些\n',
            '线索也好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260042V#810F#6P不过，好像没有\n',
            '任何有关他们去向的线索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260043V不过在那边的帐篷\n',
            '发现了这个文件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260044V#052F哦，我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x010A, 0x00F6, 0x00000320, 0x000005DC, 0x00)
    Sleep(500)

    OP_8F(0x010A, -3360, 0, -1060, 1500, 0x00)
    Sleep(500)

    FadeOut(300, 0, 100)
    OP_AD(0x00240112, 0x00BE, 0x0096, 0x000001F4)
    Sleep(3000)

    OP_AE(0x000001F4)
    FadeIn(300, 0)
    Sleep(1500)

    ChrTalk(
        0x0106,
        (
            '#0050260045V#555F这是什么……\n',
            '画着奇怪的图案啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260046V『奥尔杰尤』开发计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260047V好像是什么交通工具的设计图啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260048V#810F#6P『奥尔杰尤』……\n',
            '略微有点华丽的名字呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260049V是飞船吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260050V#053F这个，我是门外汉\n',
            '不大清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050260051V#052F……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260052V#814F#6P怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260053V#555F书页之间\n',
            '夹着一张纸条。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260054V『请帖发送完毕了。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260055V『桌椅也准备好了。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260056V『这样一来茶会的准备就完成了。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260057V『只剩下烤点心\n',
            '和等待客人到齐了。』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260058V#1310F#6P哦～\n',
            '内容听起来很温暖呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260059V#811F感觉像是图画书中的一段文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260060V#053F唔……\n',
            '反正是什么密码吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260061V#552F问题是这个讯息\n',
            '到底意味着什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050260062V#054F#4S散开！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260063V#814F#6P咦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp003_00.eff')
    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -4210, 0, -6050, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -3380, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -3300, 0, -2370, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x0106, 7)
    SetChrChipByIndex(0x010A, 11)

    @scena.Lambda('lambda_0C9B')
    def lambda_0C9B():
        OP_96(0x00FE, 0xFFFFFC22, 0x00000000, 0xFFFFFA06, 0x0000012C, 0x00001770)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0C9B)

    @scena.Lambda('lambda_0CB9')
    def lambda_0CB9():
        OP_96(0x00FE, 0xFFFFEE30, 0x00000000, 0xFFFFFB28, 0x0000012C, 0x00001770)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0CB9)

    Sleep(100)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -2300, 0, -1090, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    @scena.Lambda('lambda_0D1B')
    def lambda_0D1B():
        OP_8C(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_0D1B)

    @scena.Lambda('lambda_0D29')
    def lambda_0D29():
        OP_8C(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_0D29)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -2540, 0, 130, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -2000, 0, 1320, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    Sleep(500)

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000A, -11440, 0, -1180, 90)
    SetChrPos(0x000B, 7610, 0, -2040, 270)
    SetChrPos(0x000C, -3650, 0, -10100, 0)
    SetChrChipByIndex(0x000A, 17)
    SetChrChipByIndex(0x000B, 17)
    SetChrChipByIndex(0x000C, 18)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)

    @scena.Lambda('lambda_0E1A')
    def lambda_0E1A():
        OP_6D(-3470, 0, -1890, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_0E1A)

    @scena.Lambda('lambda_0E32')
    def lambda_0E32():
        OP_67(0, 8380, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0E32)

    @scena.Lambda('lambda_0E4A')
    def lambda_0E4A():
        OP_6B(2100, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_0E4A)

    @scena.Lambda('lambda_0E5A')
    def lambda_0E5A():
        OP_6E(501, 3000)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_0E5A)

    WaitForThreadExit(0x0106, 0x0000)
    WaitForThreadExit(0x0106, 0x0001)
    WaitForThreadExit(0x0106, 0x0002)
    OP_8C(0x0106, 90, 400)
    OP_8C(0x010A, 270, 400)

    ChrTalk(
        0x010A,
        (
            '#0120260064V#1317F#6P骗人……什么时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260065V#051F#5P哼，好巧妙的\n',
            '让人放松警惕的方法啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260066V跟那个红头盔少尉学的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1K#2P…………………',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000B,
        (
            '#1K#6P…………………',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000C,
        (
            '#2630260069V#1K#1P…………………',
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    OP_56(0x01)
    OP_59()
    SetChrChipByIndex(0x000A, 19)
    SetChrChipByIndex(0x000B, 19)
    SetChrChipByIndex(0x000C, 20)

    @scena.Lambda('lambda_0F85')
    def lambda_0F85():
        OP_8F(0x00FE, -10470, 0, -1040, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F85)

    @scena.Lambda('lambda_0FA0')
    def lambda_0FA0():
        OP_8E(0x00FE, 5540, 0, -2180, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0FA0)

    @scena.Lambda('lambda_0FBB')
    def lambda_0FBB():
        OP_8E(0x00FE, -3810, 0, -9020, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0FBB)

    Sleep(1000)

    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    CreateThread(0x010A, 0x00, 0x00, 0x0006)

    @scena.Lambda('lambda_0FEE')
    def lambda_0FEE():
        OP_6D(-2240, 0, -1410, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_0FEE)

    @scena.Lambda('lambda_1006')
    def lambda_1006():
        OP_67(0, 7870, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1006)

    @scena.Lambda('lambda_101E')
    def lambda_101E():
        OP_6B(2000, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_101E)

    Sleep(250)

    @scena.Lambda('lambda_1033')
    def lambda_1033():
        OP_8F(0x00FE, -9340, 0, -1070, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1033)

    @scena.Lambda('lambda_104E')
    def lambda_104E():
        OP_8E(0x00FE, 4710, 0, -2200, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_104E)

    @scena.Lambda('lambda_1069')
    def lambda_1069():
        OP_8E(0x00FE, -3720, 0, -8029, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1069)

    Sleep(1000)

    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x010A, 0x00)
    Sleep(250)

    @scena.Lambda('lambda_109E')
    def lambda_109E():
        OP_8F(0x00FE, -7870, 0, -1370, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_109E)

    @scena.Lambda('lambda_10B9')
    def lambda_10B9():
        OP_8E(0x00FE, 3760, 0, -2210, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_10B9)

    @scena.Lambda('lambda_10D4')
    def lambda_10D4():
        OP_8E(0x00FE, -3580, 0, -7030, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_10D4)

    CreateThread(0x010A, 0x00, 0x00, 0x0006)
    Sleep(1000)

    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    SetChrChipByIndex(0x000A, 17)
    SetChrChipByIndex(0x000B, 17)
    SetChrChipByIndex(0x000C, 18)
    WaitForThreadExit(0x0106, 0x0000)
    WaitForThreadExit(0x0106, 0x0001)
    WaitForThreadExit(0x0106, 0x0002)

    ChrTalk(
        0x010A,
        (
            '#0120260070V#812F#6P（阿加特前辈……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260071V#053F#5P（啊啊……\n',
            '  果然非同寻常啊。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260072V#050F（还是先联手打倒一个，\n',
            '  然后再各自处理残局。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260073V(能做到吧)？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260074V#816F#6P（放心吧！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260075V#054F#5P那好──上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260076V#815F#6P好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF2')

    def _loc_124D(): pass

    label('loc_124D')

    ChrTalk(
        0x010A,
        (
            '#0120260037V#1316F#6P不行啊。\n',
            '感觉像是人去楼空的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260038V#818F前辈那边怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260079V#025F这边也一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260080V#522F出去了呢，还是\n',
            '刚转移据点了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260081V哪怕是有一些\n',
            '他们去向的线索也好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260042V#810F#6P嗯，看来没有任何\n',
            '关于去向的线索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260043V不过在那边的帐篷\n',
            '发现了这个文件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260084V#023F哎呀，给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x010A, 0x00F6, 0x00000320, 0x000005DC, 0x00)
    Sleep(500)

    OP_8F(0x010A, -3360, 0, -1060, 1500, 0x00)
    Sleep(500)

    FadeOut(300, 0, 100)
    OP_AD(0x00240112, 0x00BE, 0x0096, 0x000001F4)
    Sleep(3000)

    OP_AE(0x000001F4)
    FadeIn(300, 0)
    Sleep(1500)

    ChrTalk(
        0x0103,
        (
            '#0030260085V#022F嗯……\n',
            '画着奇怪的图案呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260086V『奥尔杰尤』开发计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260087V好像是什么交通工具的设计图啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260048V#810F#6P『奥尔杰尤』……\n',
            '略微有点华丽的名字呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260049V是飞船吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260090V#025F嗯～我不是专家\n',
            '不太明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030260091V#023F……哎呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260052V#814F#6P怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260093V#022F书页间夹着一张纸条呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260094V『请帖发送完毕了。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260095V『桌椅也准备好了。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260096V『这样一来茶会的准备就完成了。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260097V『只剩下烤点心\n',
            '  和等待客人到齐了。』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260058V#1310F#6P哦～\n',
            '感觉好温暖的内容啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260059V#811F感觉像是图画书中的一段文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260100V#026F嗯……\n',
            '好像是什么暗语似的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260101V#522F问题是这个讯息\n',
            '意味着什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030260102V#024F#4S散开！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260063V#814F#6P咦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp003_00.eff')
    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -4210, 0, -6050, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -3380, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -3300, 0, -2370, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_184B')
    def lambda_184B():
        OP_96(0x00FE, 0xFFFFFC22, 0x00000000, 0xFFFFFA06, 0x00000258, 0x00001770)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_184B)

    @scena.Lambda('lambda_1869')
    def lambda_1869():
        OP_96(0x00FE, 0xFFFFEE30, 0x00000000, 0xFFFFFB28, 0x00000258, 0x00001770)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1869)

    Sleep(100)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -2300, 0, -1090, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    SetChrChipByIndex(0x0103, 3)
    SetChrChipByIndex(0x010A, 11)

    @scena.Lambda('lambda_18D5')
    def lambda_18D5():
        OP_8C(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_18D5)

    @scena.Lambda('lambda_18E3')
    def lambda_18E3():
        OP_8C(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_18E3)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -2540, 0, 130, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -2000, 0, 1320, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    Sleep(500)

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000A, -11440, 0, -1180, 90)
    SetChrPos(0x000B, 7610, 0, -2040, 270)
    SetChrPos(0x000C, -3650, 0, -10100, 0)
    SetChrChipByIndex(0x000A, 17)
    SetChrChipByIndex(0x000B, 17)
    SetChrChipByIndex(0x000C, 18)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)

    @scena.Lambda('lambda_19D4')
    def lambda_19D4():
        OP_6D(-3470, 0, -1890, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_19D4)

    @scena.Lambda('lambda_19EC')
    def lambda_19EC():
        OP_67(0, 8380, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_19EC)

    @scena.Lambda('lambda_1A04')
    def lambda_1A04():
        OP_6B(2100, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_1A04)

    @scena.Lambda('lambda_1A14')
    def lambda_1A14():
        OP_6E(501, 3000)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_1A14)

    WaitForThreadExit(0x0103, 0x0000)
    WaitForThreadExit(0x0103, 0x0001)
    WaitForThreadExit(0x0103, 0x0002)
    OP_8C(0x0103, 90, 400)
    OP_8C(0x010A, 270, 400)

    ChrTalk(
        0x010A,
        (
            '#0120260064V#1317F#6P骗人……什么时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260105V#027F#5P呵呵，遮蔽气息的\n',
            '方式挺巧妙的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260106V跟那个银发\n',
            '少尉学来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1K#2P…………………',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000B,
        (
            '#1K#6P…………………',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000C,
        (
            '#2630260069V#1K#1P…………………',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    SetChrChipByIndex(0x000A, 19)
    SetChrChipByIndex(0x000B, 19)
    SetChrChipByIndex(0x000C, 20)

    @scena.Lambda('lambda_1B37')
    def lambda_1B37():
        OP_8F(0x00FE, -10470, 0, -1040, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B37)

    @scena.Lambda('lambda_1B52')
    def lambda_1B52():
        OP_8E(0x00FE, 5540, 0, -2180, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B52)

    @scena.Lambda('lambda_1B6D')
    def lambda_1B6D():
        OP_8E(0x00FE, -3810, 0, -9020, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B6D)

    Sleep(1000)

    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    CreateThread(0x010A, 0x00, 0x00, 0x0006)

    @scena.Lambda('lambda_1BA0')
    def lambda_1BA0():
        OP_6D(-2240, 0, -1410, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_1BA0)

    @scena.Lambda('lambda_1BB8')
    def lambda_1BB8():
        OP_67(0, 7870, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1BB8)

    @scena.Lambda('lambda_1BD0')
    def lambda_1BD0():
        OP_6B(2000, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_1BD0)

    Sleep(250)

    @scena.Lambda('lambda_1BE5')
    def lambda_1BE5():
        OP_8F(0x00FE, -9340, 0, -1070, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1BE5)

    @scena.Lambda('lambda_1C00')
    def lambda_1C00():
        OP_8E(0x00FE, 4710, 0, -2200, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1C00)

    @scena.Lambda('lambda_1C1B')
    def lambda_1C1B():
        OP_8E(0x00FE, -3720, 0, -8029, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1C1B)

    Sleep(1000)

    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x010A, 0x00)
    Sleep(250)

    @scena.Lambda('lambda_1C50')
    def lambda_1C50():
        OP_8F(0x00FE, -7870, 0, -1370, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1C50)

    @scena.Lambda('lambda_1C6B')
    def lambda_1C6B():
        OP_8E(0x00FE, 3760, 0, -2210, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1C6B)

    @scena.Lambda('lambda_1C86')
    def lambda_1C86():
        OP_8E(0x00FE, -3580, 0, -7030, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1C86)

    CreateThread(0x010A, 0x00, 0x00, 0x0006)
    Sleep(1000)

    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    SetChrChipByIndex(0x000A, 17)
    SetChrChipByIndex(0x000B, 17)
    SetChrChipByIndex(0x000C, 18)
    WaitForThreadExit(0x0103, 0x0000)
    WaitForThreadExit(0x0103, 0x0001)
    WaitForThreadExit(0x0103, 0x0002)

    ChrTalk(
        0x010A,
        (
            '#0120260110V#812F#6P（雪拉前辈……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260111V#026F#5P（嗯嗯……\n',
            '  看来不一般呢。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260112V#020F（先联手打倒一个，\n',
            '  然后各自解决残余。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260113V(能做到吧)？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260074V#816F#6P（放心吧！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260115V#024F#5P那好──上了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260076V#815F#6P好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DF2(): pass

    label('loc_1DF2')

    SetChrChipByIndex(0x000A, 19)
    SetChrChipByIndex(0x000B, 19)
    SetChrChipByIndex(0x000C, 20)

    @scena.Lambda('lambda_1E07')
    def lambda_1E07():
        OP_8E(0x00FE, -4280, 0, -1470, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1E07)

    @scena.Lambda('lambda_1E22')
    def lambda_1E22():
        OP_8E(0x00FE, 40, 0, -1410, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1E22)

    @scena.Lambda('lambda_1E3D')
    def lambda_1E3D():
        OP_8E(0x00FE, -2860, 0, -3780, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1E3D)

    @scena.Lambda('lambda_1E58')
    def lambda_1E58():
        OP_6B(1300, 500)

        ExitThread()

    DispatchAsync(0x010A, 0x0003, lambda_1E58)

    WaitForThreadExit(0x010A, 0x0003)
    OP_D6(0x00)
    AddItem(ItemTable['中回复药'], 4)
    AddItem(ItemTable['复苏药'], 2)
    AddItem(ItemTable['痊愈之药'], 4)
    SetChrStatus(ChrTable['亚妮拉丝'], 0x00, 53)
    SetChrStatus(ChrTable['亚妮拉丝'], 0xFE, 0)
    SetChrStatus(ChrTable['亚妮拉丝'], 0x05, 65)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['直刃剑'], 0xFF)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['纤维大衣'], 0xFF)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['纤维靴'], 0xFF)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['妨害２'], 0x00)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['省ＥＰ２'], 0x01)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['防御２'], 0x02)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['情报'], 0x03)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['精神２'], 0x04)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['ＨＰ２'], 0x05)
    EquipCmd(ChrTable['亚妮拉丝'], 0x0000, 0x03)
    EquipCmd(ChrTable['亚妮拉丝'], 0x0000, 0x04)
    AddCraft(ChrTable['亚妮拉丝'], 0x0000)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F1D',
    )

    SetChrStatus(ChrTable['雪拉扎德'], 0x00, 55)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    SetChrStatus(ChrTable['雪拉扎德'], 0x05, 65)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['青蛇'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['纤维大衣'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['纤维靴'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['青蛇'], 0x00)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['回避３'], 0x00)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['精神２'], 0x01)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['ＥＰ２'], 0x02)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['睡眠之刃'], 0x04)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['攻击２'], 0x05)
    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x03)
    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x04)
    AddCraft(ChrTable['雪拉扎德'], 0x0000)

    Jump('loc_1F71')

    def _loc_1F1D(): pass

    label('loc_1F1D')

    SetChrStatus(ChrTable['阿加特'], 0x00, 55)
    SetChrStatus(ChrTable['阿加特'], 0xFE, 0)
    SetChrStatus(ChrTable['阿加特'], 0x05, 65)
    EquipCmd(ChrTable['阿加特'], ItemTable['宫廷御剑'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['纤维大衣'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['纤维靴'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['攻击３'], 0x00)
    EquipCmd(ChrTable['阿加特'], ItemTable['移动２'], 0x01)
    EquipCmd(ChrTable['阿加特'], ItemTable['魔防２'], 0x02)
    EquipCmd(ChrTable['阿加特'], ItemTable['封技之刃'], 0x05)
    EquipCmd(ChrTable['阿加特'], ItemTable['防御２'], 0x06)
    EquipCmd(ChrTable['阿加特'], 0x0000, 0x03)
    EquipCmd(ChrTable['阿加特'], 0x0000, 0x04)
    AddCraft(ChrTable['阿加特'], 0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 5, 0x1045)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F71',
    )

    OP_BB(0x05, 0x06, 0x00000100)

    def _loc_1F71(): pass

    label('loc_1F71')

    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x000007A0, 0x00000000, 0x01, 0x0000, 0xFF)
    OP_D6(0x01)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x1FB3
@scena.Code('func_04_1FB3')
def func_04_1FB3():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000A, 0x0002)
    SetChrFlags(0x000B, 0x0002)
    SetChrFlags(0x000C, 0x0002)
    SetChrFlags(0x000A, 0x0800)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000C, 0x0800)
    SetChrChipByIndex(0x000A, 14)
    SetChrChipByIndex(0x000B, 14)
    SetChrChipByIndex(0x000C, 14)
    SetChrSubChip(0x000A, 3)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 2)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x000B, 0x00)
    TerminateThread(0x000C, 0x00)
    SetChrSubChip(0x00F6, 0)
    SetChrChipByIndex(0x00F6, 65535)
    ClearChrFlags(0x00F6, 0x0002)
    SetChrChipByIndex(0x010A, 65535)
    SetChrPos(0x00F6, -3000, 0, -2660, 270)
    SetChrPos(0x010A, -2930, 0, -3910, 270)
    SetChrPos(0x000A, -6360, 0, -3390, 90)
    SetChrPos(0x000B, -7770, 0, -4330, 270)
    SetChrPos(0x000C, -7530, 0, -2270, 90)
    SetChrPos(0x0008, 6360, 0, -3740, 270)
    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0008, 0x0080)
    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_6D(-4000, 0, -2190, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(45000, 0)
    OP_6E(464, 0)
    FadeIn(2000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_37A7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260117V#057F#5P这些家伙是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260118V解决是解决了……\n',
            '但感觉还真是奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260119V#812F#2P嗯～是不是用了\n',
            '什么危险的药物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260120V听说之前卢安的不良集团\n',
            '被药物操纵过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260121V#552F#5P不……\n',
            '不过反应还是不同啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260122V简直像在砍\n',
            '石头和树木一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    OP_22(0x007B, 0x00, 0x64)
    Sleep(500)

    NpcTalk(
        0x0008,
        '少年的声音',
        (
            '#0190260123V#3P啊哈哈，厉害厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '少年的声音',
        (
            '#0190260124V#3P你们真是\n',
            '相当优秀的游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)
    OP_21()
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_59()
    OP_1D(0x6F)
    Sleep(1000)

    @scena.Lambda('lambda_22EC')
    def lambda_22EC():
        OP_6D(-130, 0, -2660, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_22EC)

    @scena.Lambda('lambda_2304')
    def lambda_2304():
        OP_67(0, 7230, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2304)

    @scena.Lambda('lambda_231C')
    def lambda_231C():
        OP_6B(2009, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_231C)

    @scena.Lambda('lambda_232C')
    def lambda_232C():
        OP_8E(0x00FE, 3360, 0, -3740, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_232C)

    @scena.Lambda('lambda_2347')
    def lambda_2347():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2347)

    ChrTurnDirection(0x010A, 0x0008, 400)
    WaitForThreadExit(0x0008, 0x0003)
    WaitForThreadExit(0x0008, 0x0000)

    ChrTalk(
        0x0106,
        (
            '#0050260125V#052F#1P你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '奇怪的少年',
        (
            '#0190260126V#853F呼呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C5(0x00, 0x0000, 0x0000, 0x0200, 0x0200, 0x0064, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0200, 0x0200, 0x00FFFFFF, 0x00, 'C_VIS118._CH')
    OP_C6(0x00, 0x00, 150000, 60000, 0)
    OP_C6(0x00, 0x00, 175000, 60000, 500)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('奇怪的少年')

    Talk(
        (
            '#0190260127V#850F执行者Ｎｏ．０。\n',
            '『小丑』肯帕雷拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260128V『噬身之蛇』的成员之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x03, 16777215, 250, 0)
    Sleep(250)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x010A,
        (
            '#0120260129V#1317F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260130V#057F#1P终于出现了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0106, 7)
    SetChrSubChip(0x0106, 0)
    Sleep(300)

    SetChrChipByIndex(0x010A, 11)
    SetChrSubChip(0x010A, 0)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050260131V#057F#1P你小子……\n',
            '为什么会在这种地方？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260132V和特务兵的余党在一起\n',
            '你打算做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260133V#853F呵呵呵～\n',
            '这次我的任务仅仅是当一个旁观者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260134V如果要问我关于具体计划的事情\n',
            '那可就问错人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260135V因为我也一无所知呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260136V#555F#1P旁观者……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260137V#850F不过、要参加茶会的话\n',
            '可能还是抓紧点比较好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260138V虽然不知道在哪举行\n',
            '不过至少不是这里就对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260139V#851F还是说，待在这里和我一起\n',
            '喝一晚上咖啡？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260140V#057F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260141V#813F#6P唔，我说你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260142V好像还很年轻\n',
            '真的是『结社』的人？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260143V#812F为了你自己好，\n',
            '还是别干了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260144V#853F哈哈哈，好善良的姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260145V把小丑当笑话\n',
            '也就算了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260146V#854F担心别人可是很不礼貌的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260147V#814F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 8)
    OP_99(0x0008, 0x09, 0x0A, 0x000005DC)
    OP_22(0x00BC, 0x00, 0x64)
    Sleep(500)

    SetChrSubChip(0x0008, 8)

    @scena.Lambda('lambda_28B1')
    def lambda_28B1():
        OP_6D(-2000, 0, -2270, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_28B1)

    Fade(1000)
    ClearChrFlags(0x000A, 0x0002)
    ClearChrFlags(0x000B, 0x0002)
    ClearChrFlags(0x000C, 0x0002)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)
    SetChrChipByIndex(0x000A, 17)
    SetChrChipByIndex(0x000B, 17)
    SetChrChipByIndex(0x000C, 18)
    OP_8C(0x000A, 90, 0)
    OP_8C(0x000B, 90, 0)
    OP_8C(0x000C, 90, 0)
    OP_0D()
    WaitForThreadExit(0x0008, 0x0001)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    @scena.Lambda('lambda_2944')
    def lambda_2944():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2944)

    OP_8C(0x010A, 270, 400)

    ChrTalk(
        0x010A,
        (
            '#0120260148V#1317F骗、骗人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260149V#055F#5P经受那样的打击\n',
            '居然还能动弹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260150V#854F#8P哈哈哈，所以说你们这些\n',
            '游击士真是太天真了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260151V要打就应该将其\n',
            '彻底地破坏掉㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x01, 'monster\\msc0100.eff')
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 8)
    OP_99(0x0008, 0x09, 0x0A, 0x000005DC)
    OP_22(0x00BC, 0x00, 0x64)
    Sleep(500)

    SetChrSubChip(0x0008, 8)
    PlayEffect(0x01, 0x01, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0x02, 0x000B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0x03, 0x000C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    LoadEffect(0x02, 'map\\mp047_00.eff')
    PlayEffect(0x02, 0x04, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0x05, 0x000B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0x06, 0x000C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    CreateThread(0x0008, 0x03, 0x00, 0x0007)
    Fade(500)

    @scena.Lambda('lambda_2BDE')
    def lambda_2BDE():
        OP_6D(-130, 0, -2660, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2BDE)

    TerminateThread(0x000A, 0x00)
    TerminateThread(0x000B, 0x00)
    TerminateThread(0x000C, 0x00)
    ClearChrFlags(0x000A, 0x0001)
    ClearChrFlags(0x000B, 0x0001)
    ClearChrFlags(0x000C, 0x0001)
    SetChrFlags(0x000A, 0x0002)
    SetChrFlags(0x000B, 0x0002)
    SetChrFlags(0x000C, 0x0002)
    SetChrChipByIndex(0x000A, 15)
    SetChrChipByIndex(0x000B, 15)
    SetChrChipByIndex(0x000C, 15)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000B, 1)
    SetChrSubChip(0x000C, 2)
    SetChrPos(0x000A, -5990, 0, -2060, 0)
    SetChrPos(0x000C, -7310, 0, -5200, 0)
    ClearChrFlags(0x000D, 0x0001)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0002)
    SetChrChipByIndex(0x000D, 15)
    SetChrSubChip(0x000D, 3)
    SetChrPos(0x000D, -4610, 0, -4540, 0)
    SetChrChipByIndex(0x0106, 22)
    SetChrChipByIndex(0x010A, 23)
    SetChrSubChip(0x0106, 0)
    SetChrSubChip(0x010A, 0)

    @scena.Lambda('lambda_2C9E')
    def lambda_2C9E():
        OP_96(0x00FE, 0xFFFFF948, 0x00000000, 0xFFFFF75E, 0x0000012C, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2C9E)

    @scena.Lambda('lambda_2CBC')
    def lambda_2CBC():
        OP_9E(0x00FE, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_2CBC)

    @scena.Lambda('lambda_2CD6')
    def lambda_2CD6():
        OP_96(0x00FE, 0xFFFFF876, 0x00000000, 0xFFFFF06A, 0x0000012C, 0x00001B58)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2CD6)

    @scena.Lambda('lambda_2CF4')
    def lambda_2CF4():
        OP_9E(0x00FE, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_2CF4)

    WaitForThreadExit(0x010A, 0x0001)
    OP_8C(0x0106, 270, 0)
    OP_8C(0x010A, 270, 0)
    SetChrChipByIndex(0x0106, 10)
    SetChrChipByIndex(0x010A, 13)
    SetChrSubChip(0x0106, 3)
    SetChrSubChip(0x010A, 3)

    ChrTalk(
        0x0106,
        (
            '#056F#10A#1P啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x010A,
        (
            '#0120260153V#1312F#1P#10A#2P啊呜……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_0D()
    WaitForThreadExit(0x0008, 0x0000)
    Sleep(1000)

    OP_9E(0x0106, 0x00000014, 0x00000000, 0x000001F4, 0x00000FA0)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050260154V#550F#5P唔……你小子！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260155V#1317F好过分……竟然做这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260156V#851F啊哈哈，吓了一跳吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260157V很精彩的演出～\n',
            '让你们受惊了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x02, 'map\\\\mp055_00.eff')
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 8)
    OP_99(0x0008, 0x09, 0x0A, 0x000005DC)
    OP_22(0x00BC, 0x00, 0x64)
    Sleep(500)

    SetChrSubChip(0x0008, 8)
    PlayEffect(0x02, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x010A, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0190260158V#854F哈哈哈～好了，\n',
            '今晚的演出到此结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(100)
    ClearChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    OP_99(0x0008, 0x00, 0x03, 0x000003E8)

    ChrTalk(
        0x0008,
        (
            '#0190260159V#854F那么各位，保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2F49')
    def lambda_2F49():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_2F49')

    DispatchAsync2(0x0106, 0x0003, lambda_2F49)

    Sleep(500)

    OP_99(0x0106, 0x03, 0x00, 0x000005DC)
    TerminateThread(0x0106, 0x03)
    SetChrChipByIndex(0x0106, 7)
    SetChrSubChip(0x0106, 0)
    Sleep(300)

    OP_8C(0x0106, 90, 600)

    ChrTalk(
        0x0106,
        (
            '#0050260160V#054F#3S别开玩笑了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0008, 0)
    SetChrFlags(0x0106, 0x1000)
    SetChrChipByIndex(0x0106, 8)

    @scena.Lambda('lambda_2FC5')
    def lambda_2FC5():
        OP_6D(2500, 0, -2270, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2FC5)

    @scena.Lambda('lambda_2FDD')
    def lambda_2FDD():
        OP_8F(0x00FE, 500, 0, -3200, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2FDD)

    @scena.Lambda('lambda_2FF8')
    def lambda_2FF8():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2FF8)

    WaitForThreadExit(0x0106, 0x0001)
    OP_22(0x01F9, 0x00, 0x64)
    SetChrChipByIndex(0x0106, 9)
    SetChrSubChip(0x0106, 0)
    SetChrFlags(0x0106, 0x0020)
    OP_82(0x01, 0x02)
    CreateThread(0x0008, 0x03, 0x00, 0x0008)

    @scena.Lambda('lambda_302D')
    def lambda_302D():
        OP_94(0x01, 0x00FE, 0x0000, 0x000009C4, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_302D)

    @scena.Lambda('lambda_3043')
    def lambda_3043():
        OP_99(0x00FE, 0x00, 0x07, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_3043)

    Sleep(300)

    OP_22(0x0208, 0x00, 0x64)
    OP_20(0x000007D0)
    WaitForThreadExit(0x0106, 0x0002)
    TerminateThread(0x0106, 0x01)
    Sleep(2000)

    OP_99(0x0106, 0x07, 0x00, 0x000005DC)
    ClearChrFlags(0x0106, 0x1000)
    ClearChrFlags(0x0106, 0x0020)
    SetChrFlags(0x0008, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050260161V#057F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_30BC')
    def lambda_30BC():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_30BC')

    DispatchAsync2(0x010A, 0x0003, lambda_30BC)

    Sleep(500)

    OP_99(0x010A, 0x03, 0x00, 0x000003E8)
    TerminateThread(0x010A, 0x03)
    Fade(250)
    SetChrChipByIndex(0x010A, 65535)
    SetChrSubChip(0x010A, 0)
    OP_0D()
    Sleep(500)

    OP_8C(0x010A, 90, 400)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120260162V#813F#1P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260163V阿加特前辈……那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260164V#053F#5P……啊啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0106, 65535)
    SetChrSubChip(0x0106, 0)
    OP_0D()
    Sleep(500)

    OP_8C(0x0106, 270, 400)
    Sleep(500)

    @scena.Lambda('lambda_31A9')
    def lambda_31A9():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_31A9')

    DispatchAsync2(0x010A, 0x0001, lambda_31A9)

    @scena.Lambda('lambda_31BA')
    def lambda_31BA():
        OP_6D(-2500, 0, -3390, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_31BA)

    OP_8E(0x0106, -2070, 0, -2710, 1500, 0x00)
    WaitForThreadExit(0x0106, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050260165V#552F明明没有那么\n',
            '罪大恶极，\n',
            '却沦落到这种死法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260166V总之……\n',
            '不能就这样放着不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x010A, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050260167V#556F你就在那边\n',
            '随便打发打发时间吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260168V对年轻女孩来说，这种场面太残酷了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260169V#1317F#4P但、但是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    TerminateThread(0x010A, 0x01)
    OP_8C(0x010A, 270, 400)

    ChrTalk(
        0x010A,
        (
            '#0120260170V#814F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_333C')
    def lambda_333C():
        ChrTurnDirection(0x00FE, 0x010A, 400)
        Yield()

        Jump('lambda_333C')

    DispatchAsync2(0x0106, 0x0001, lambda_333C)

    @scena.Lambda('lambda_334D')
    def lambda_334D():
        OP_8E(0x00FE, -3760, 0, -4440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_334D)

    WaitForThreadExit(0x010A, 0x0001)
    Fade(250)
    SetChrFlags(0x010A, 0x0002)
    SetChrChipByIndex(0x010A, 2)
    SetChrSubChip(0x010A, 7)
    OP_0D()
    Sleep(1000)

    Fade(250)
    ClearChrFlags(0x000D, 0x0002)
    SetChrFlags(0x000D, 0x0080)
    SetChrChipByIndex(0x010A, 16)
    SetChrSubChip(0x010A, 7)
    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050260171V#055F喂、喂！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260172V#1317F那个、阿加特前辈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260173V这个手臂……\n',
            '好像是人造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260174V#052F什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    TerminateThread(0x0106, 0x01)
    OP_8C(0x0106, 270, 400)

    @scena.Lambda('lambda_344A')
    def lambda_344A():
        OP_6D(-4620, 0, -2840, 1500)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_344A)

    OP_8E(0x0106, -4690, 0, -1920, 2000, 0x00)
    Fade(250)
    SetChrFlags(0x0106, 0x0002)
    SetChrChipByIndex(0x0106, 24)
    SetChrSubChip(0x0106, 7)
    OP_0D()
    Sleep(500)

    OP_62(0x0106, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0106)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050260175V#057F#5P齿轮和发条……\n',
            '还有结晶回路的碎片……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260176V也就是说这个东西是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, -9770, 0, 5880, 180)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    SetChrName('青年的声音')

    NpcTalk(
        0x0009,
        '青年的声音',
        (
            '#0180260177V#4P可以按规则自己行动的导力人偶……\n',
            '也就是那人形兵器吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)
    OP_62(0x0106, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_6D(-4950, 0, -600, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(1860, 0)
    OP_6C(21000, 0)
    OP_6E(464, 0)
    ClearChrFlags(0x010A, 0x0020)
    ClearChrFlags(0x010A, 0x0002)
    SetChrChipByIndex(0x010A, 65535)
    SetChrSubChip(0x010A, 0)
    ClearChrFlags(0x0106, 0x0002)
    SetChrChipByIndex(0x0106, 65535)
    SetChrSubChip(0x0106, 0)
    TerminateThread(0x010A, 0xFF)
    OP_8C(0x0106, 340, 0)
    OP_8C(0x010A, 340, 0)

    @scena.Lambda('lambda_3663')
    def lambda_3663():
        OP_8E(0x00FE, -6740, 0, 1320, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3663)

    @scena.Lambda('lambda_367E')
    def lambda_367E():
        OP_6D(-5810, 0, 150, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_367E)

    OP_0D()
    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x010A,
        (
            '#0120260178V#814F#2P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260179V#057F#2P……什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0180260180V#1065F#5P七耀教会巡回神父，\n',
            '凯文·格拉汉姆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180260181V#1060F是阿加特·科洛斯纳先生和\n',
            '亚妮拉丝·艾尔菲德小姐对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180260182V和你们商量一下……\n',
            '相互交换一下情报怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E61')

    def _loc_37A7(): pass

    label('loc_37A7')

    ChrTalk(
        0x0103,
        (
            '#0030260183V#022F#5P呼，这些家伙是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260184V虽然是打倒了……\n',
            '反应还真是奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260119V#812F#2P嗯～是不是用了\n',
            '什么危险的药物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260120V听说之前卢安的不良集团\n',
            '被药物操纵过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260187V#020F#5P是艾丝蒂尔他们\n',
            '解决了的事件吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260188V#522F不过，和那个\n',
            '反应又不相同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260189V简直像打在石头或者木头上一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x007B, 0x00, 0x64)
    Sleep(500)

    NpcTalk(
        0x0008,
        '少年的声音',
        (
            '#0190260123V#3P啊哈哈，厉害厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '少年的声音',
        (
            '#0190260191V#3P姐姐们、\n',
            '是相当优秀的游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_39C4')
    def lambda_39C4():
        OP_6D(-130, 0, -2660, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_39C4)

    @scena.Lambda('lambda_39DC')
    def lambda_39DC():
        OP_67(0, 7230, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_39DC)

    @scena.Lambda('lambda_39F4')
    def lambda_39F4():
        OP_6B(2009, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_39F4)

    @scena.Lambda('lambda_3A04')
    def lambda_3A04():
        OP_8E(0x00FE, 3360, 0, -3740, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_3A04)

    @scena.Lambda('lambda_3A1F')
    def lambda_3A1F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_3A1F)

    ChrTurnDirection(0x010A, 0x0008, 400)
    WaitForThreadExit(0x0008, 0x0003)
    WaitForThreadExit(0x0008, 0x0000)

    ChrTalk(
        0x0103,
        (
            '#0030260192V#023F#1P你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '奇怪的少年',
        (
            '#0190260193V#853F呼呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C5(0x00, 0x0000, 0x0000, 0x0200, 0x0200, 0x0064, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0200, 0x0200, 0x00FFFFFF, 0x00, 'C_VIS118._CH')
    OP_C6(0x00, 0x00, 150000, 60000, 0)
    OP_C6(0x00, 0x00, 175000, 60000, 500)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('奇怪的少年')

    Talk(
        (
            '#0190260127V#850F执行者Ｎｏ．０。\n',
            '『小丑』肯帕雷拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260128V『噬身之蛇』的成员之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x03, 16777215, 250, 0)
    Sleep(250)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_1D(0x6F)
    Sleep(1000)

    ChrTalk(
        0x010A,
        (
            '#0120260129V#1317F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260197V#022F#1P终于出现了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0103, 3)
    SetChrSubChip(0x0103, 0)
    Sleep(300)

    SetChrChipByIndex(0x010A, 11)
    SetChrSubChip(0x010A, 0)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030260198V#022F#1P你……\n',
            '怎么会在这种地方？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260199V和特务兵的余党在一起\n',
            '打算做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260133V#853F呵呵呵，\n',
            '这次我的任务仅仅是当一个『旁观者』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260134V如果是要问我关于具体计划的事\n',
            '那可就问错人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260135V因为我也一无所知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260203V#023F#1P『旁观者』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260137V#850F不过，要参加『茶会』的话，\n',
            '或许动作要快一点比较好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260138V虽然不知道在哪举行\n',
            '不过至少不是这里就对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260139V#851F还是说，待在这里和我一起\n',
            '喝一晚上咖啡？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260207V#022F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260141V#813F#6P唔，我说你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260142V看起来好像很年轻，\n',
            '真的是『结社』的人？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260143V#812F我不会责备你的，\n',
            '别再继续做这种事情了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260144V#853F哼哼哼，好善良的姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260145V不过，要是你把本小丑\n',
            '当成笑料看也就算了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260146V#854F如果是为我担心，那就是多此一举了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260147V#814F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 8)
    OP_99(0x0008, 0x09, 0x0A, 0x000005DC)
    OP_22(0x00BC, 0x00, 0x64)
    Sleep(500)

    SetChrSubChip(0x0008, 8)

    @scena.Lambda('lambda_3FB7')
    def lambda_3FB7():
        OP_6D(-2000, 0, -2270, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3FB7)

    Fade(1000)
    ClearChrFlags(0x000A, 0x0002)
    ClearChrFlags(0x000B, 0x0002)
    ClearChrFlags(0x000C, 0x0002)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)
    SetChrChipByIndex(0x000A, 17)
    SetChrChipByIndex(0x000B, 17)
    SetChrChipByIndex(0x000C, 18)
    OP_8C(0x000A, 90, 0)
    OP_8C(0x000B, 90, 0)
    OP_8C(0x000C, 90, 0)
    OP_0D()
    WaitForThreadExit(0x0008, 0x0001)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    @scena.Lambda('lambda_404A')
    def lambda_404A():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_404A)

    OP_8C(0x010A, 270, 400)

    ChrTalk(
        0x010A,
        (
            '#0120260148V#1317F骗、骗人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260216V#024F#5P怎么会……\n',
            '应该完全无法战斗了才对啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260150V#854F#8P哈哈哈，所以说你们这些\n',
            '游击士真是太天真了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260151V要做就应该要\n',
            '彻底地破坏掉㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x01, 'monster\\msc0100.eff')
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 8)
    OP_99(0x0008, 0x09, 0x0A, 0x000005DC)
    OP_22(0x00BC, 0x00, 0x64)
    Sleep(500)

    SetChrSubChip(0x0008, 8)
    PlayEffect(0x01, 0x01, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0x02, 0x000B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0x03, 0x000C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    LoadEffect(0x02, 'map\\mp047_00.eff')
    PlayEffect(0x02, 0x04, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0x05, 0x000B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0x06, 0x000C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    CreateThread(0x0008, 0x03, 0x00, 0x0007)
    Fade(500)

    @scena.Lambda('lambda_42E8')
    def lambda_42E8():
        OP_6D(-130, 0, -2660, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_42E8)

    TerminateThread(0x000A, 0x00)
    TerminateThread(0x000B, 0x00)
    TerminateThread(0x000C, 0x00)
    ClearChrFlags(0x000A, 0x0001)
    ClearChrFlags(0x000B, 0x0001)
    ClearChrFlags(0x000C, 0x0001)
    SetChrFlags(0x000A, 0x0002)
    SetChrFlags(0x000B, 0x0002)
    SetChrFlags(0x000C, 0x0002)
    SetChrChipByIndex(0x000A, 15)
    SetChrChipByIndex(0x000B, 15)
    SetChrChipByIndex(0x000C, 15)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000B, 1)
    SetChrSubChip(0x000C, 2)
    SetChrPos(0x000A, -5990, 0, -2060, 0)
    SetChrPos(0x000C, -7310, 0, -5200, 0)
    ClearChrFlags(0x000D, 0x0001)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0002)
    SetChrChipByIndex(0x000D, 15)
    SetChrSubChip(0x000D, 3)
    SetChrPos(0x000D, -4610, 0, -4540, 0)
    SetChrChipByIndex(0x0103, 21)
    SetChrChipByIndex(0x010A, 23)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x010A, 0)

    @scena.Lambda('lambda_43A8')
    def lambda_43A8():
        OP_96(0x00FE, 0xFFFFF948, 0x00000000, 0xFFFFF75E, 0x0000012C, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_43A8)

    @scena.Lambda('lambda_43C6')
    def lambda_43C6():
        OP_9E(0x00FE, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_43C6)

    @scena.Lambda('lambda_43E0')
    def lambda_43E0():
        OP_96(0x00FE, 0xFFFFF876, 0x00000000, 0xFFFFF06A, 0x0000012C, 0x00001B58)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_43E0)

    @scena.Lambda('lambda_43FE')
    def lambda_43FE():
        OP_9E(0x00FE, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_43FE)

    WaitForThreadExit(0x010A, 0x0001)
    OP_8C(0x0103, 270, 0)
    OP_8C(0x010A, 270, 0)
    SetChrChipByIndex(0x0103, 6)
    SetChrChipByIndex(0x010A, 13)
    SetChrSubChip(0x0103, 3)
    SetChrSubChip(0x010A, 3)

    ChrTalk(
        0x0103,
        (
            '#523F#10A#1P唔……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x010A,
        (
            '#0120260153V#1312F#1P#10A#2P啊呜……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_0D()
    WaitForThreadExit(0x0008, 0x0000)
    Sleep(1000)

    OP_9E(0x0103, 0x00000014, 0x00000000, 0x000001F4, 0x00000FA0)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030260221V#522F#5P怎、怎么这样……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260222V#1317F好过分……这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190260156V#851F啊哈哈，吓了一跳吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190260157V这个吓人箱子\n',
            '做得很不赖吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x02, 'map\\\\mp055_00.eff')
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 8)
    OP_99(0x0008, 0x09, 0x0A, 0x000005DC)
    OP_22(0x00BC, 0x00, 0x64)
    Sleep(500)

    SetChrSubChip(0x0008, 8)
    PlayEffect(0x02, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x010A, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0190260158V#854F哈哈哈，好了，\n',
            '今晚的演出就到此结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(100)
    ClearChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    OP_99(0x0008, 0x00, 0x03, 0x000003E8)

    ChrTalk(
        0x0008,
        (
            '#0190260159V#854F那么各位，保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_464F')
    def lambda_464F():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_464F')

    DispatchAsync2(0x0103, 0x0003, lambda_464F)

    Sleep(500)

    OP_99(0x0103, 0x03, 0x00, 0x000005DC)
    TerminateThread(0x0103, 0x03)
    SetChrChipByIndex(0x0103, 3)
    SetChrSubChip(0x0103, 0)
    Sleep(300)

    OP_8C(0x0103, 90, 600)

    ChrTalk(
        0x0103,
        (
            '#0030260227V#024F#3S等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0008, 0)
    SetChrFlags(0x0103, 0x1000)
    SetChrChipByIndex(0x0103, 4)

    @scena.Lambda('lambda_46C7')
    def lambda_46C7():
        OP_6D(2500, 0, -2270, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_46C7)

    @scena.Lambda('lambda_46DF')
    def lambda_46DF():
        OP_8F(0x00FE, 1500, 0, -3200, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_46DF)

    @scena.Lambda('lambda_46FA')
    def lambda_46FA():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_46FA)

    WaitForThreadExit(0x0103, 0x0001)
    SetChrChipByIndex(0x0103, 5)
    SetChrSubChip(0x0103, 0)
    OP_82(0x01, 0x02)
    CreateThread(0x0008, 0x03, 0x00, 0x0008)

    @scena.Lambda('lambda_4725')
    def lambda_4725():
        OP_99(0x00FE, 0x00, 0x07, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_4725)

    OP_22(0x01F6, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0208, 0x00, 0x64)
    OP_20(0x000007D0)
    WaitForThreadExit(0x0103, 0x0003)
    ClearChrFlags(0x0103, 0x1000)
    SetChrFlags(0x0008, 0x0080)
    Sleep(1500)

    ChrTalk(
        0x0103,
        (
            '#0030260228V#022F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_478B')
    def lambda_478B():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_478B')

    DispatchAsync2(0x010A, 0x0003, lambda_478B)

    Sleep(500)

    OP_99(0x010A, 0x03, 0x00, 0x000003E8)
    TerminateThread(0x010A, 0x03)
    Fade(250)
    SetChrChipByIndex(0x010A, 65535)
    SetChrSubChip(0x010A, 0)
    OP_0D()
    Sleep(500)

    OP_8C(0x010A, 90, 400)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120260162V#813F#1P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260230V雪拉前辈……那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260231V#026F#5P……嗯嗯………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0103, 65535)
    SetChrSubChip(0x0103, 0)
    OP_0D()
    Sleep(500)

    OP_8C(0x0103, 270, 400)
    Sleep(500)

    @scena.Lambda('lambda_4876')
    def lambda_4876():
        ChrTurnDirection(0x00FE, 0x0103, 400)
        Yield()

        Jump('lambda_4876')

    DispatchAsync2(0x010A, 0x0001, lambda_4876)

    @scena.Lambda('lambda_4887')
    def lambda_4887():
        OP_6D(-2500, 0, -3390, 2000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4887)

    OP_8E(0x0103, -2070, 0, -2710, 1500, 0x00)
    WaitForThreadExit(0x0103, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030260232V#522F虽然毫无痛苦地\n',
            '死去也算是幸运……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260233V不管怎样……\n',
            '不能就这样放着不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x010A, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030260234V#524F亚妮拉丝，不好意思，\n',
            '能不能帮我把他们埋了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260235V#812F#4P是、是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    TerminateThread(0x010A, 0x01)
    OP_8C(0x010A, 270, 400)

    ChrTalk(
        0x010A,
        (
            '#0120260170V#814F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_49D9')
    def lambda_49D9():
        ChrTurnDirection(0x00FE, 0x010A, 400)
        Yield()

        Jump('lambda_49D9')

    DispatchAsync2(0x0103, 0x0001, lambda_49D9)

    @scena.Lambda('lambda_49EA')
    def lambda_49EA():
        OP_8E(0x00FE, -3760, 0, -4440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_49EA)

    WaitForThreadExit(0x010A, 0x0001)
    Fade(250)
    SetChrFlags(0x010A, 0x0002)
    SetChrChipByIndex(0x010A, 2)
    SetChrSubChip(0x010A, 7)
    OP_0D()
    Sleep(1000)

    Fade(250)
    ClearChrFlags(0x000D, 0x0002)
    SetChrFlags(0x000D, 0x0080)
    SetChrChipByIndex(0x010A, 16)
    SetChrSubChip(0x010A, 7)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#0030260237V#023F慢、慢着！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260238V#1317F那个、雪拉前辈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260173V这个手臂……\n',
            '好像是人造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260240V#023F咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    TerminateThread(0x0103, 0x01)
    OP_8C(0x0103, 270, 400)

    @scena.Lambda('lambda_4AE5')
    def lambda_4AE5():
        OP_6D(-4620, 0, -2840, 1500)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4AE5)

    OP_8E(0x0103, -4690, 0, -1920, 2000, 0x00)
    Fade(250)
    SetChrFlags(0x0103, 0x0002)
    SetChrChipByIndex(0x0103, 25)
    SetChrSubChip(0x0103, 7)
    OP_0D()
    Sleep(500)

    OP_62(0x0103, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0103)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030260241V#022F#5P齿轮和发条……\n',
            '还有结晶回路的碎片……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260242V说不定这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, -9770, 0, 5880, 180)
    ClearChrFlags(0x0009, 0x0080)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    SetChrName('青年的声音')

    NpcTalk(
        0x0009,
        '青年的声音',
        (
            '#0180260177V#4P可以按规则自己行动的导力人偶……\n',
            '也就是所谓的人形兵器吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_6D(-4950, 0, -600, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(1860, 0)
    OP_6C(21000, 0)
    OP_6E(464, 0)
    ClearChrFlags(0x010A, 0x0020)
    ClearChrFlags(0x010A, 0x0002)
    SetChrChipByIndex(0x010A, 65535)
    SetChrSubChip(0x010A, 0)
    ClearChrFlags(0x0103, 0x0002)
    SetChrChipByIndex(0x0103, 65535)
    SetChrSubChip(0x0103, 0)
    TerminateThread(0x010A, 0xFF)
    OP_8C(0x0103, 340, 0)
    OP_8C(0x010A, 340, 0)

    @scena.Lambda('lambda_4CD9')
    def lambda_4CD9():
        OP_8E(0x00FE, -6740, 0, 1320, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4CD9)

    @scena.Lambda('lambda_4CF4')
    def lambda_4CF4():
        OP_6D(-5810, 0, 150, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_4CF4)

    OP_0D()
    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x010A,
        (
            '#0120260178V#814F#2P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260245V#023F#2P你确实是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0180260246V#1062F#5P哟，看来\n',
            '你还记得我呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180260247V#1065F重新自我介绍一下──我是\n',
            '七耀教会的巡回神父凯文·格拉汉姆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180260248V#1060F两位是雪拉扎德·哈维小姐和\n',
            '亚妮拉丝·艾尔菲德小姐对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180260182V和你们商量一下……\n',
            '相互交换一下情报怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E61(): pass

    label('loc_4E61')

    FadeOut(1500, 0, -1)
    OP_0D()
    OP_23(0x010E)
    Sleep(500)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R1203._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x4E90
@scena.Code('func_05_4E90')
def func_05_4E90():
    OP_8F(0x00FE, -1970, 0, -1430, 1000, 0x00)

    Return()

# id: 0x0006 offset: 0x4EA5
@scena.Code('func_06_4EA5')
def func_06_4EA5():
    SetChrChipByIndex(0x010A, 12)
    SetChrSubChip(0x010A, 0)
    OP_8F(0x00FE, -3020, 0, -1450, 1000, 0x00)
    SetChrChipByIndex(0x010A, 11)
    SetChrSubChip(0x010A, 0)

    Return()

# id: 0x0007 offset: 0x4ECE
@scena.Code('func_07_4ECE')
def func_07_4ECE():
    OP_7C(0x000000C8, 0x000000C8, 0x00000BB8, 0x000003E8)
    Sleep(200)

    OP_7C(0x000000C8, 0x000000C8, 0x00000BB8, 0x000003E8)
    Sleep(200)

    OP_7C(0x000000C8, 0x000000C8, 0x00000BB8, 0x000003E8)

    Return()

# id: 0x0008 offset: 0x4F0C
@scena.Code('func_08_4F0C')
def func_08_4F0C():
    Sleep(300)

    OP_24(0x010A, 0x5A)
    Sleep(300)

    OP_24(0x010A, 0x50)
    Sleep(300)

    OP_24(0x010A, 0x46)
    Sleep(300)

    OP_24(0x010A, 0x3C)
    Sleep(300)

    OP_24(0x010A, 0x32)
    Sleep(300)

    OP_24(0x010A, 0x28)
    Sleep(300)

    OP_24(0x010A, 0x1E)
    Sleep(300)

    OP_23(0x010A)

    Return()

# id: 0x0009 offset: 0x4F54
@scena.Code('func_09_4F54')
def func_09_4F54():
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
        (0x00000000, 'loc_4FCE'),
        (0x00000001, 'loc_4FD4'),
        (-1, 'loc_4FDA'),
    )

    def _loc_4FCE(): pass

    label('loc_4FCE')

    OP_A2(0x1200)

    Jump('loc_4FDA')

    def _loc_4FD4(): pass

    label('loc_4FD4')

    OP_A2(0x1201)

    Jump('loc_4FDA')

    def _loc_4FDA(): pass

    label('loc_4FDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4FE8',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_4FEC')

    def _loc_4FE8(): pass

    label('loc_4FE8')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_4FEC(): pass

    label('loc_4FEC')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
