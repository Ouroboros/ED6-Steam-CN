import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2610_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2610   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2610.x'
    header.mapIndex       = 1
    header.bgm            = 32
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
            name                = '基尔巴特',
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
            name                = '莉秋儿',
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
            name                = '小丑肯帕雷拉',
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
            name                = '基库',
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

# id: 0x10002 offset: 0x128
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x128
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x128
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -80200,
            triggerZ            = 250,
            triggerY            = 31450,
            triggerRange        = 1000,
            actorX              = -80240,
            actorZ              = 250,
            actorY              = 32100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x14C
@scena.Code('Init')
def Init():
    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 6, 0x202E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_170',
    )

    Event(0, func_03_2F4)

    Jump('loc_170')

    def _loc_170(): pass

    label('loc_170')

    Return()

# id: 0x0001 offset: 0x171
@scena.Code('func_01_171')
def func_01_171():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 1, 0x1229)),
            Expr.Return,
        ),
        'loc_181',
    )

    OP_10(0x05, 0x00)
    OP_10(0x17, 0x01)

    Jump('loc_187')

    def _loc_181(): pass

    label('loc_181')

    OP_10(0x05, 0x01)
    OP_10(0x17, 0x00)

    def _loc_187(): pass

    label('loc_187')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0268, 1, 0x1341)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199',
    )

    OP_6F(0x000B, 0)

    Jump('loc_1A0')

    def _loc_199(): pass

    label('loc_199')

    OP_6F(0x000B, 60)

    def _loc_1A0(): pass

    label('loc_1A0')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0xF40),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D7')

    def _loc_1B8(): pass

    label('loc_1B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1C2',
    )

    Jump('loc_1D7')

    def _loc_1C2(): pass

    label('loc_1C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_1D7',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    def _loc_1D7(): pass

    label('loc_1D7')

    Return()

# id: 0x0002 offset: 0x1D8
@scena.Code('func_02_1D8')
def func_02_1D8():
    UnlockAchievement(0x02, 0x01FE, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0268, 1, 0x1341)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回复药'], 1)"),
            Expr.Return,
        ),
        'loc_24C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0268, 1, 0x1341))

    Jump('loc_2B2')

    def _loc_24C(): pass

    label('loc_24C')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0)

    def _loc_2B2(): pass

    label('loc_2B2')

    Jump('loc_2E6')

    def _loc_2B5(): pass

    label('loc_2B5')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_2E6(): pass

    label('loc_2E6')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x2F4
@scena.Code('func_03_2F4')
def func_03_2F4():
    Call(0, 0x0004)
    Call(0, 0x0005)

    Return()

