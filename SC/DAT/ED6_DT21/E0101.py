import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0101.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3000,
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
        ('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP'),
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT26/CH20370._CH', 'ED6_DT26/CH20370P._CP'),
        ('ED6_DT26/CH20400._CH', 'ED6_DT26/CH20400P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT27/CH03015._CH', 'ED6_DT27/CH03015P._CP'),
        ('ED6_DT26/CH20401._CH', 'ED6_DT26/CH20401P._CP'),
        ('ED6_DT27/CH03101._CH', 'ED6_DT27/CH03101P._CP'),
        ('ED6_DT26/CH20398._CH', 'ED6_DT26/CH20398P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乔丝特',
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
            name                = '吉尔',
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
            name                = '多伦',
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
    )

# id: 0x10002 offset: 0x152
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x152
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x152
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x152
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_160',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_02_181)

    def _loc_160(): pass

    label('loc_160')

    Return()

# id: 0x0001 offset: 0x161
@scena.Code('func_01_161')
def func_01_161():
    PlaySE(121, 0x01, 0x3C)
    PlaySE(451, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_180',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_180(): pass

    label('loc_180')

    Return()

# id: 0x0002 offset: 0x181
@scena.Code('func_02_181')
def func_02_181():
    EventBegin(0x00)
    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    ChrSetFlags(0x0102, 0x0080)
    OP_DB()
    Yield()
    CameraMove(-289560, 30000, -136650, 0)
    OP_67(0, 2320, -10000, 0)
    CameraSetDistance(12030, 0)
    OP_6C(66000, 0)
    OP_6E(300, 0)
    OP_12(0x0000D6D8, 0x0007A120, 0x00000000)
    OP_EB(0xD5, 0x00)
    OP_BB(0x01, 0x01, 0x00000001)
    OP_BD()
    FadeIn(2000, 0)
    OP_12(0x0000D6D8, 0x00033450, 0x000032C8)

    @scena.Lambda('lambda_0200')
    def lambda_0200():
        CameraMove(-99550, 5550, -94010, 13000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0200)

    @scena.Lambda('lambda_0218')
    def lambda_0218():
        CameraSetDistance(2800, 13000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0218)

    @scena.Lambda('lambda_0228')
    def lambda_0228():
        OP_6E(334, 13000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0228)

    Sleep(7000)

    OP_72(0x0003, 0x0020)

    @scena.Lambda('lambda_0242')
    def lambda_0242():
        OP_6C(35000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0242)

    OP_67(0, 7540, -10000, 6000)
    PlaySE(106, 0x00, 0x64)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    OP_73(0x0000)
    Sleep(1000)

    ChrSetFlags(0x0008, 0x0004)
    ChrSetBattleFlags(0x0008, 0x0020)
    ChrSetPos(0x0008, -99440, 5550, -91440, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrWalkTo(0x0008, -99470, 5540, -93960, 2000, 0x00)
    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#0090320001V#213F#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    Sleep(500)

    ChrSetDirection(0x0008, 180, 400)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(500)

    ChrSetDirection(0x0008, 180, 400)
    ChrSetDirection(0x0008, 90, 400)
    Sleep(500)

    ChrSetPos(0x0102, -100000, 5550, -89500, 0)
    ChrSetFlags(0x0102, 0x0004)
    ChrClearFlags(0x0102, 0x0080)
    ChrSetFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetSubChip(0x0102, 2)
    CreateThread(0x0008, 0x01, 0x00, func_05_1432)

    @scena.Lambda('lambda_033D')
    def lambda_033D():
        CameraMove(-98020, 5550, -89450, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_033D)

    OP_6C(225000, 8000)

    ChrTalk(
        0x0008,
        (
            '#0090320002V#210F什么啊，原来在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0102, 1)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    ChrSetSubChip(0x0102, 3)
    Sleep(100)

    ChrSetSubChip(0x0102, 4)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020320003V#1031F……从这边可以\n',
            '比较清楚地看到月亮呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320004V肌肤也能感受到到风的流动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320005V#211F啊哈哈！又～在\n',
            '装模作样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0459')
    def lambda_0459():
        CameraMove(-99380, 5550, -89500, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0459)

    @scena.Lambda('lambda_0471')
    def lambda_0471():
        CameraSetDistance(2350, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0471)

    @scena.Lambda('lambda_0481')
    def lambda_0481():
        ChrWalkTo(0x0008, -99020, 5550, -89450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0481)

    WaitForThreadExit(0x0008, 0x0000)
    ChrSetDirection(0x0008, 0, 400)
    WaitForThreadExit(0x0102, 0x0001)
    Fade(250)
    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0090320006V#210F……哟咻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320007V#413F我可不是在\n',
            '装模作样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320008V#215F那是为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0102, 3)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020320009V#1035F#5P月光的亮度、云的位置、风的流动…\n',
            '在此时都变得相当重要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320010V#1031F我希望把失败的可能性\n',
            '尽量降到最低。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320011V#212F尽、尽量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0008, 4)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0090320012V#214F你啊……\n',
            '可别说什么能尽力而为的话哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320013V失败了就是死路一条啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320014V#1035F#5P别担心，失败的可能性很小。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320015V这种危险程度的任务，\n',
            '以前可是每天都会接触到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320016V#1033F真正的危险……\n',
            '不如说是在任务成功之后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320017V#212F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320018V#413F……我问你，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320019V你真的有必要\n',
            '做到这种地步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0102, 3)
    Sleep(100)

    ChrSetSubChip(0x0102, 4)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020320020V#1034F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320021V#215F你也和我们一样是\n',
            '埃雷波尼亚出身的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320022V#413F虽然说彼此或许各有隐情\n',
            '而不能返回故乡也说不定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320023V#212F但就算是这样，你也没必要\n',
            '对这个国家尽什么义务不是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320024V『结社』要做什么的话，\n',
            '随他们去做不就好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320025V#1033F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320026V#210F好不好，现在还来得及。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320027V就这个样子和我们一起\n',
            '离开利贝尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320028V去找个自治州\n',
            '揭竿而起怎么样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320029V如果不想做空贼，\n',
            '也可以找其它的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320030V#211F我和哥哥他们谈过，\n',
            '利用这艘飞船的速度\n',
            '来做运输业应该也不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 5)
    Sleep(75)

    ChrSetSubChip(0x0102, 6)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020320031V#1035F用飞船做运输业吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320032V这方面的需求今后还会增加，\n',
            '或许是相当有前途的行业呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320033V至少应该能赚得\n',
            '比当空贼还多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320034V#210F那、那么就！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0102, 5)
    Sleep(100)

    ChrSetSubChip(0x0102, 4)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020320035V#1031F说得也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320036V毁灭『结社』的计划之后，\n',
            '如果我还活着的话\n',
            '就考虑考虑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320037V#213F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320038V#1034F嗯嗯，你不用担心，\n',
            '我们的契约到此就结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320039V#1031F只要帮忙这个作战计划，\n',
            '之前欠我的人情就一笔勾销了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320040V你们随时都可以出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320041V#215F……够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320042V#1034F哎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetDirection(0x0008, 270, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0090320043V#214F笨蛋！\n',
            '谁在说什么欠人情的事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320044V#215F算了！\n',
            '我不管你了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320045V你爱跳入火坑、\n',
            '爱送死去的话就尽管去好了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 600)
    ChrSetChipByIndex(0x0008, 7)
    ChrWalkTo(0x0008, -94660, 5550, -90000, 6000, 0x00)
    ChrWalkTo(0x0008, -94810, 5550, -92930, 6000, 0x00)
    ChrWalkTo(0x0008, -99390, 5550, -93940, 6000, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    PlaySE(230, 0x00, 0x64)
    Sleep(300)

    OP_6F(0x0000, 0)
    OP_71(0x0000, 0x0010)
    Sleep(500)

    ChrSetSubChip(0x0102, 3)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(800)

    ChrSetSubChip(0x0102, 1)
    Sleep(140)

    ChrSetSubChip(0x0102, 2)
    Sleep(800)

    ChrTalk(
        0x0102,
        (
            '#0020320046V#1035F#5P……对不起，乔丝特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetBattleFlags(0x0009, 0x0020)
    ChrSetPos(0x0009, -103120, 13050, -91360, 10)
    OP_6F(0x0001, 35)
    Sleep(500)

    NpcTalk(
        0x0009,
        '青年的声音',
        (
            '#0290320047V#6P真是的……\n',
            '假装迟钝可真没意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 1)
    Sleep(50)

    ChrSetSubChip(0x0102, 0)
    OP_62(0x0102, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetPos(0x0009, -103120, 9050, -91360, 10)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x0009, 0x0020)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x0009, 0x0080)
    Fade(500)
    ChrClearFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    OP_0D()

    @scena.Lambda('lambda_0EB1')
    def lambda_0EB1():
        CameraMove(-100330, 5550, -92350, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0EB1)

    @scena.Lambda('lambda_0EC9')
    def lambda_0EC9():
        OP_67(0, 9500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0EC9)

    @scena.Lambda('lambda_0EE1')
    def lambda_0EE1():
        OP_6C(144000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0EE1)

    @scena.Lambda('lambda_0EF1')
    def lambda_0EF1():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0EF1)

    WaitForThreadExit(0x0102, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020320048V#1034F#6P……吉尔兄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290320049V#200F那家伙一样也是\n',
            '脱离不了小孩子个性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290320050V不过，刚才毕竟是\n',
            '你的说话方式不对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320051V#1035F#6P……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320052V#1033F虽然并不打算道歉，\n',
            '但还是觉得对不起她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290320053V#203F真是的……\n',
            '虽然知道这就是你\n',
            '关心别人的方式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290320054V#200F不过，刚才的话\n',
            '你还是认真考虑一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290320055V等一切都了结之后，\n',
            '要是你不打算回那个\n',
            '游击士小姑娘身边的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320056V#1031F#6P哈哈……那当然不会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320057V毕竟，我和她\n',
            '生存的世界差距太大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320058V已经不可能再走到一起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290320059V#200F呼……\n',
            '嗯，这倒也不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290320060V#202F那样的话\n',
            '也不算是件坏事情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320061V#1031F#6P是啊……\n',
            '我会好好考虑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(171, 0x01, 0x50)
    Sleep(500)

    OP_20(0x000003E8)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0290320062V#201F出现了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1226')
    def lambda_1226():
        ChrMoveTo(0x00FE, -103120, 8600, -91360, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1226)

    ChrSetDirection(0x0009, 270, 400)
    WaitForThreadExit(0x0009, 0x0001)
    PlayBGM(86)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0290320063V#201F#5P大哥，来了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, -103120, 6550, -91360, 270)

    NpcTalk(
        0x000A,
        '多伦的声音',
        (
            '#0300320064V#2P哦哦！\n',
            '正如那小子预料的一样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300320065V从东北方\n',
            '不断接近中呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_12FA')
    def lambda_12FA():
        ChrMoveTo(0x00FE, -103120, 9050, -91360, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_12FA)

    ChrSetDirection(0x0009, 10, 400)
    WaitForThreadExit(0x0009, 0x0001)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0290320066V#206F你听到了吧？\n',
            '马上到舰桥来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320067V#1032F#6P知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_137B')
    def lambda_137B():
        CameraMove(-100000, 5550, -89480, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_137B)

    @scena.Lambda('lambda_1393')
    def lambda_1393():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1393)

    @scena.Lambda('lambda_13AB')
    def lambda_13AB():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_13AB)

    @scena.Lambda('lambda_13BB')
    def lambda_13BB():
        OP_6C(135000, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_13BB)

    @scena.Lambda('lambda_13CB')
    def lambda_13CB():
        OP_6E(262, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_13CB)

    ChrSetDirection(0x0009, 270, 400)
    CreateThread(0x0009, 0x01, 0x00, func_04_141D)
    OP_23(0x00AB)
    OP_6F(0x0001, 35)
    OP_70(0x0001, 0)
    CreateThread(0x0009, 0x00, 0x00, func_03_140D)
    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    OP_D6(0x00)
    WaitForThreadExit(0x0102, 0x0001)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0003 offset: 0x140D
@scena.Code('func_03_140D')
def func_03_140D():
    Sleep(800)

    PlaySE(230, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0004 offset: 0x141D
@scena.Code('func_04_141D')
def func_04_141D():
    ChrMoveTo(0x00FE, -103120, 6050, -91360, 2000, 0x00)

    Return()

# id: 0x0005 offset: 0x1432
@scena.Code('func_05_1432')
def func_05_1432():
    ChrWalkTo(0x00FE, -94380, 5550, -92900, 1500, 0x00)
    ChrWalkTo(0x00FE, -94520, 5550, -90170, 1500, 0x00)
    ChrWalkTo(0x00FE, -95150, 5550, -89860, 1500, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x00FE, 270, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
