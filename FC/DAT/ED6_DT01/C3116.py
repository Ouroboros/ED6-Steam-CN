import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3116_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3116   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3116.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
        ('ED6_DT07/CH02450._CH', 'ED6_DT07/CH02450P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '希德少校',
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
            name                = '士兵的声音',
            x                   = -1100,
            z                   = 0,
            y                   = -3000,
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

# id: 0x10002 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xFA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xFA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xFA
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_106'),
        (-1, 'loc_11C'),
    )

    def _loc_106(): pass

    label('loc_106')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 0, 0x570)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 7, 0x56F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_119',
    )

    SetScenaFlags(ScenaFlag(0x00AE, 0, 0x570))
    Event(0, func_02_12A)

    def _loc_119(): pass

    label('loc_119')

    Jump('loc_11C')

    def _loc_11C(): pass

    label('loc_11C')

    Return()

# id: 0x0001 offset: 0x11D
@scena.Code('func_01_11D')
def func_01_11D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 3, 0x56B)),
            Expr.Return,
        ),
        'loc_129',
    )

    PlaySE(172, 0x01, 0x3C)

    def _loc_129(): pass

    label('loc_129')

    Return()

# id: 0x0002 offset: 0x12A
@scena.Code('func_02_12A')
def func_02_12A():
    EventBegin(0x00)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -820, 0, 4400, 180)
    ChrSetPos(0x0102, -1790, 0, -440, 0)
    ChrSetPos(0x0101, -1250, 0, 1250, 0)
    ChrSetPos(0x0106, -180, 0, 650, 0)
    ChrSetPos(0x0107, -170, 0, -450, 0)
    ChrSetPos(0x010B, -2090, 0, 580, 0)
    CameraMove(-590, 0, 2080, 0)
    OP_67(0, 7290, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0620091277V#701F真是千钧一发啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091278V#501F果然……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091279V#700F为了保险起见，快把门锁上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091280V#012F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_027C')
    def lambda_027C():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_027C')

    DispatchAsync2(0x0101, 0x0001, lambda_027C)

    @scena.Lambda('lambda_028D')
    def lambda_028D():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_028D')

    DispatchAsync2(0x0106, 0x0001, lambda_028D)

    @scena.Lambda('lambda_029E')
    def lambda_029E():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_029E')

    DispatchAsync2(0x0107, 0x0001, lambda_029E)

    @scena.Lambda('lambda_02AF')
    def lambda_02AF():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_02AF')

    DispatchAsync2(0x010B, 0x0001, lambda_02AF)

    ChrWalkTo(0x0102, -1070, 0, -1610, 3000, 0x00)
    ChrSetDirection(0x0102, 180, 400)
    Sleep(500)

    PlaySE(115, 0x00, 0x64)
    Sleep(500)

    ChrTurnDirection(0x0102, 0x0008, 400)
    Sleep(100)

    @scena.Lambda('lambda_02F6')
    def lambda_02F6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_02F6)

    @scena.Lambda('lambda_0304')
    def lambda_0304():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_0304)

    @scena.Lambda('lambda_0312')
    def lambda_0312():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0312)

    @scena.Lambda('lambda_0320')
    def lambda_0320():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x010B, 0x0002, lambda_0320)

    @scena.Lambda('lambda_032E')
    def lambda_032E():
        CameraMove(-740, 0, 3380, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_032E)

    @scena.Lambda('lambda_0346')
    def lambda_0346():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0346')

    DispatchAsync2(0x0101, 0x0002, lambda_0346)

    @scena.Lambda('lambda_0357')
    def lambda_0357():
        ChrWalkTo(0x00FE, -990, 0, 2780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0357)

    Sleep(200)

    @scena.Lambda('lambda_0377')
    def lambda_0377():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0377')

    DispatchAsync2(0x0106, 0x0002, lambda_0377)

    @scena.Lambda('lambda_0388')
    def lambda_0388():
        ChrWalkTo(0x00FE, 480, 0, 3330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0388)

    Sleep(100)

    @scena.Lambda('lambda_03A8')
    def lambda_03A8():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_03A8')

    DispatchAsync2(0x010B, 0x0002, lambda_03A8)

    @scena.Lambda('lambda_03B9')
    def lambda_03B9():
        ChrWalkTo(0x00FE, -1980, 0, 3570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010B, 0x0001, lambda_03B9)

    Sleep(100)

    @scena.Lambda('lambda_03D9')
    def lambda_03D9():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_03D9')

    DispatchAsync2(0x0107, 0x0002, lambda_03D9)

    @scena.Lambda('lambda_03EA')
    def lambda_03EA():
        ChrWalkTo(0x00FE, -90, 0, 2080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_03EA)

    Sleep(200)

    @scena.Lambda('lambda_040A')
    def lambda_040A():
        ChrWalkTo(0x00FE, -1960, 0, 2150, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_040A)

    Sleep(2500)

    ChrTalk(
        0x010B,
        (
            '#0540091281V#102F哼，你打算怎么样？\n',
            '雷斯顿要塞的守备队长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091282V那个理查德上校\n',
            '刚刚不是命令你要严密地监视我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091283V#703F……那个时候真是失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091284V#700F现在王国军已经被\n',
            '上校所管辖的情报部控制了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091285V军中的主要将领不是被上校收服，\n',
            '就是被剥夺了自由……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091286V摩尔根将军也被监禁在哈肯大门……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091287V#580F咦咦咦！？\n',
            '连那个顽固的老爷爷也……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091288V#012F情况好像变得很糟糕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091289V#055F喂喂……\n',
            '到底为什么会变成这样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091290V王国军不是那么脆弱的组织吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091291V#703F很遗憾……\n',
            '和帝国的战争结束后，\n',
            '王国军的军纪就渐渐散漫了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091292V特别是将领级别之间，\n',
            '互相攀比，争斗，受贿不断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091293V理查德上校就是钻了这个空子。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091294V#102F原来如此……\n',
            '利用其特有的情报掌控能力，\n',
            '然后逐一找到竞争对手的弱点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091295V#700F就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091296V现在摩尔根将军被监禁着，\n',
            '王国军实权已经落在了理查德上校手上。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091297V#007F怎、怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091298V#050F艾莉茜雅女王怎么样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091299V王国军的指挥权\n',
            '最终还是归属于女王的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091300V#703F虽然不清楚情况……\n',
            '但女王陛下一直保持着沉默。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091301V女王陛下直属的王室亲卫队\n',
            '刚刚也以谋反的罪名被追捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091302V#580F谋、谋反！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091303V尤莉亚中尉他们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091304V#702F他们将中央工房袭击事件\n',
            '伪装成王室亲卫队的所为。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091305V竟然周全到连照片都准备了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091306V#013F朵洛希的照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091307V#065F这、这太过分了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091308V#561F不仅把工房搞得乱七八糟，\n',
            '而且还绑架了爷爷……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091309V连阿加特大哥哥也差点被他们……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091310V#062F之后居然还嫁祸于人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091311V#703F啊……我无可辩驳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091312V虽说上级的命令不可不从……\n',
            '但是，默许的我也有不可推卸的责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091313V#701F因此……\n',
            '至少请让我在此向大家赎罪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091314V#051F真是忠义两难全啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091315V#104F嗯，既然这样，\n',
            '以前的种种恩怨就付诸流水吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091316V先让我用扳手敲敲你这木鱼脑袋，\n',
            '然后就饶了你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091317V#702F不、不胜惶恐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091318V#065F爷、爷爷真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091319V#100F开玩笑嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091320V#002F事情我们明白了……\n',
            '不过接下来你打算怎么办？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091321V让我们藏到风声过去吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091322V#700F不，我还有个更安全的办法。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091323V我可以帮你们通过这个房间\n',
            '安全地逃出雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091324V#004F这个房间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091325V#010F原来如此，\n',
            '这里有逃脱的密道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091326V#701F呵呵，很敏锐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 45, 400)

    @scena.Lambda('lambda_0DA1')
    def lambda_0DA1():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0DA1')

    DispatchAsync2(0x0101, 0x0001, lambda_0DA1)

    @scena.Lambda('lambda_0DB2')
    def lambda_0DB2():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0DB2')

    DispatchAsync2(0x0106, 0x0001, lambda_0DB2)

    @scena.Lambda('lambda_0DC3')
    def lambda_0DC3():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0DC3')

    DispatchAsync2(0x0107, 0x0001, lambda_0DC3)

    @scena.Lambda('lambda_0DD4')
    def lambda_0DD4():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0DD4')

    DispatchAsync2(0x010B, 0x0001, lambda_0DD4)

    @scena.Lambda('lambda_0DE5')
    def lambda_0DE5():
        CameraMove(3440, 0, 9720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DE5)

    @scena.Lambda('lambda_0DFD')
    def lambda_0DFD():
        ChrWalkTo(0x00FE, 3330, 0, 8810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0DFD)

    @scena.Lambda('lambda_0E18')
    def lambda_0E18():
        ChrSetDirection(0x00FE, 90, 0)
        Yield()

        Jump('lambda_0E18')

    DispatchAsync2(0x0008, 0x0001, lambda_0E18)

    Sleep(800)

    @scena.Lambda('lambda_0E2E')
    def lambda_0E2E():
        ChrSetDirection(0x00FE, 45, 0)
        Yield()

        Jump('lambda_0E2E')

    DispatchAsync2(0x0106, 0x0001, lambda_0E2E)

    @scena.Lambda('lambda_0E3F')
    def lambda_0E3F():
        ChrWalkTo(0x00FE, 2520, 0, 7610, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_0E3F)

    Sleep(50)

    @scena.Lambda('lambda_0E5F')
    def lambda_0E5F():
        ChrSetDirection(0x00FE, 45, 0)
        Yield()

        Jump('lambda_0E5F')

    DispatchAsync2(0x0107, 0x0001, lambda_0E5F)

    @scena.Lambda('lambda_0E70')
    def lambda_0E70():
        ChrWalkTo(0x00FE, 1940, 0, 6790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_0E70)

    Sleep(100)

    @scena.Lambda('lambda_0E90')
    def lambda_0E90():
        ChrSetDirection(0x00FE, 90, 0)
        Yield()

        Jump('lambda_0E90')

    DispatchAsync2(0x0101, 0x0001, lambda_0E90)

    @scena.Lambda('lambda_0EA1')
    def lambda_0EA1():
        ChrWalkTo(0x00FE, 1830, 0, 8330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0EA1)

    Sleep(350)

    @scena.Lambda('lambda_0EC1')
    def lambda_0EC1():
        ChrSetDirection(0x00FE, 45, 0)
        Yield()

        Jump('lambda_0EC1')

    DispatchAsync2(0x010B, 0x0001, lambda_0EC1)

    @scena.Lambda('lambda_0ED2')
    def lambda_0ED2():
        ChrWalkTo(0x00FE, 2800, 0, 6790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010B, 0x0002, lambda_0ED2)

    Sleep(50)

    @scena.Lambda('lambda_0EF2')
    def lambda_0EF2():
        ChrSetDirection(0x00FE, 90, 0)
        Yield()

        Jump('lambda_0EF2')

    DispatchAsync2(0x0102, 0x0001, lambda_0EF2)

    @scena.Lambda('lambda_0F03')
    def lambda_0F03():
        ChrWalkTo(0x00FE, 1000, 0, 7020, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0F03)

    WaitForThreadExit(0x0008, 0x0002)
    Sleep(100)

    OP_70(0x0000, 240)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010091327V#004F哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_73(0x0000)
    TerminateThread(0x0008, 0xFF)
    ChrSetDirection(0x0008, 0, 400)
    ChrWalkTo(0x0008, 2630, 0, 10220, 2000, 0x00)
    ChrSetDirection(0x0008, 180, 400)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0106,
        (
            '#0050091328V#051F不愧是要塞的司令室，\n',
            '各方面都很有一套嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091329V#703F使用这个紧急逃脱口，\n',
            '就能通往要塞内部的水道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091330V而且船已经准备好了，\n',
            '这样你们就能完全逃离这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091331V#701F本来把这个秘密告诉外人\n',
            '要被判处十年的监禁……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091332V哈哈……就算军规不能原谅，\n',
            '我想女神也会原谅我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10CC')
    def lambda_10CC():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10CC)

    @scena.Lambda('lambda_10DA')
    def lambda_10DA():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_10DA)

    @scena.Lambda('lambda_10E8')
    def lambda_10E8():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_10E8)

    @scena.Lambda('lambda_10F6')
    def lambda_10F6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x010B, 0x0001, lambda_10F6)

    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070091333V#063F少校先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091334V#051F那我们就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0107, 400)
    Sleep(400)

    ChrTalk(
        0x0106,
        (
            '#0050091335V#050F#2P我最先下去，\n',
            '接下来是老爷子和提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050091336V#054F#2P艾丝蒂尔、约修亚，\n',
            '殿后就交给你们两个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11EA')
    def lambda_11EA():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_11EA)

    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091337V#006F知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091338V#010F明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0106, 0x0004)
    ChrSetFlags(0x010B, 0x0004)
    ChrSetFlags(0x0107, 0x0004)
    ChrWalkTo(0x0106, 3310, 0, 8810, 5000, 0x00)
    ChrWalkTo(0x0106, 7840, 0, 9000, 5000, 0x00)

    ChrTalk(
        0x010B,
        (
            '#0540091339V#100F少校，再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x010B, 3310, 0, 8810, 5000, 0x00)
    ChrWalkTo(0x010B, 7840, 0, 9000, 5000, 0x00)

    ChrTalk(
        0x0107,
        (
            '#0070091340V#560F嗯，那个……\n',
            '真的非常感谢您呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0107, 3310, 0, 8810, 5000, 0x00)
    ChrWalkTo(0x0107, 7840, 0, 9000, 5000, 0x00)

    @scena.Lambda('lambda_1327')
    def lambda_1327():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1327)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091341V#006F好了……\n',
            '只剩下我们两个了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091342V少校，多谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, 2720, 0, 7650, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091343V#010F承蒙您的关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091344V#703F不，你们太客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091345V其实……\n',
            '当我最初遇到你们的时候，\n',
            '我就预料到事情会变成这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091346V#505F最初遇到的时候……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091347V#010F在大门遇到的时候吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091348V#701F啊啊……\n',
            '听到你们俩名字的那时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091349V你们是卡西乌斯上校的孩子吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091350V#505F卡西乌斯上校……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091351V#004F哎哎……\n',
            '老爸有这么高的军衔吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091352V#703F嗯，我和那个理查德上校\n',
            '都曾经是他的直属部下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091353V卡西乌斯上校是十年前\n',
            '百日战役时击退帝国军的英雄啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091354V#701F我想他的孩子们\n',
            '一定会为了追查真相，\n',
            '前来要塞营救博士的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091355V#004F是、是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091356V不过……\n',
            '老爸居然是击退帝国军的英雄……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(114, 0x00, 0x64)
    Sleep(300)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_16DB')
    def lambda_16DB():
        CameraMove(1910, 0, 8160, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_16DB)

    @scena.Lambda('lambda_16F3')
    def lambda_16F3():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16F3)

    @scena.Lambda('lambda_1701')
    def lambda_1701():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1701)

    ChrTurnDirection(0x0101, 0x0009, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0009,
        (
            '#4190091357V少校，可以进来吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190091358V入侵者似乎来过地牢！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190091359V他们依然潜伏在司令部的可能性很高，\n',
            '请问可以让我们进来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091360V#580F不、不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620091361V#704F#3S知道了！\n',
            '你们先原地待命！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1809')
    def lambda_1809():
        CameraMove(3440, 0, 9720, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1809)

    @scena.Lambda('lambda_1821')
    def lambda_1821():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1821)

    @scena.Lambda('lambda_182F')
    def lambda_182F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_182F)

    ChrSetDirection(0x0008, 180, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0620091362V#702F好了，你们快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091363V#002F嗯、嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091364V#012F那么我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18BC')
    def lambda_18BC():
        ChrWalkTo(0x00FE, 7840, 0, 9000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18BC)

    Sleep(600)

    @scena.Lambda('lambda_18DC')
    def lambda_18DC():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_18DC')

    DispatchAsync2(0x0008, 0x0001, lambda_18DC)

    ChrWalkTo(0x0102, 3310, 0, 8810, 5000, 0x00)
    ChrWalkTo(0x0102, 7840, 0, 9000, 5000, 0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_28(0x0044, 0x01, 0x0800)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C3114._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