# id: 0x0004 offset: 0x2FD
@scena.Code('func_04_2FD')
def func_04_2FD():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    LoadChip('ED6_DT26/CH20444._CH', 'ED6_DT26/CH20444P._CP', 0)
    LoadChip('ED6_DT26/CH20254._CH', 'ED6_DT26/CH20254P._CP', 1)
    LoadChip('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP', 2)
    LoadChip('ED6_DT26/CH20445._CH', 'ED6_DT26/CH20445P._CP', 3)
    LoadChip('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP', 4)
    LoadChip('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP', 5)
    LoadChip('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP', 6)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 7)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 8)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 9)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 10)
    LoadChip('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP', 11)
    LoadChip('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP', 12)
    LoadChip('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP', 13)
    LoadChip('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP', 14)
    LoadChip('ED6_DT27/CH03750._CH', 'ED6_DT27/CH03750P._CP', 15)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetChipByIndex(0x0009, 4)
    ChrSetChipByIndex(0x000A, 5)
    ChrSetChipByIndex(0x000B, 6)
    CameraMove(510, 0, 2770, 0)
    OP_67(0, 6890, -10000, 0)
    CameraSetDistance(2450, 0)
    OP_6C(45000, 0)
    OP_6E(311, 0)
    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x0101, 0x01, 0x00, func_08_2C42)
    Sleep(80)

    CreateThread(0x0102, 0x01, 0x00, func_09_2C8A)
    Sleep(200)

    CreateThread(0x010A, 0x01, 0x00, func_0A_2CD2)
    Sleep(70)

    CreateThread(0x010E, 0x01, 0x00, func_0B_2D1A)
    CameraMove(520, 0, 6900, 1500)
    ChrSetPos(0x0008, 30, 0, 16059, 180)

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#0480361039V#4P果然是你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetPos(0x0008, -190, 2000, 25350, 180)
    ChrSetPos(0x0009, 360, 2000, 25240, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    CameraMove(-50, 2000, 24730, 2500)
    PlayBGM(41)
    Sleep(1000)

    ChrSetChipByIndex(0x0101, 7)
    ChrSetChipByIndex(0x0102, 9)
    ChrSetChipByIndex(0x010A, 11)
    ChrSetChipByIndex(0x010E, 13)

    @scena.Lambda('lambda_0572')
    def lambda_0572():
        CameraMove(50, 1800, 20880, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0572)

    @scena.Lambda('lambda_058A')
    def lambda_058A():
        OP_67(0, 3650, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_058A)

    @scena.Lambda('lambda_05A2')
    def lambda_05A2():
        CameraSetDistance(2550, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_05A2)

    @scena.Lambda('lambda_05B2')
    def lambda_05B2():
        OP_6E(405, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_05B2)

    @scena.Lambda('lambda_05C2')
    def lambda_05C2():
        ChrWalkTo(0x00FE, -520, -50, 18350, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05C2)

    Sleep(80)

    @scena.Lambda('lambda_05E2')
    def lambda_05E2():
        ChrWalkTo(0x00FE, 930, -50, 18230, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05E2)

    Sleep(70)

    @scena.Lambda('lambda_0602')
    def lambda_0602():
        ChrWalkTo(0x00FE, -1050, 0, 16590, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0602)

    Sleep(80)

    @scena.Lambda('lambda_0622')
    def lambda_0622():
        ChrWalkTo(0x00FE, 590, 0, 16450, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_0622)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x010E, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010361040V#1005F#6P基尔巴特……是你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361041V#1221F哟，不要\n',
            '再靠近了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361042V如果不想\n',
            '伤害这位小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0009, 15, 0, 300, 3000)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#4030361043V#2P不、不要……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361044V#1020F#6P（啊……！\n',
            '科洛丝的学妹……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361045V#1042F#4P（是击剑部\n',
            '的女孩吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361046V#1222F你们每次\n',
            '都来妨碍我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361047V#1225F但是！\n',
            '这次，你们休想得逞！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361048V我要用这女孩作为礼物，\n',
            '提高在『结社』中的地位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361049V#1004F#6P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361050V#1226F看来『噬身之蛇』\n',
            '是个超乎想象的巨大组织。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361051V现在来到利贝尔的\n',
            '也只是极少的一部分……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361052V恐怕其影响力\n',
            '应该波及到大陆全境了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361053V#1221F呵呵，一定\n',
            '有出人头地的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361054V#814F#4P原来如此……\n',
            '还有这种想法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361055V#1007F#6P怎么说呢……\n',
            '这种向上爬的志向也过于可怜点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361056V#1225F住口！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361057V说到底，利贝尔这种\n',
            '小国岂能容得下我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361058V#1226F『噬身之蛇』\n',
            '才是我应该活跃的舞台！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361059V#1221F岂能容你们来捣乱！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361060V#1007F#6P嗯，本来想\n',
            '让你加油努力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361061V#1019F不过，我觉得就算你绑架了那孩子\n',
            '好像对你并不能有多大的帮助？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361062V#1226F哼，看来你们\n',
            '好像完全不知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361063V#1221F这女孩是隐姓埋名的\n',
            '利贝尔王室的公主！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#4030361064V#2P不、不是告诉你\n',
            '不是了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361065V#1221F哼……\n',
            '少来这套了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361066V#1226F据我打听\n',
            '那位公主似乎经常使用细剑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361067V而现在，击剑部的\n',
            '女学生只有你一个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361068V#1225F那么除了你还有谁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x0102)
    OP_63(0x0009)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#4030361069V#2P这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361070V#1019F#6P唉……怎么说你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361071V#1035F#4P也太会钻牛角尖了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361072V#1224F你、你们这是什么意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361073V#1007F#6P我说啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361074V#1019F你啊，还记不记得以前\n',
            '在巴伦诺灯塔被捕的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361075V#1225F怎、怎么可能忘记！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361076V一想到当时的事\n',
            '现在还一肚子火呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361077V#1048F#4P那和我们在一起的\n',
            '女学生你还记得吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361078V多少也算是见过一面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361079V#1221F……啊啊，是科洛丝吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361080V这么说来关起来的学生中\n',
            '好像没看到她……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361081V……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0008)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0480361082V#1224F#3S啊啊。',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361083V#1006F#6P就是这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361084V在灯塔科洛丝\n',
            '也用了细剑吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361085V#1224F这么说来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361086V#1225F……不、不对！\n',
            '不可能有这种蠢事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361087V事到如今\n',
            '我所做的一切都是白费吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361088V#819F#4P嗯……\n',
            '开始逃避现实了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330361089V#843F#4P……真可怜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361090V#1227F住、住口！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361091V#1225F无论如何，只要手上有人质\n',
            '我就是有利的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361092V如果你们不想她受到伤害\n',
            '就全体人员立即放下武器！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0009, 15, 0, 300, 3000)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#4030361093V#2P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361094V#1019F#6P（……真想把他\n',
            '  一脚踢飞。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361095V#1043F#4P（看看有什么机会……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361096V#1221F干、干什么！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361097V如果不照我说的做\n',
            '我就在她这可爱的脸蛋上──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x01, 'scraft\\\\sc000_11.eff')
    PlaySE(407, 0x00, 0x64)
    OP_20(0x000007D0)
    PlaySE(140, 0x00, 0x64)
    ChrSetPos(0x000B, -410, 5000, 5000, 0)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetAfterImage(0x00, 0x000B, 0x0032, 0x01F4)
    ChrClearFlags(0x000B, 0x0080)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x010E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    PlaySE(140, 0x00, 0x64)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 6)
    CreateThread(0x000B, 0x01, 0x00, func_10_2EE1)

    @scena.Lambda('lambda_12A2')
    def lambda_12A2():
        CameraMove(90, 3500, 13500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12A2)

    @scena.Lambda('lambda_12BA')
    def lambda_12BA():
        OP_6E(343, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_12BA)

    WaitForThreadExit(0x0101, 0x0002)
    PlayBGM(44)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_12DA')
    def lambda_12DA():
        CameraMove(430, 2000, 25000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12DA)

    @scena.Lambda('lambda_12F2')
    def lambda_12F2():
        CameraSetDistance(2300, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_12F2)

    ChrMoveTo(0x000B, 200, 2400, 25200, 26000, 0x00)
    ChrSetAfterImage(0x01, 0x000B, 0x0000, 0x0000)
    PlayEffect(0x01, 0x00, 0x0008, 0, 1600, 700, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    PlaySE(521, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)

    ChrTalk(
        0x0008,
        (
            '#1227F#20A呜！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#4030361099V#2P#20A呀！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x010A, 0x02)
    TerminateThread(0x010E, 0x02)
    ChrSetDirection(0x0101, 0, 0)
    ChrSetDirection(0x0102, 0, 0)
    ChrSetDirection(0x010A, 0, 0)
    ChrSetDirection(0x010E, 0, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0009, 0, 0)
    ChrSetChipByIndex(0x000B, 1)
    TerminateThread(0x000B, 0x01)

    @scena.Lambda('lambda_13E3')
    def lambda_13E3():
        OP_99(0x00FE, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_13E3')

    DispatchAsync2(0x000B, 0x0001, lambda_13E3)

    @scena.Lambda('lambda_13F6')
    def lambda_13F6():
        ChrMoveTo(0x000B, 500, 5600, 27800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_13F6)

    @scena.Lambda('lambda_1411')
    def lambda_1411():
        ChrSetDirection(0x00FE, 225, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1411)

    @scena.Lambda('lambda_141F')
    def lambda_141F():
        ChrMoveTo(0x00FE, 960, 2000, 24640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_141F)

    CreateThread(0x0008, 0x00, 0x00, func_0D_2DBA)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_14B1')
    def lambda_14B1():
        ChrSetDirection(0x00FE, 225, 300)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_14B1)

    @scena.Lambda('lambda_14BF')
    def lambda_14BF():
        OP_67(0, 3490, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_14BF)

    @scena.Lambda('lambda_14D7')
    def lambda_14D7():
        CameraSetDistance(2610, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_14D7)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010361100V#1005F#5P莉秋儿，这边！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#4030361101V#5P是、是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1543')
    def lambda_1543():
        CameraMove(-340, 2000, 22200, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1543)

    @scena.Lambda('lambda_155B')
    def lambda_155B():
        OP_67(0, 5880, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_155B)

    @scena.Lambda('lambda_1573')
    def lambda_1573():
        CameraSetDistance(2640, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1573)

    @scena.Lambda('lambda_1583')
    def lambda_1583():
        OP_6E(360, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1583)

    PlaySE(140, 0x00, 0x64)
    CreateThread(0x000B, 0x02, 0x00, func_0E_2E03)
    CreateThread(0x0009, 0x01, 0x00, func_0C_2D62)
    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000B,
        (
            '#0440361102V#310F#6P啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x0000012C, 1500, 0x28, 0x2B, 0x000000C8, 0x00)
    Sleep(200)

    ChrSetSubChip(0x0008, 1)
    Sleep(1000)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0480361103V#1224F#8P什、什、什…么…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361104V#1018F#5P基库……\n',
            '你怎么在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361105V#1044F#2P难不成\n',
            '是科洛丝要你来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440210795V#311F#6P啾～～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330361107V#841F#2P哈哈，真是佩服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361108V#811F好厉害！太厉害了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361109V#1224F#8P不、不可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480361110V#1227F这不可能啊啊啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361111V#1035F#2P好了，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361112V#1028F#5P开始惩罚吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_179B')
    def lambda_179B():
        CameraMove(370, 2000, 24910, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_179B)

    @scena.Lambda('lambda_17B3')
    def lambda_17B3():
        CameraSetDistance(2000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_17B3)

    @scena.Lambda('lambda_17C3')
    def lambda_17C3():
        ChrMoveTo(0x00FE, -580, 1750, 25610, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_17C3)

    Sleep(30)

    @scena.Lambda('lambda_17E3')
    def lambda_17E3():
        ChrMoveTo(0x00FE, 680, 1750, 25560, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_17E3)

    @scena.Lambda('lambda_17FE')
    def lambda_17FE():
        ChrMoveTo(0x00FE, -590, 750, 25710, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_17FE)

    Sleep(30)

    @scena.Lambda('lambda_181E')
    def lambda_181E():
        ChrMoveTo(0x00FE, 840, 750, 25660, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_181E)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x010E, 0xFF)
    TerminateThread(0x0009, 0xFF)
    Battle(0x00000F40, 0x0030000E, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1865'),
        (-1, 'loc_186A'),
    )

    def _loc_1865(): pass

    label('loc_1865')

    OP_B4(0x00)

    Jump('loc_186A')

    def _loc_186A(): pass

    label('loc_186A')

    Return()

# id: 0x0005 offset: 0x186B
@scena.Code('func_05_186B')
def func_05_186B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x010A, 0x01)
    TerminateThread(0x010E, 0x01)
    LoadChip('ED6_DT26/CH20444._CH', 'ED6_DT26/CH20444P._CP', 0)
    LoadChip('ED6_DT26/CH20254._CH', 'ED6_DT26/CH20254P._CP', 1)
    LoadChip('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP', 2)
    LoadChip('ED6_DT26/CH20445._CH', 'ED6_DT26/CH20445P._CP', 3)
    LoadChip('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP', 4)
    LoadChip('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP', 5)
    LoadChip('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP', 6)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 7)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 8)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 9)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 10)
    LoadChip('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP', 11)
    LoadChip('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP', 12)
    LoadChip('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP', 13)
    LoadChip('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP', 14)
    LoadChip('ED6_DT26/CH20450._CH', 'ED6_DT26/CH20450P._CP', 16)
    LoadChip('ED6_DT26/CH20451._CH', 'ED6_DT26/CH20451P._CP', 17)
    LoadChip('ED6_DT26/CH20298._CH', 'ED6_DT26/CH20298P._CP', 18)
    LoadChip('ED6_DT26/CH20305._CH', 'ED6_DT26/CH20305P._CP', 19)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, -680, 1000, 22880, 0)
    ChrSetPos(0x0102, 620, 1000, 22880, 0)
    ChrSetPos(0x010A, -750, 0, 21730, 0)
    ChrSetPos(0x010E, 650, 0, 21730, 0)
    ChrSetPos(0x0008, 240, 2000, 27150, 180)
    ChrSetPos(0x0009, 130, 0, 16730, 0)
    ChrSetChipByIndex(0x0101, 7)
    ChrSetChipByIndex(0x0102, 9)
    ChrSetChipByIndex(0x010A, 11)
    ChrSetChipByIndex(0x010E, 13)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x010A, 0)
    ChrSetSubChip(0x010E, 0)
    ChrSetChipByIndex(0x0009, 4)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x000A, 5)
    ChrSetSubChip(0x000A, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 0)
    ChrSetFlags(0x0008, 0x0800)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -3900, 5400, 25090, 90)
    ChrSetChipByIndex(0x000B, 2)
    ChrSetSubChip(0x000B, 0)
    CameraMove(270, 2000, 24030, 0)
    OP_67(0, 3150, -10000, 0)
    CameraSetDistance(2940, 0)
    OP_6C(32000, 0)
    OP_6E(337, 0)
    LoadEffect(0x00, 'map\\mp055_00.eff')
    LoadEffect(0x01, 'map\\mp093_00.eff')
    LoadEffect(0x02, 'map\\mp093_01.eff')
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0480361113V#1224F#5P……呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Fade(250)
    ChrSetChipByIndex(0x0008, 17)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    PlaySE(536, 0x00, 0x64)
    OP_99(0x0008, 0x00, 0x06, 1500)
    CreateThread(0x0008, 0x01, 0x00, func_06_2B84)

    ChrTalk(
        0x0008,
        (
            '#0480361114V#1227F#5P求、求求你们……\n',
            '饶我一条小命吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361115V#1007F#6P真受不了……\n',
            '不至于突然这么卑躬屈膝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361116V#819F#6P啊哈哈，到最后感觉\n',
            '好像在欺负弱者一样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330361117V#843F#4P这是自作自受。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330361118V#842F那么根据协会条约，\n',
            '在此逮捕你──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0190361119V那可不妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TerminateThread(0x0008, 0x01)
    ChrSetSubChip(0x0008, 7)
    OP_62(0x010E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetPos(0x000A, 190, 2000, 25290, 180)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrClearFlags(0x000A, 0x0080)
    PlayBGM(111)
    Sleep(500)

    @scena.Lambda('lambda_1CD1')
    def lambda_1CD1():
        CameraSetDistance(2100, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1CD1)

    @scena.Lambda('lambda_1CE1')
    def lambda_1CE1():
        CameraMove(870, 2000, 26560, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1CE1)

    @scena.Lambda('lambda_1CF9')
    def lambda_1CF9():
        OP_67(0, 4830, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1CF9)

    @scena.Lambda('lambda_1D11')
    def lambda_1D11():
        OP_6E(391, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1D11)

    PlayEffect(0x00, 0x01, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(266, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    CreateThread(0x0101, 0x00, 0x00, func_07_2BC1)
    WaitForThreadExit(0x0101, 0x0000)
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_1DDC')
    def lambda_1DDC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1DDC)

    Sleep(1500)

    StopEffect(0x01, 0x02)
    CreateThread(0x000A, 0x03, 0x00, func_11_2EF7)
    ChrSetSubChip(0x0008, 8)
    Sleep(200)

    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010361120V#1005F#5P你、你是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361121V#815F#5P废坑时出现的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361122V#1042F#5P……肯帕雷拉吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000A, 19)
    ChrSetSubChip(0x000A, 0)
    OP_99(0x000A, 0x00, 0x03, 1500)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0190361123V#853F#5P哈哈哈，诸位好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000A, 0x03, 0x00, 1500)
    ChrSetChipByIndex(0x000A, 5)
    ChrSetSubChip(0x000A, 0)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0190361124V#854F#5P我从你们突入学院开始\n',
            '就一直在旁观战……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190361125V#851F呀～这实在是太有趣了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190361126V没想到在这个时机\n',
            '临时演员突然登场啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440361127V#310F#6P啾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361128V#1221F#5P肯、肯帕雷拉大人……\n',
            '您是来救我的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    @scena.Lambda('lambda_2007')
    def lambda_2007():
        CameraMove(920, 2000, 27360, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2007)

    Sleep(500)

    OP_63(0x000A)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000A,
        (
            '#0190361129V#850F#6P……我说，基尔巴特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190361130V我可不记得有命令你\n',
            '掳走王室的公主啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0480361131V#1224F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0190361132V#853F#6P当然，根据现场状况\n',
            '而随机应变倒也不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190361133V我也并不打算\n',
            '计较这种小事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190361134V#854F……只是…\n',
            '如果失败的话，就毫无意义了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 15, 0, 300, 3000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0480361135V#1224F#5P呜……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetFlags(0x0008, 0x0020)
    ChrMoveTo(0x0008, 100, 2000, 27700, 1000, 0x00)
    ChrClearFlags(0x0008, 0x0020)
    Sleep(300)

    Fade(250)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetChipByIndex(0x000A, 18)
    ChrSetSubChip(0x000A, 0)
    OP_0D()
    OP_99(0x000A, 0x01, 0x02, 1500)
    PlaySE(188, 0x00, 0x64)
    Sleep(500)

    Fade(500)
    CameraMove(-90, 2500, 26730, 0)
    OP_67(0, 3870, -10000, 0)
    CameraSetDistance(2170, 0)
    OP_6C(1000, 0)
    OP_6E(391, 0)
    ChrSetPos(0x0101, -1090, 0, 18620, 0)
    ChrSetPos(0x0102, 180, -50, 18470, 0)
    ChrSetPos(0x010A, -1290, 0, 16900, 0)
    ChrSetPos(0x010E, -40, 0, 16760, 0)
    ChrSetPos(0x0009, -220, 0, 15100, 0)
    ChrSetPos(0x0008, -500, 2000, 26910, 180)
    ChrSetPos(0x000A, 0, 2000, 24750, 180)
    ChrClearFlags(0x000A, 0x0002)
    ChrSetChipByIndex(0x000A, 5)
    ChrSetSubChip(0x000A, 0)
    OP_0D()
    PlaySE(135, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1100, 1100, 1100, 0x00FF, 0, 0, 0, 0)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0001)
    ChrClearFlags(0x0008, 0x0800)
    ChrSetChipByIndex(0x0008, 16)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2316')
    def lambda_2316():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_2316')

    DispatchAsync2(0x0008, 0x0003, lambda_2316)

    ChrMoveTo(0x0008, -500, 2100, 26800, 8000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0480361136V#1227F#5P呜啊啊啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010361137V#1020F#5P怎、怎么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361138V#1035F#5P炎之舌……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361139V#1042F和露茜奥拉使用的一样\n',
            '是一种攻击性幻术吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0190361140V#851F#5P哈哈哈，我可\n',
            '没她用得那么好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190361141V#854F不过，这种水平的话还是可以应付的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0001)

    @scena.Lambda('lambda_2476')
    def lambda_2476():
        CameraMove(-90, 3500, 26730, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2476)

    StopEffect(0x01, 0x00)
    PlaySE(135, 0x00, 0x64)
    PlayEffect(0x02, 0x02, 0x0008, 0, 0, 0, 0, 0, 0, 1100, 1200, 1100, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_24CB')
    def lambda_24CB():
        OP_9E(0x00FE, 50, 0, 5000, 2000)
        Yield()

        Jump('lambda_24CB')

    DispatchAsync2(0x0008, 0x0003, lambda_24CB)

    ChrMoveTo(0x0008, -500, 3200, 26800, 8000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0480361142V#1227F#5P呜哇啊啊啊啊啊啊！！！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0190361143V#851F#5P不过，基尔巴特小丑一样的举动\n',
            '也挺让人开心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190361144V这次就免你一死，\n',
            '稍微惩罚一下就算了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    StopEffect(0x02, 0x02)
    OP_23(0x0087)

    @scena.Lambda('lambda_25C5')
    def lambda_25C5():
        CameraMove(0, 2000, 26730, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_25C5)

    TerminateThread(0x0008, 0x03)
    ChrMoveTo(0x0008, -500, 2000, 26800, 8000, 0x00)
    PlaySE(524, 0x00, 0x64)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 0)
    ChrSetFlags(0x0008, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0480361145V#5P……呜呜呜………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayEffect(0x00, 0x01, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(266, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010341722V#1005F#5P慢、慢着！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361147V#815F#5P又、又想逃跑吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0190361148V#851F#5P啊哈哈，这次嘛，\n',
            '我就向大家赔个不是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190361149V我发誓今后，『结社』\n',
            '绝不会再对这个学院出手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190361150V#854F那么各位──打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_2777')
    def lambda_2777():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2777)

    @scena.Lambda('lambda_2789')
    def lambda_2789():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2789)

    Sleep(1500)

    StopEffect(0x01, 0x02)
    CreateThread(0x000A, 0x03, 0x00, func_11_2EF7)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    Sleep(1000)

    Fade(1000)
    OP_20(0x000007D0)
    CameraMove(170, 2000, 25490, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(2330, 0)
    OP_6C(45000, 0)
    OP_6E(353, 0)
    ChrSetPos(0x0101, -730, 0, 18400, 0)
    ChrSetPos(0x0102, 790, 0, 18470, 0)
    ChrSetPos(0x010A, -1130, 0, 16880, 0)
    ChrSetPos(0x010E, 530, -50, 16790, 0)
    ChrSetPos(0x0009, -300, 0, 15300, 0)
    OP_0D()
    CreateThread(0x000B, 0x02, 0x00, func_0F_2E63)

    @scena.Lambda('lambda_285D')
    def lambda_285D():
        CameraMove(1020, -50, 18700, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_285D)

    @scena.Lambda('lambda_2875')
    def lambda_2875():
        OP_67(0, 5500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2875)

    @scena.Lambda('lambda_288D')
    def lambda_288D():
        CameraSetDistance(2310, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_288D)

    Sleep(2500)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010A, 65535)
    ChrSetChipByIndex(0x010E, 65535)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010361151V#1003F#6P又、又来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120361152V#1316F#6P被他逃跑了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330361153V#844F#4P『小丑』肯帕雷拉……\n',
            '真是个深不可测的少年啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361154V#1043F#2P嗯嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2980')
    def lambda_2980():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2980)

    Sleep(100)

    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0102,
        (
            '#0020361155V#1040F#5P不过，他的承诺\n',
            '在某种程度上应该可信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330361156V#845F#4P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361157V#1007F#5P唉，虽然不算圆满……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361158V#1025F但也\n',
            '算是告一段落了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A56')
    def lambda_2A56():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2A56)

    Sleep(100)

    ChrTurnDirection(0x010E, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120361159V#816F#6P嗯，这样也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000B, 0x0002)

    ChrTalk(
        0x000B,
        (
            '#0440361160V#311F#6P啾⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，强化猎兵\n',
            '侵占学院事件落下了帷幕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '王国军部队到达时\n',
            '学院内外的猎兵们\n',
            '已全数撤退……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '经过学院长和乔儿等人的努力\n',
            '学生们的不安也平息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/T2500._SN', 122, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x2B84
@scena.Code('func_06_2B84')
def func_06_2B84():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2BC0',
    )

    OP_9E(0x0008, 15, 0, 300, 3000)
    Sleep(1000)

    OP_9E(0x0008, 15, 0, 300, 3000)
    Sleep(1500)

    Jump('func_06_2B84')

    def _loc_2BC0(): pass

    label('loc_2BC0')

    Return()

# id: 0x0007 offset: 0x2BC1
@scena.Code('func_07_2BC1')
def func_07_2BC1():
    @scena.Lambda('lambda_2BC7')
    def lambda_2BC7():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -4000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2BC7)

    Sleep(50)

    @scena.Lambda('lambda_2BE7')
    def lambda_2BE7():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -4000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_2BE7)

    Sleep(200)

    @scena.Lambda('lambda_2C07')
    def lambda_2C07():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -4000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2C07)

    Sleep(50)

    @scena.Lambda('lambda_2C27')
    def lambda_2C27():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -4000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2C27)

    WaitForThreadExit(0x0101, 0x0001)

    Return()

