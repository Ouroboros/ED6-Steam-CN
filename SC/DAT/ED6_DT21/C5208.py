import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5208_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5208   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5208.x'
    header.mapIndex       = 1
    header.bgm            = 63
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '穆拉少校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '尤莉亚上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '多伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '吉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '凯文神父',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '乔丝特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '地震控制用假人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x268
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x268
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x268
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x268
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_284',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x42),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    PlaySE(133, 0x01, 0x46)
    Event(0, func_02_2D6)

    def _loc_284(): pass

    label('loc_284')

    Return()

# id: 0x0001 offset: 0x285
@scena.Code('func_01_285')
def func_01_285():
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_72(0x0001, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Return,
        ),
        'loc_2CE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x42),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)
    MapSetFlags(0x00100000)
    OP_6F(0x0001, 240)
    CreateThread(0x0015, 0x03, 0x00, func_04_1E09)
    PlaySE(133, 0x01, 0x46)
    OP_72(0x0002, 0x0004)
    OP_72(0x0002, 0x0002)

    Jump('loc_2D5')

    def _loc_2CE(): pass

    label('loc_2CE')

    OP_6F(0x0001, 0)

    def _loc_2D5(): pass

    label('loc_2D5')

    Return()

# id: 0x0002 offset: 0x2D6
@scena.Code('func_02_2D6')
def func_02_2D6():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x08, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    FormationDelMember(0x0E, 0xFF)
    FormationDelMember(0x0F, 0xFF)
    LoadChip('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP', 0)
    LoadChip('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP', 1)
    LoadChip('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP', 2)
    LoadChip('ED6_DT27/CH03760._CH', 'ED6_DT27/CH03760P._CP', 3)
    LoadChip('ED6_DT27/CH03770._CH', 'ED6_DT27/CH03770P._CP', 4)
    LoadChip('ED6_DT07/CH00021._CH', 'ED6_DT07/CH00021P._CP', 5)
    LoadChip('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP', 6)
    LoadChip('ED6_DT07/CH00031._CH', 'ED6_DT07/CH00031P._CP', 7)
    LoadChip('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP', 8)
    LoadChip('ED6_DT27/CH03211._CH', 'ED6_DT27/CH03211P._CP', 9)
    LoadChip('ED6_DT27/CH03210._CH', 'ED6_DT27/CH03210P._CP', 10)
    LoadChip('ED6_DT07/CH00051._CH', 'ED6_DT07/CH00051P._CP', 11)
    LoadChip('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP', 12)
    LoadChip('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP', 13)
    LoadChip('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP', 14)
    LoadChip('ED6_DT07/CH00071._CH', 'ED6_DT07/CH00071P._CP', 15)
    LoadChip('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP', 16)
    LoadChip('ED6_DT27/CH03081._CH', 'ED6_DT27/CH03081P._CP', 17)
    LoadChip('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP', 18)
    LoadChip('ED6_DT27/CH03101._CH', 'ED6_DT27/CH03101P._CP', 19)
    LoadChip('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP', 20)
    LoadChip('ED6_DT27/CH03204._CH', 'ED6_DT27/CH03204P._CP', 21)
    LoadChip('ED6_DT26/CH20486._CH', 'ED6_DT26/CH20486P._CP', 22)
    LoadChip('ED6_DT27/CH03581._CH', 'ED6_DT27/CH03581P._CP', 23)
    LoadChip('ED6_DT27/CH03571._CH', 'ED6_DT27/CH03571P._CP', 24)
    LoadChip('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP', 25)
    LoadChip('ED6_DT27/CH03761._CH', 'ED6_DT27/CH03761P._CP', 26)
    LoadChip('ED6_DT27/CH03771._CH', 'ED6_DT27/CH03771P._CP', 27)
    ChrSetChipByIndex(0x0009, 23)
    ChrSetChipByIndex(0x0008, 24)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetChipByIndex(0x000B, 26)
    ChrSetChipByIndex(0x000C, 27)
    ChrSetChipByIndex(0x000E, 5)
    ChrSetChipByIndex(0x000F, 7)
    ChrSetChipByIndex(0x0010, 9)
    ChrSetChipByIndex(0x000D, 11)
    ChrSetChipByIndex(0x0011, 13)
    ChrSetChipByIndex(0x0012, 15)
    ChrSetChipByIndex(0x0013, 17)
    ChrSetChipByIndex(0x0014, 19)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    CreateThread(0x0015, 0x03, 0x00, func_04_1E09)
    CameraMove(-319380, -4000, 250640, 0)
    OP_67(0, 8370, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0000, 0)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    Sleep(500)

    CreateThread(0x0009, 0x01, 0x00, func_09_1F17)
    Sleep(350)

    CreateThread(0x0010, 0x01, 0x00, func_09_1F17)
    Sleep(500)

    CreateThread(0x000A, 0x01, 0x00, func_09_1F17)
    Sleep(310)

    CreateThread(0x0011, 0x01, 0x00, func_0A_1F47)
    Sleep(330)

    CreateThread(0x000D, 0x01, 0x00, func_0A_1F47)
    Sleep(650)

    CreateThread(0x0008, 0x01, 0x00, func_09_1F17)
    Sleep(450)

    CreateThread(0x000F, 0x01, 0x00, func_09_1F17)
    Sleep(450)

    CreateThread(0x000E, 0x01, 0x00, func_0A_1F47)
    Sleep(550)

    CreateThread(0x0012, 0x01, 0x00, func_09_1F17)
    Sleep(700)

    CreateThread(0x0014, 0x01, 0x00, func_0A_1F47)
    Sleep(460)

    CreateThread(0x000C, 0x01, 0x00, func_09_1F17)
    Sleep(400)

    CreateThread(0x000B, 0x01, 0x00, func_09_1F17)
    Sleep(530)

    CreateThread(0x0013, 0x01, 0x00, func_0A_1F47)
    Sleep(800)

    @scena.Lambda('lambda_056A')
    def lambda_056A():
        CameraMove(-276550, -4000, 250690, 10500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_056A)

    CreateThread(0x0102, 0x01, 0x00, func_07_1EC1)
    Sleep(650)

    CreateThread(0x0101, 0x01, 0x00, func_08_1EEC)
    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_059A')
    def lambda_059A():
        OP_9E(0x00FE, 40, 0, 300, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_059A)

    PlaySE(524, 0x00, 0x64)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 21)
    Sleep(100)

    @scena.Lambda('lambda_05C8')
    def lambda_05C8():
        ChrWalkTo(0x00FE, -245500, 0, 250500, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05C8)

    Sleep(1)

    TerminateThread(0x0101, 0x01)
    ChrSetSubChip(0x0101, 0)
    OP_DC()

    ChrTalk(
        0x0102,
        (
            '#0020421023V#1047F#5P呜……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010421024V#1020F#5P约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0654')
    def lambda_0654():
        CameraMove(-276180, -4000, 251130, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0654)

    @scena.Lambda('lambda_066C')
    def lambda_066C():
        OP_67(0, 7850, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_066C)

    @scena.Lambda('lambda_0684')
    def lambda_0684():
        CameraSetDistance(2220, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0684)

    @scena.Lambda('lambda_0694')
    def lambda_0694():
        OP_6C(315000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0694)

    @scena.Lambda('lambda_06A4')
    def lambda_06A4():
        OP_6E(367, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06A4)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0101, -275750, -4000, 251690, 5000, 0x00)
    ChrSetDirection(0x0101, 180, 500)
    ChrSetChipByIndex(0x0101, 25)
    ChrSetSubChip(0x0101, 0)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010421025V#1020F#2P没、没问题吗！？\n',
            '哪里受伤了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421026V#1035F#6P不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421027V#1043F只是……\n',
            '有点头晕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421028V#1026F#2P头晕……\n',
            '怎，怎么突然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0013, 18)
    TerminateThread(0x0013, 0x01)
    ChrSetPos(0x0013, -262920, 0, 254400, 270)
    ChrClearFlags(0x0013, 0x0080)

    ChrTalk(
        0x0013,
        (
            '#0180421029V#1P……可能是『圣痕』\n',
            '消失的后遗症吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210711V#1004F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 1)
    ChrSetPos(0x0013, -265180, 0, 250330, 270)
    ChrSetChipByIndex(0x0013, 17)
    ChrWalkTo(0x0013, -273610, -4000, 250620, 5000, 0x00)
    ChrSetChipByIndex(0x0013, 18)
    ChrSetSubChip(0x0013, 0)
    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#0180421031V#1063F毕竟是深植在\n',
            '意识底部的部分啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421032V如果被除去的话，\n',
            '必然会产生某种形式的反应。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421033V#1065F目眩、头痛、喘气……\n',
            '或许一段时间不得安宁吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421034V#1020F#5P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421035V#1053F#6P好了，艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)

    @scena.Lambda('lambda_0974')
    def lambda_0974():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_0974')

    DispatchAsync2(0x0102, 0x0003, lambda_0974)

    Sleep(200)

    Fade(250)
    ChrSetChipByIndex(0x0102, 65535)
    OP_0D()
    TerminateThread(0x0102, 0x03)
    Fade(250)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020421036V#1054F#6P我早就有所觉悟……\n',
            '才会请求凯文神父的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421037V#1026F#2P……约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -262920, 0, 254400, 270)

    ChrTalk(
        0x000A,
        (
            '#0540421038V#1P喂～！\n',
            '在干什么！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540421039V不快点的话就丢下你们了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010421040V#1004F#5P啊……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AB2')
    def lambda_0AB2():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_0AB2')

    DispatchAsync2(0x0101, 0x0001, lambda_0AB2)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010421041V#1015F#2P能走了吗，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421042V#1040F#6P啊啊，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0180421043V#1069F好……那就赶快了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0013, 90, 600)
    ChrSetChipByIndex(0x0013, 17)
    CreateThread(0x0013, 0x01, 0x00, func_0D_1FB9)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_0E_1FD3)

    @scena.Lambda('lambda_0B67')
    def lambda_0B67():
        CameraMove(-232890, 0, 251320, 8500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B67)

    @scena.Lambda('lambda_0B7F')
    def lambda_0B7F():
        OP_6E(446, 8500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B7F)

    Sleep(800)

    CreateThread(0x0101, 0x01, 0x00, func_0F_1FEF)
    WaitForThreadExit(0x0102, 0x0001)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    ChrSetDirection(0x0102, 270, 600)

    ChrTalk(
        0x0102,
        (
            '#0020421044V#1046F#5A艾丝蒂尔！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(800)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010421045V#1004F#5P#8A咦……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020421046V#1047F#3A唔……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(600)

    Sleep(100)

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    CameraMove(-234520, 0, 250530, 0)
    OP_67(0, 5200, -10000, 0)
    CameraSetDistance(2240, 0)
    OP_6C(315000, 0)
    OP_6E(446, 0)
    CreateThread(0x0101, 0x00, 0x00, func_05_1E32)
    CreateThread(0x0101, 0x01, 0x00, func_06_1E8C)
    Sleep(100)

    @scena.Lambda('lambda_0CAD')
    def lambda_0CAD():
        CameraMove(-238580, 0, 252000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0CAD)

    @scena.Lambda('lambda_0CC5')
    def lambda_0CC5():
        OP_67(0, 4200, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0CC5)

    ChrWalkTo(0x0102, -232000, 0, 250500, 6000, 0x00)
    ChrSetAfterImage(0x00, 0x0102, 0x0032, 0x01F4)
    ChrSetFlags(0x0102, 0x0002)
    ChrSetFlags(0x0102, 0x0020)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 22)
    PlaySE(571, 0x00, 0x64)

    @scena.Lambda('lambda_0D17')
    def lambda_0D17():
        ChrJumpTo(0x00FE, -241300, 0, 250500, 1000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D17)

    Sleep(150)

    ChrSetFlags(0x0101, 0x0080)
    ChrSetSubChip(0x0102, 2)

    @scena.Lambda('lambda_0D44')
    def lambda_0D44():
        OP_99(0x00FE, 0x02, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0D44)

    WaitForThreadExit(0x0102, 0x0001)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x0102, 0x0002)
    ChrSetAfterImage(0x01, 0x0102, 0x0000, 0x0000)
    ChrSetPos(0x0101, -241560, 0, 250460, 90)
    ChrSetPos(0x0102, -241790, 0, 250920, 90)
    Sleep(3000)

    @scena.Lambda('lambda_0D92')
    def lambda_0D92():
        CameraMove(-241630, 0, 251050, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D92)

    @scena.Lambda('lambda_0DAA')
    def lambda_0DAA():
        OP_67(0, 6300, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DAA)

    @scena.Lambda('lambda_0DC2')
    def lambda_0DC2():
        CameraSetDistance(2690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DC2)

    @scena.Lambda('lambda_0DD2')
    def lambda_0DD2():
        OP_6C(315000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0DD2)

    @scena.Lambda('lambda_0DE2')
    def lambda_0DE2():
        OP_6E(318, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0DE2)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0101, 0x0001)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(600)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(400)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x16),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x17),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x16),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x14),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x15),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x14),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010421047V#1004F#6P…………啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421048V#1043F#5P刚才的摇晃中，\n',
            '脆弱的部分崩塌了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(250)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(250)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(250)

    Fade(200)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0101, 0x0002)
    ChrClearFlags(0x0101, 0x0020)
    ChrClearFlags(0x0101, 0x0040)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetPos(0x0101, -241560, 0, 250460, 90)
    ChrClearFlags(0x0102, 0x0002)
    ChrClearFlags(0x0102, 0x0020)
    ChrClearFlags(0x0102, 0x0040)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetPos(0x0102, -241790, 0, 250920, 90)
    OP_0D()
    ChrMoveTo(0x0102, -241760, 0, 251420, 1000, 0x00)

    ChrTalk(
        0x0013,
        (
            '#0180421049V没，没事吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0013, -220520, 0, 250500, 270)
    ChrClearFlags(0x0013, 0x0080)

    @scena.Lambda('lambda_1026')
    def lambda_1026():
        CameraMove(-221300, 0, 250820, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1026)

    @scena.Lambda('lambda_103E')
    def lambda_103E():
        OP_67(0, 5810, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_103E)

    @scena.Lambda('lambda_1056')
    def lambda_1056():
        CameraSetDistance(3220, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1056)

    OP_6E(292, 3000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421050V#1016F嗯，嗯……还好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0010, -208710, 0, 248470, 0)
    ChrSetPos(0x0014, -208400, 0, 251230, 0)

    ChrTalk(
        0x0010,
        (
            '#0060421051V#1P#1163F艾丝蒂尔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0090421052V#1P#216F……约修亚……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1115')
    def lambda_1115():
        CameraMove(-219230, 0, 250420, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1115)

    CreateThread(0x0010, 0x01, 0x00, func_10_200B)
    Sleep(300)

    CreateThread(0x0014, 0x01, 0x00, func_11_2040)
    Sleep(300)

    CreateThread(0x000C, 0x01, 0x00, func_12_2075)
    Sleep(300)

    CreateThread(0x000B, 0x01, 0x00, func_13_20AA)
    Sleep(300)

    CreateThread(0x0011, 0x01, 0x00, func_14_20DF)
    Sleep(300)

    CreateThread(0x000D, 0x01, 0x00, func_15_2114)
    Sleep(300)

    CreateThread(0x000E, 0x01, 0x00, func_16_2149)
    Sleep(300)

    CreateThread(0x0012, 0x01, 0x00, func_17_217E)
    Sleep(300)

    CreateThread(0x000F, 0x01, 0x00, func_18_21B3)
    Sleep(300)

    CreateThread(0x000A, 0x01, 0x00, func_1B_2252)
    Sleep(300)

    CreateThread(0x0009, 0x01, 0x00, func_19_21E8)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, func_1A_221D)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(300)

    WaitForThreadExit(0x0011, 0x0001)

    ChrTalk(
        0x0011,
        (
            '#0070420946V#065F#6P姐姐！哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000D, 0x0001)

    ChrTalk(
        0x000D,
        (
            '#0050421054V#055F#6P怎么搞的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050421055V没有其他通道了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000E, 0x0001)

    ChrTalk(
        0x000E,
        (
            '#0030421056V#523F#4P去『中枢塔』的通道\n',
            '应该只有这里而已啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030421057V……唔……没有什么办法吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-241420, 0, 250780, 0)
    OP_67(0, 5810, -10000, 0)
    CameraSetDistance(3220, 0)
    OP_6C(315000, 0)
    OP_6E(292, 0)
    MapSetFlags(0x00000010)
    OP_0D()
    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x0102, 180, 400)
    Sleep(1500)

    ChrSetDirection(0x0101, 90, 400)
    ChrSetDirection(0x0102, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421058V#1008F#5P嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421059V别管我们，\n',
            '大家先逃出去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421060V#1040F#5P我们会想办法\n',
            '找到逃脱的方法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030421061V#024F#1P#3S别说傻话了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0030421062V#024F#1P要是把你们丢在这里不管，\n',
            '我还有什么脸去面对老师！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030421063V再仔细想一想！一定会有什么办法的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300383V#1003F#5P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421065V#1043F#5P对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-219230, 0, 250420, 0)
    OP_67(0, 5810, -10000, 0)
    CameraSetDistance(3220, 0)
    OP_6C(315000, 0)
    OP_6E(292, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0080421066V#074F#4P实际问题，这不是\n',
            '用跳跃就能飞过去的距离……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080421067V#072F这么一来……\n',
            '也就只能去寻找其他的通路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 90, 400)

    ChrTalk(
        0x0010,
        (
            '#0060421068V#1163F#5P其他的通路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060421069V但、但是！路只有一条吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0013, 18)
    ChrSetSubChip(0x0013, 0)

    @scena.Lambda('lambda_15FB')
    def lambda_15FB():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_15FB)

    Sleep(50)

    @scena.Lambda('lambda_160E')
    def lambda_160E():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_160E)

    Sleep(50)

    @scena.Lambda('lambda_1621')
    def lambda_1621():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1621)

    Sleep(50)

    @scena.Lambda('lambda_1634')
    def lambda_1634():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_1634)

    Sleep(50)

    @scena.Lambda('lambda_1647')
    def lambda_1647():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1647)

    Sleep(50)

    @scena.Lambda('lambda_165A')
    def lambda_165A():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_165A)

    Sleep(50)

    @scena.Lambda('lambda_166D')
    def lambda_166D():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_166D)

    ChrTalk(
        0x000F,
        (
            '#0040421070V#035F#6P不！那仅是限于\n',
            '这条地下通道而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040421071V#032F这个浮游都市本身\n',
            '似乎有好几条地下通道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040421072V只要能找到那样的道路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0290421073V#206F#2P这么说来…在『中枢塔』前面\n',
            '确实是见过其他的地下通道入口……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290421074V好像写着是通往『卡尔玛丽』\n',
            '的紧急避难通道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17C4')
    def lambda_17C4():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_17C4)

    Sleep(50)

    @scena.Lambda('lambda_17D7')
    def lambda_17D7():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_17D7)

    Sleep(50)

    @scena.Lambda('lambda_17EA')
    def lambda_17EA():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_17EA)

    Sleep(50)

    @scena.Lambda('lambda_17FD')
    def lambda_17FD():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_17FD)

    Sleep(50)

    @scena.Lambda('lambda_1810')
    def lambda_1810():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1810)

    Sleep(50)

    @scena.Lambda('lambda_1823')
    def lambda_1823():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_1823)

    Sleep(50)

    @scena.Lambda('lambda_1836')
    def lambda_1836():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1836)

    ChrTalk(
        0x0014,
        (
            '#0090421075V#415F真、真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0300421076V#490F啊啊，确实有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300421077V那个『卡尔玛丽』\n',
            '是你们的船所在的地方吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100421078V#173F啊，啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0110421079V#277F如果那里现在能用的话……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0540421080V#102F#6P唔，这个情况下\n',
            '锁定应该解除了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-241420, 0, 250780, 0)
    OP_67(0, 5810, -10000, 0)
    CameraSetDistance(3220, 0)
    OP_6C(315000, 0)
    OP_6E(292, 0)
    ChrSetDirection(0x0013, 270, 0)
    ChrSetDirection(0x0010, 270, 0)
    ChrSetDirection(0x0014, 270, 0)
    ChrSetDirection(0x000C, 270, 0)
    ChrSetDirection(0x000B, 270, 0)
    ChrSetDirection(0x0011, 270, 0)
    ChrSetDirection(0x000D, 270, 0)
    ChrSetDirection(0x000E, 270, 0)
    ChrSetDirection(0x0012, 270, 0)
    ChrSetDirection(0x000F, 270, 0)
    ChrSetDirection(0x000A, 270, 0)
    ChrSetDirection(0x0009, 270, 0)
    ChrSetDirection(0x0008, 270, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#0180421081V#1069F#1P艾丝蒂尔、约修亚！\n',
            '看来也没有其他选择了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180421082V就从那边\n',
            '返回『埃尔赛尤』吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421083V#1006F#5P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421084V#1040F#5P明白了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070421085V#063F#1P小，小心点哦！\n',
            '姐姐，哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060421086V#1162F#1P等你们……\n',
            '在『埃尔赛尤』上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421087V#1006F#5P嗯！\n',
            '大家也都要当心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-228030, 0, 251140, 0)
    OP_67(0, 3850, -10000, 0)
    CameraSetDistance(4970, 0)
    OP_6C(302000, 0)
    OP_6E(360, 0)
    ChrSetChipByIndex(0x0009, 23)
    CreateThread(0x0009, 0x01, 0x00, func_0B_1F77)
    Sleep(250)

    CreateThread(0x000A, 0x01, 0x00, func_0B_1F77)
    Sleep(300)

    ChrSetChipByIndex(0x0008, 24)
    CreateThread(0x0008, 0x01, 0x00, func_0C_1F98)
    Sleep(280)

    ChrSetChipByIndex(0x000F, 7)
    CreateThread(0x000F, 0x01, 0x00, func_0C_1F98)
    Sleep(150)

    ChrSetChipByIndex(0x0012, 15)
    CreateThread(0x0012, 0x01, 0x00, func_0B_1F77)
    Sleep(150)

    ChrSetChipByIndex(0x000E, 5)
    CreateThread(0x000E, 0x01, 0x00, func_0B_1F77)
    Sleep(200)

    ChrSetChipByIndex(0x000D, 11)
    CreateThread(0x000D, 0x01, 0x00, func_0B_1F77)
    Sleep(300)

    ChrSetChipByIndex(0x0011, 13)
    CreateThread(0x0011, 0x01, 0x00, func_0B_1F77)
    Sleep(300)

    ChrSetChipByIndex(0x000C, 27)
    CreateThread(0x000C, 0x01, 0x00, func_0B_1F77)
    Sleep(250)

    ChrSetChipByIndex(0x000B, 26)
    CreateThread(0x000B, 0x01, 0x00, func_0B_1F77)
    Sleep(120)

    ChrSetChipByIndex(0x0014, 19)
    CreateThread(0x0014, 0x01, 0x00, func_0C_1F98)
    Sleep(400)

    ChrSetChipByIndex(0x0010, 9)
    CreateThread(0x0010, 0x01, 0x00, func_0C_1F98)
    Sleep(250)

    ChrSetChipByIndex(0x0013, 17)
    CreateThread(0x0013, 0x01, 0x00, func_0B_1F77)
    Sleep(3000)

    Fade(500)
    CameraMove(-242080, 0, 251310, 0)
    OP_67(0, 5980, -10000, 0)
    CameraSetDistance(3840, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrSetDirection(0x0102, 180, 400)

    ChrTalk(
        0x0102,
        (
            '#0020421088V#1035F#2P好了……我们也赶快吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421089V#1042F看来离崩塌\n',
            '没有多少时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010421090V#1002F#6P嗯……明白！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421091V『中枢塔』前的\n',
            '紧急用的避难通道吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0x03)
    OP_72(0x0002, 0x0004)
    OP_72(0x0002, 0x0002)
    SetScenaFlags(ScenaFlag(0x0447, 6, 0x223E))
    OP_BB(0x01, 0x00, 0x00200053)
    OP_28(0x00A0, 0x01, 0x0002)
    OP_28(0x00A0, 0x01, 0x0004)
    OP_28(0x00A0, 0x01, 0x0008)
    Fade(1000)
    EventEnd(0x00)
    CreateThread(0x0015, 0x03, 0x00, func_04_1E09)
    MapSetFlags(0x02000000)
    MapSetFlags(0x00100000)

    Return()

# id: 0x0003 offset: 0x1DBA
@scena.Code('func_03_1DBA')
def func_03_1DBA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1E08',
    )

    OP_7C(60, 60, 1000, 900)
    Sleep(1500)

    OP_7C(40, 40, 1000, 1400)
    Sleep(1300)

    OP_7C(50, 50, 1000, 1600)
    Sleep(1700)

    Jump('func_03_1DBA')

    def _loc_1E08(): pass

    label('loc_1E08')

    Return()

# id: 0x0004 offset: 0x1E09
@scena.Code('func_04_1E09')
def func_04_1E09():
    OP_C4(0x00, 0x00000020)
    def _loc_1E0F(): pass

    label('loc_1E0F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1E31',
    )

    OP_7C(60, 60, 1000, 900)
    Sleep(1000)

    Jump('loc_1E0F')

    def _loc_1E31(): pass

    label('loc_1E31')

    Return()

# id: 0x0005 offset: 0x1E32
@scena.Code('func_05_1E32')
def func_05_1E32():
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetSubChip(0x0101, 1)
    ChrSetChipByIndex(0x0101, 22)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    Return()

# id: 0x0006 offset: 0x1E8C
@scena.Code('func_06_1E8C')
def func_06_1E8C():
    PlaySE(993, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 240)
    Sleep(1500)

    PlaySE(136, 0x00, 0x64)
    OP_7C(1000, 1000, 3000, 1500)
    OP_73(0x0001)
    OP_23(0x03E1)

    Return()

# id: 0x0007 offset: 0x1EC1
@scena.Code('func_07_1EC1')
def func_07_1EC1():
    ChrSetPos(0x00FE, -324210, -4000, 250500, 90)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -276120, -4000, 250500, 5000, 0x00)

    Return()

# id: 0x0008 offset: 0x1EEC
@scena.Code('func_08_1EEC')
def func_08_1EEC():
    ChrSetPos(0x00FE, -324210, -4000, 250500, 90)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -245500, 0, 250500, 5000, 0x00)

    Return()

# id: 0x0009 offset: 0x1F17
@scena.Code('func_09_1F17')
def func_09_1F17():
    ChrSetPos(0x00FE, -324210, -4000, 250500, 90)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -245500, 0, 252500, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000A offset: 0x1F47
@scena.Code('func_0A_1F47')
def func_0A_1F47():
    ChrSetPos(0x00FE, -324210, -4000, 250500, 90)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -245500, 0, 248500, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000B offset: 0x1F77
@scena.Code('func_0B_1F77')
def func_0B_1F77():
    ChrSetDirection(0x00FE, 90, 400)
    ChrWalkTo(0x00FE, -185290, -4000, 251660, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000C offset: 0x1F98
@scena.Code('func_0C_1F98')
def func_0C_1F98():
    ChrSetDirection(0x00FE, 90, 400)
    ChrWalkTo(0x00FE, -185170, -4000, 249520, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000D offset: 0x1FB9
@scena.Code('func_0D_1FB9')
def func_0D_1FB9():
    ChrWalkTo(0x00FE, -210500, 0, 250500, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000E offset: 0x1FD3
@scena.Code('func_0E_1FD3')
def func_0E_1FD3():
    ChrSetDirection(0x00FE, 90, 600)
    ChrWalkTo(0x00FE, -230000, 0, 250500, 6000, 0x00)

    Return()

# id: 0x000F offset: 0x1FEF
@scena.Code('func_0F_1FEF')
def func_0F_1FEF():
    ChrSetDirection(0x00FE, 90, 600)
    ChrWalkTo(0x00FE, -236000, 0, 250500, 5000, 0x00)

    Return()

# id: 0x0010 offset: 0x200B
@scena.Code('func_10_200B')
def func_10_200B():
    ChrSetPos(0x00FE, -208080, 0, 248880, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -220080, 0, 249200, 4000, 0x00)
    ChrSetChipByIndex(0x0010, 10)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0011 offset: 0x2040
@scena.Code('func_11_2040')
def func_11_2040():
    ChrSetPos(0x00FE, -208420, 0, 251710, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -220670, 0, 251830, 4000, 0x00)
    ChrSetChipByIndex(0x0014, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0012 offset: 0x2075
@scena.Code('func_12_2075')
def func_12_2075():
    ChrSetPos(0x00FE, -208420, 0, 251710, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -219360, 0, 251280, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 4)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0013 offset: 0x20AA
@scena.Code('func_13_20AA')
def func_13_20AA():
    ChrSetPos(0x00FE, -208420, 0, 251710, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -219090, 0, 252270, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 3)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0014 offset: 0x20DF
@scena.Code('func_14_20DF')
def func_14_20DF():
    ChrSetPos(0x00FE, -210070, 0, 248800, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -219550, 0, 247670, 4000, 0x00)
    ChrSetChipByIndex(0x0011, 14)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0015 offset: 0x2114
@scena.Code('func_15_2114')
def func_15_2114():
    ChrSetPos(0x00FE, -209920, 0, 249540, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -218280, 0, 246870, 4000, 0x00)
    ChrSetChipByIndex(0x000D, 12)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0016 offset: 0x2149
@scena.Code('func_16_2149')
def func_16_2149():
    ChrSetPos(0x00FE, -207570, 0, 250500, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -218780, 0, 249640, 4000, 0x00)
    ChrSetChipByIndex(0x000E, 6)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0017 offset: 0x217E
@scena.Code('func_17_217E')
def func_17_217E():
    ChrSetPos(0x00FE, -207570, 0, 250500, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -217680, 0, 251310, 4000, 0x00)
    ChrSetChipByIndex(0x0012, 16)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0018 offset: 0x21B3
@scena.Code('func_18_21B3')
def func_18_21B3():
    ChrSetPos(0x00FE, -209590, 0, 248860, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -218100, 0, 248340, 4000, 0x00)
    ChrSetChipByIndex(0x000F, 8)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0019 offset: 0x21E8
@scena.Code('func_19_21E8')
def func_19_21E8():
    ChrSetPos(0x00FE, -207570, 0, 250500, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -216360, 0, 250150, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 0)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001A offset: 0x221D
@scena.Code('func_1A_221D')
def func_1A_221D():
    ChrSetPos(0x00FE, -207570, 0, 250500, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -216750, 0, 247770, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 1)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001B offset: 0x2252
@scena.Code('func_1B_2252')
def func_1B_2252():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -207570, 0, 250500, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -217360, 0, 249570, 4000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