# id: 0x0008 offset: 0x2C42
@scena.Code('func_08_2C42')
def func_08_2C42():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -470, 0, -1270, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2C69')
    def lambda_2C69():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C69)

    ChrWalkTo(0x00FE, -430, 0, 6650, 5000, 0x00)

    Return()

# id: 0x0009 offset: 0x2C8A
@scena.Code('func_09_2C8A')
def func_09_2C8A():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 630, 0, -1270, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2CB1')
    def lambda_2CB1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2CB1)

    ChrWalkTo(0x00FE, 700, 0, 6550, 5000, 0x00)

    Return()

# id: 0x000A offset: 0x2CD2
@scena.Code('func_0A_2CD2')
def func_0A_2CD2():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -470, 0, -1270, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2CF9')
    def lambda_2CF9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2CF9)

    ChrWalkTo(0x00FE, -1040, 0, 5320, 5000, 0x00)

    Return()

# id: 0x000B offset: 0x2D1A
@scena.Code('func_0B_2D1A')
def func_0B_2D1A():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 630, 0, -1270, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2D41')
    def lambda_2D41():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2D41)

    ChrWalkTo(0x00FE, 470, 0, 5300, 5000, 0x00)

    Return()

# id: 0x000C offset: 0x2D62
@scena.Code('func_0C_2D62')
def func_0C_2D62():
    ChrWalkTo(0x00FE, 550, 0, 21040, 5000, 0x00)
    ChrWalkTo(0x00FE, 2190, 0, 19550, 5000, 0x00)
    ChrWalkTo(0x00FE, 1880, 0, 14700, 5000, 0x00)
    ChrWalkTo(0x00FE, -70, 0, 14700, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000D offset: 0x2DBA
@scena.Code('func_0D_2DBA')
def func_0D_2DBA():
    ChrSetDirection(0x00FE, 180, 0)

    @scena.Lambda('lambda_2DC7')
    def lambda_2DC7():
        ChrJumpTo(0x00FE, -90, 2000, 26090, 1000, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2DC7)

    ChrSetFlags(0x0008, 0x0020)
    ChrSetChipByIndex(0x0008, 15)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 0)

    Return()

# id: 0x000E offset: 0x2E03
@scena.Code('func_0E_2E03')
def func_0E_2E03():
    ChrSetChipByIndex(0x000B, 6)
    OP_97(0x000B, -1360, 27260, 160000, 6000, 0x0001)
    ChrSetChipByIndex(0x000B, 1)
    ChrSetDirection(0x00FE, 90, 300)
    ChrMoveTo(0x00FE, -3900, 5100, 25090, 1000, 0x00)
    Fade(250)
    TerminateThread(0x000B, 0x01)
    ChrSetPos(0x000B, -3900, 5400, 25090, 90)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 2)
    OP_0D()

    Return()

# id: 0x000F offset: 0x2E63
@scena.Code('func_0F_2E63')
def func_0F_2E63():
    PlaySE(140, 0x00, 0x64)
    ChrSetChipByIndex(0x000B, 1)

    @scena.Lambda('lambda_2E73')
    def lambda_2E73():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_2E73')

    DispatchAsync2(0x000B, 0x0001, lambda_2E73)

    ChrMoveTo(0x00FE, -2900, 6000, 25090, 1000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, -2000, 1550, 21990, 2000, 0x00)
    ChrSetDirection(0x00FE, 135, 300)
    Sleep(100)

    Fade(250)
    TerminateThread(0x000B, 0x01)
    ChrSetPos(0x000B, -2000, 1750, 21990, 135)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 2)
    OP_0D()

    Return()

# id: 0x0010 offset: 0x2EE1
@scena.Code('func_10_2EE1')
def func_10_2EE1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2EF6',
    )

    OP_99(0x00FE, 0x00, 0x07, 3000)

    Jump('func_10_2EE1')

    def _loc_2EF6(): pass

    label('loc_2EF6')

    Return()

# id: 0x0011 offset: 0x2EF7
@scena.Code('func_11_2EF7')
def func_11_2EF7():
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

# id: 0x0012 offset: 0x2F3F
@scena.Code('func_12_2F3F')
def func_12_2F3F():
    NewScene('ED6_DT21/T2611._SN', 120, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
